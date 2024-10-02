import asyncio

from conn import get_async_db


async def main():
    async with get_async_db() as conn:
        tr = conn.transaction()
        await tr.start()
        try:
            await conn.execute("""INSERT INTO book (id, title, pages, author) 
VALUES(999, 'Python in 7 days', 328, 'Ebara Koji');
""")

            # Key (id)=(1) already exists.
            await conn.execute("""INSERT INTO book (id, title, pages, author) 
VALUES(1, 'Python in 7 days', 328, 'Ebara Koji');
""")
        except BaseException as e:
            print(f'Failed to execue query.\nError: {e}')
            await tr.rollback()
        else:
            await tr.commit()

        # with tr.rollback(), record of id 999 does not exist.
        row = await conn.fetchrow('SELECT * from book WHERE id = 999;')
        print(row)  # None


if __name__ == '__main__':
    asyncio.run(main())
