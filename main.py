import asyncio

from config import dp, bot
from db.a_db import AsyncDatabase
from handlers import setup_routes


async def main():
    db= AsyncDatabase()
    await db.create_tables()
    router = setup_routes()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())