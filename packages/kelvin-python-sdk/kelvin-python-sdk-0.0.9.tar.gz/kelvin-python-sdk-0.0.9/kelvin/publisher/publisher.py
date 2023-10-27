from __future__ import annotations

import asyncio
import csv
import random
from abc import ABC, abstractmethod
from asyncio import Queue, StreamReader, StreamWriter
from datetime import datetime
from typing import AsyncGenerator, Callable, Dict, List, Optional, Tuple, Union

import arrow
import structlog
from pydantic import ValidationError
from pydantic.dataclasses import dataclass

from kelvin.app.config_msg import ConfigMessage, ConfigMessagePayload, Resource
from kelvin.app.stream import KelvinStreamConfig
from kelvin.message import (
    KRN,
    KMessageType,
    KMessageTypeData,
    KMessageTypeParameter,
    KRNAssetDataStream,
    KRNAssetParameter,
    KRNParameter,
    Message,
)
from kelvin.publisher.config import AppConfig, AssetsEntry, Metric, ParameterDefinition

structlog.reset_defaults()
logger = structlog.get_logger()


class PublisherError(Exception):
    pass


def flatten_dict(d: Dict, parent_key: str = "", sep: str = ".") -> Dict:
    items: list = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, Dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


class PublishServer:
    CYCLE_TIMEOUT_S = 0.25

    app_config: AppConfig
    allowed_assets: Optional[list[str]] = None
    asset_params: dict[Tuple[str, str], Union[bool, float, str]] = {}

    on_message: Callable[[Message], None]
    write_queue: Queue[Message]

    def __init__(self, conf: AppConfig, generator: DataGenerator) -> None:
        self.app_config = conf
        if self.app_config.app.kelvin.assets:
            self.allowed_assets = [asset.name for asset in self.app_config.app.kelvin.assets]

        self.writer = None
        self.on_message = log_message
        self.write_queue = Queue()
        self.host = "127.0.0.1"
        self.port = KelvinStreamConfig().port
        self.running = False
        self.generator = generator

    def update_param(self, asset: str, param: str, value: Union[bool, float, str]) -> None:
        """Sets an asset parameter.
        Empty asset ("") to change app default

        Args:
            asset (Optional[str]): asset name (empty ("") for fallback)
            param (str): param name
            value (Union[bool, float, str]): param value
        """
        self.asset_params[(asset, param)] = value

    def add_extra_assets(self, assets_extra: list[str]) -> None:
        self.allowed_assets = assets_extra

    def build_config_message(self) -> ConfigMessage:
        # Prepare app parameters
        flat_config = flatten_dict(self.app_config.app.kelvin.configuration)
        resources: List[Resource] = [Resource(type="app", parameters=flat_config)]

        # Prepare asset parameters
        # Parameter priority: asset override > override default > asset param on app config > default on app config
        for asset_name in self.allowed_assets or []:
            asset_params = {}
            for param in self.app_config.app.kelvin.parameters:
                payload = self.asset_params.get((asset_name, param.name), None) or self.asset_params.get(
                    ("", param.name), None
                )
                if payload is None:
                    try:
                        asset = next(asset for asset in self.app_config.app.kelvin.assets if asset.name == asset_name)
                        payload = (
                            asset.parameters.get(param.name, {}).get("value", None) or param.default.get("value", None)
                            if param.default
                            else None
                        )
                    except StopIteration:
                        pass

                if payload is None:
                    # asset has no parameter and parameter doesn't have default value
                    continue

                asset_params[param.name] = payload

            resources.append(Resource(type="asset", name=asset_name, parameters=asset_params))

        return ConfigMessage(resource=KRNParameter("configuration"), payload=ConfigMessagePayload(resources=resources))

    async def start_server(self) -> None:
        server = await asyncio.start_server(self.new_client, self.host, self.port)

        addr = server.sockets[0].getsockname()
        logger.info(f"Serving on {addr}")

        async with server:
            await server.serve_forever()

    async def new_client(self, reader: StreamReader, writer: StreamWriter) -> None:
        if self.running is True:
            writer.close()
            return

        logger.info("Connected")
        self.running = True

        connection_tasks = {
            asyncio.create_task(self.handle_read(reader)),
            asyncio.create_task(self.handle_write(writer, self.write_queue)),
        }

        gen_task = asyncio.create_task(self.handle_generator(self.generator))

        config_msg = self.build_config_message()
        writer.write(config_msg.encode() + b"\n")
        try:
            await writer.drain()
        except ConnectionResetError:
            pass

        _, pending = await asyncio.wait(connection_tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in pending:
            task.cancel()

        if not task.done():
            gen_task.cancel()

        self.running = False
        logger.info("Disconnected")

    async def handle_read(self, reader: StreamReader) -> None:
        while self.running:
            data = await reader.readline()
            if not len(data):
                break
            try:
                msg = Message.parse_raw(data)
                self.on_message(msg)
            except Exception:
                logger.exception("error parsing message")

    async def handle_write(self, writer: StreamWriter, queue: Queue[Message]) -> None:
        while self.running and not writer.is_closing():
            try:
                msg = await asyncio.wait_for(queue.get(), timeout=self.CYCLE_TIMEOUT_S)
            except asyncio.TimeoutError:
                continue

            writer.write(msg.encode() + b"\n")

            try:
                await writer.drain()
            except ConnectionResetError:
                pass

    async def handle_generator(self, generator: DataGenerator) -> None:
        async for data in generator.run():
            await self.publish_data(data)

    async def publish_unsafe(self, msg: Message) -> None:
        """Publish the message as is, do not validate it against the app configuration

        Args:
            msg (Message): message to publish
        """
        await self.write_queue.put(msg)

    async def publish_data(self, data: MessageData) -> bool:
        if self.allowed_assets is not None and len(data.asset) > 0 and data.asset not in self.allowed_assets:
            logger.error("error publishing: asset not allowed to app", asset=data.asset)
            return False

        # if data.asset is empty publish to all allowed_assets (if set)
        assets = [data.asset] if len(data.asset) > 0 else self.allowed_assets
        if assets is None:
            logger.error("error publishing to empty asset: no allowed assets set")
            return False

        app_resource: Union[Metric, ParameterDefinition, None] = None
        msg_resource_builder: Optional[type[KRN]] = None
        try:
            # check is app input
            app_resource = next(i for i in self.app_config.app.kelvin.inputs if i.name == data.resource)
            msg_type: KMessageType = KMessageTypeData(primitive=app_resource.data_type)
            msg_resource_builder = KRNAssetDataStream
        except StopIteration:
            try:
                # check is app param
                app_resource = next(p for p in self.app_config.app.kelvin.parameters if p.name == data.resource)
                msg_type = KMessageTypeParameter(primitive=app_resource.data_type)
                msg_resource_builder = KRNAssetParameter
            except StopIteration:
                app_resource = None

        if app_resource is None or msg_resource_builder is None:
            # invalid resource for this app
            logger.error("error publishing: invalid resource to app", asset=data.asset, resource=data.resource)
            return False

        for asset in assets:
            try:
                msg = Message(
                    type=msg_type,
                    timestamp=data.timestamp or datetime.now().astimezone(),
                    resource=msg_resource_builder(asset, data.resource),
                    payload=data.value,
                )

                await self.write_queue.put(msg)
            except ValidationError:
                logger.exception("publish_value: invalid value for resource", resource=data.resource, value=data.value)
        return True


def log_message(msg: Message) -> None:
    logger.info("New message:\n", msg=msg)


@dataclass
class MessageData:
    asset: str
    resource: str
    timestamp: Optional[datetime]
    value: Union[bool, float, str]


class DataGenerator(ABC):
    @abstractmethod
    async def run(self) -> AsyncGenerator[MessageData, None]:
        if False:
            yield  # trick for mypy


class CSVPublisher(DataGenerator):
    period: float

    def __init__(self, csv_file_path: str, period: float):
        self.period = period
        self.csv_file_path = csv_file_path

    async def run(self) -> AsyncGenerator[MessageData, None]:
        self.csv_file = open(self.csv_file_path)
        self.csv_reader = csv.reader(self.csv_file)
        self.headers = next(self.csv_reader)

        for row in self.csv_reader:
            row_dict = dict(zip(self.headers, row))

            asset = row_dict.pop("asset", "")
            ts_str = row_dict.pop("timestamp", None)
            timestamp = None
            if ts_str is not None:
                try:
                    timestamp = datetime.fromtimestamp(int(ts_str))
                except ValueError:
                    try:
                        timestamp = arrow.get(ts_str).datetime if ts_str is not None else None
                    except Exception:
                        logger.exception("csv: error parsing timestamp, skipping value", timestamp=ts_str)
            for r, v in row_dict.items():
                yield MessageData(asset=asset, resource=r, value=v, timestamp=timestamp)

            await asyncio.sleep(self.period)

        logger.info("csv: publishing data from the CSV file is complete")


class Simulator(DataGenerator):
    app_yaml: str
    app_config: AppConfig
    rand_min: float
    rand_max: float
    random: bool
    current_value: float
    assets: list[AssetsEntry]
    params_override: dict[str, Union[bool, float, str]]

    def __init__(
        self,
        app_config: AppConfig,
        period: float,
        rand_min: float = 0,
        rand_max: float = 100,
        random: bool = True,
        assets_extra: list[str] = [],
        parameters_override: list[str] = [],
    ):
        self.app_config = app_config
        self.period = period
        self.rand_min = rand_min
        self.rand_max = rand_max
        self.random = random
        self.current_value = 0.0
        self.params_override: dict[str, Union[bool, float, str]] = {}

        for override in parameters_override:
            param, value = override.split("=", 1)
            self.params_override[param] = value

        if len(assets_extra) > 0:
            self.assets = [AssetsEntry(name=asset, parameters={}) for asset in assets_extra]
        elif self.app_config.app.kelvin.assets:
            self.assets = self.app_config.app.kelvin.assets
        else:
            raise PublisherError("No assets set")

    def generate_random_value(self, data_type: str) -> Union[bool, float, str]:
        if data_type == "boolean":
            return random.choice([True, False])

        if self.random:
            number = round(random.random() * (self.rand_max - self.rand_min) + self.rand_min, 2)
        else:
            self.current_value = (self.current_value + 1) % (self.rand_max - self.rand_min) + self.rand_min
            number = self.current_value

        if data_type == "number":
            return number

        # if data_type == "string":
        return f"str_{number}"

    async def run(self) -> AsyncGenerator[MessageData, None]:
        while True:
            for input in self.app_config.app.kelvin.inputs:
                for asset in self.assets:
                    yield MessageData(
                        asset=asset.name,
                        resource=input.name,
                        value=self.generate_random_value(input.data_type),
                        timestamp=None,
                    )

            await asyncio.sleep(self.period)
