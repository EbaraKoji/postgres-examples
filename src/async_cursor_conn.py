import asyncio

import psycopg


async def main():
    async with await psycopg.AsyncConnection.connect(
        host='localhost',
        port=5432,
        dbname='postgres',
        user='postgres',
        password='pg_secret',
        cursor_factory=psycopg.AsyncClientCursor,  # https://stackoverflow.com/questions/78410960/psycopg3-mogrify-attributeerror-connection-object-has-no-attribute-mogrify
    ) as aconn:
        async with aconn.cursor() as acur:
            await acur.execute('DROP TABLE IF EXISTS book;')

            await acur.execute("""CREATE TABLE IF NOT EXISTS book (
                id INT PRIMARY KEY,
                title VARCHAR(255),
                pages INT,
                author VARCHAR(255)
            );
            """)

            await acur.execute("""INSERT INTO book (id, title, pages, author) VALUES
            (1, 'Python in 7 days', 328, 'Ebara Koji'),
            (2, 'Machine Learning in 1 month', 691, 'Tensor John'),
            (3, 'FastAPI in 7 days', 125, 'Ebara Koji'),
            (4, 'Next.js in 7 days', 287, 'Ebara Koji'),
            (5, 'Rust in 14 days', 350, 'Crub Red');
            """)

            await acur.execute('SELECT * FROM book;')
            print(await acur.fetchall())

            await acur.execute(
                """SELECT * FROM book WHERE author = 'Ebara Koji';"""
            )
            print(await acur.fetchall())

            sql = acur.mogrify(
                """SELECT * FROM book WHERE starts_with(title, %s) AND pages > %s;""",
                ('Next.js', 200),
            )
            print(sql)

            await acur.execute(sql)
            print(await acur.fetchall())


if __name__ == '__main__':
    asyncio.run(main())
