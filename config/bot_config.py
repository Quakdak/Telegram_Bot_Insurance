import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import logging

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
PASSWORD = os.getenv('PASSWORD')

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
