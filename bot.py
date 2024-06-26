import asyncio

from aiogram import Dispatcher, Bot
from config_data.config import Config, load_config

from handlers.main_handlers import router as main_router


async def main():
    config: Config = load_config(".env")
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(main_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
