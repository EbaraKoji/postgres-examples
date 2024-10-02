import asyncio
from contextlib import asynccontextmanager

import asyncpg
from asyncpg.connection import Connection


@asynccontextmanager
async def get_async_db(
    host='localhost',
    port=5432,
    database='postgres',
    user='postgres',
    password='pg_secret',
):
    conn: Connection = await asyncpg.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
    )
    yield conn
    await conn.close()


async def main():
    async with get_async_db() as conn:
        row: asyncpg.Record = await conn.fetchrow('SELECT * FROM book;')
        print(row)
        print(f"title: {row.get('title')}")
        print(f"pages: {row.get('pages')}")


if __name__ == '__main__':
    asyncio.run(main())
