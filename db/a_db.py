import aiosqlite
from db import sql_queries

class AsyncDatabase:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path

    async def create_tables(self):
        async with aiosqlite.connect(self.db_path) as db:
           await db.execute(sql_queries.CREATE_USER_TABLE_QUERY)

           await db.commit()
           print("Database connected successfully")