from aiogram.types import Message
from lexicon.lexicon_ru import lexicon


async def error_photo(message: Message):
    await message.answer(text=lexicon['error_photo'])
