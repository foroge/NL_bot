import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters.command import Command

from services.logging import logger
from config.config import Config, load_config


async def main():
    config: Config = load_config()

    logger.info("Starting bot")

    bot_properties: DefaultBotProperties = DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )

    bot: Bot = Bot(token=config.TelegramToken.TOKEN, default=bot_properties)
    dp: Dispatcher = Dispatcher()

if __name__ == "__main__":
    asyncio.run(main())
