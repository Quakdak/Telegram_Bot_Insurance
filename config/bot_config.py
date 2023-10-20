import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

ip = os.getenv('ip')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = F'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
