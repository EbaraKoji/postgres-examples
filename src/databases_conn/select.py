import asyncio
from pprint import pprint

from conn import database, get_db
from sqlalchemy import Column, Integer, MetaData, String, Table, select

metadata = MetaData()
book_table = Table(
    'book',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('pages', Integer),
    Column('author', String(255)),
)


@get_db(database)
async def main():
    async with database.connection() as conn:
        stmt = select(book_table).where(book_table.c.author == 'Ebara Koji')
        print(stmt)
        rows = await conn.fetch_all(stmt)
        pprint([dict(row) for row in rows])


if __name__ == '__main__':
    asyncio.run(main())
