import asyncio
from contextlib import asynccontextmanager

from databases import Database

database = Database('postgresql://postgres:pg_secret@localhost:5432/postgres')


@asynccontextmanager
async def get_db(db: Database):
    await db.connect()
    yield db
    await db.disconnect()


async def main():
    async with get_db(database) as db:
        async with db.connection() as conn:
            rows = await conn.fetch_all('SELECT * from book WHERE id = 1;')
            print(dict(rows[0]))


if __name__ == '__main__':
    asyncio.run(main())
