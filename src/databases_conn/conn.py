import asyncio
from contextlib import asynccontextmanager

from databases import Database

database = Database(
    'postgresql+asyncpg://postgres:pg_secret@localhost:5432/postgres',
    ssl=False,  # In remote this should be True, but PostgreSQL server at "localhost:5432" rejects SSL upgrade.
)


@asynccontextmanager
async def get_db(db: Database):
    await db.connect()
    yield db
    await db.disconnect()


@get_db(database)
async def main():
    async with database.connection() as conn:
        rows = await conn.fetch_all('SELECT * from book WHERE id = 1;')
        print(dict(rows[0]))


if __name__ == '__main__':
    asyncio.run(main())
