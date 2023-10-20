"""import asyncio

from config import bot_config
from utils.db_api.db_gino import db
import quick_commands as commands


async def db_test():
    await db.set_bind(bot_config.POSTGRES_URI)
    await db.gino.drop_all() # удаление всех данных
    await db.gino.create_all()

    await commands.add_user(1, 'Vlad')
    await commands.add_user(2, 'Kak', 'arrarat')
    await commands.add_user(3, 'ADS')
    await commands.add_user(4, 'Valera')
    await commands.add_user(12313, 'SIS')

    users = await commands.select_all_users()
    print(users)
    count = await commands.count_users()
    print(count)
    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, 'new_ebda')

    user = await commands.select_user(1)
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
"""
