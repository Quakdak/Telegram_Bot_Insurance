import asyncio
from aiogram import types

from config.bot_config import dp, bot
from handlers import register_user_commands


async def main():
    register_user_commands(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
