__all__ = ['start', 'register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart, Command

from config.bot_config import PASSWORD
from handlers.start_handler import start
from handlers.admin_panel.add_admin import add_admin
from handlers.admin_panel.delete_admin import delete_admin


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.message.register(add_admin, Command(commands=[PASSWORD]))
    router.message.register(delete_admin, Command(commands=['Вернутьсяя в режим пользователя']))
