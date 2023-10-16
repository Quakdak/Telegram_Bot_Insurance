import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
PASSWORD = os.getenv('PASSWORD')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
