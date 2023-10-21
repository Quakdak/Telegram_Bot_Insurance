import os

from dotenv import load_dotenv

from config.bot_config import bot

load_dotenv()


async def get_photo(photo_id: str):
    file = await bot.get_file(photo_id)
    file_path = file.file_path
    file_url = f'https://api.telegram.org/file/bot{os.getenv("API_TOKEN")}/{file_path}'
    return file_url


async def get_photo_res(photo_id: str):
    file_info = await bot.get_file(photo_id)
    photo_resolution = file_info.width, file_info.height
    return photo_resolution
