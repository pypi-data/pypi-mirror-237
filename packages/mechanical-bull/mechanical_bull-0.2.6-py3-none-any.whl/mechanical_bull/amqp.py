import tomllib
import asyncio
import logging
import aiohttp

from bovine import BovineClient
from bovine_pubsub.amqp_manager import AmqpManager

from .handlers import load_handlers


async def amqp_mechanical_bull(config_file):
    with open(config_file, "rb") as fp:
        config = tomllib.load(fp)

    if "logfile" in config:
        logging.basicConfig(level=logging.INFO, filename=config["logfile"])
    else:
        logging.basicConfig(level=logging.INFO)

    manager = AmqpManager("amqp://localhost", queue_name="mechanical_bull")
    await manager.init()

    async with aiohttp.ClientSession() as session:
        handlers_for_client = {}
        for client_name, value in config.items():
            if isinstance(value, dict):
                client = BovineClient(**value)
                await client.init(session=session)

                await manager.add_bovine_client(client)

                handlers_for_client[client.information["id"]] = load_handlers(
                    value["handlers"]
                )
        async with manager.iter() as iterator:
            async for client, data in iterator:
                for handler in handlers_for_client[client.information["id"]]:
                    await handler(client, data)


def main():
    asyncio.run(amqp_mechanical_bull("config.toml"))


if __name__ == "__main__":
    main()
