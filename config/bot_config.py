import logging
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

config = dotenv_values(".env")
API_TOKEN=config["API_TOKEN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)