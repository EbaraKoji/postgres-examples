import asyncio

from conn import database, get_db


@database.transaction()
async def insert():
    async with database.connection() as conn:
        await conn.execute("""INSERT INTO book (id, title, pages, author) 
    VALUES(999, 'Python in 7 days', 328, 'Ebara Koji');
    """)
        await conn.execute("""INSERT INTO book (id, title, pages, author) 
    VALUES(1, 'Python in 7 days', 328, 'Ebara Koji');
    """)


@get_db(database)
async def main():
    try:
        await insert()
    except BaseException as e:
        print(f'Failed to execute query.\nError: {e}')
    async with database.connection() as conn:
        row = await conn.fetch_one('SELECT * from book WHERE id = 999;')
        print(row)  # None because insert() is rollbacked


if __name__ == '__main__':
    asyncio.run(main())
