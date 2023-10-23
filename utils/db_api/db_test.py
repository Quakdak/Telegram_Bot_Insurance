import asyncio

from config import bot_config
from utils.db_api.db_gino import db
import quick_commands as commands


async def db_test():
    await db.set_bind(bot_config.POSTGRES_URI)
    # await db.gino.drop_all()  # удаление всех данных
    # await db.gino.create_all()

    await commands.add_user(user_id=1, first_name='AAA', last_name='DDD', is_admin=False)
    await commands.add_user(user_id=2, first_name='BBB', last_name='BBB', is_admin=False)
    await commands.add_user(user_id=3, first_name='YYY', last_name='RRR', is_admin=False)

    user = await commands.select_user(871122808)



loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
