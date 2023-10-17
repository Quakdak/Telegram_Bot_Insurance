__all__ = ['start', 'register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from config.bot_config import PASSWORD
from handlers.start_handler import start


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())

