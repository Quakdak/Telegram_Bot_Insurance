import os

from aiogram import Bot, Dispatcher

API_TOKEN = os.getenv('token')
PASSWORD = os.getenv('password')

bot = Bot(token=os.getenv('token'))
dp = Dispatcher()
