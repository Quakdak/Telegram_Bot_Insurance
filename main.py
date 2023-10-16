import asyncio

from config.bot_config import dp, bot
from handlers import register_user_commands
from aiogram.types import BotCommand

bot_commands = (
    ("start", "Начало работы с ботом"),
)


async def main():
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
