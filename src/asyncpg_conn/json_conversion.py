import asyncio
import json

from conn import get_async_db


async def main():
    async with get_async_db() as conn:
        await conn.set_type_codec(
            'json',
            encoder=json.dumps,
            decoder=json.loads,
            schema='pg_catalog'
        )

        data = {'foo': 'bar', 'spam': 1}
        res: dict = await conn.fetchval('SELECT $1::json', data)
        print(res)

if __name__ == '__main__':
    asyncio.run(main())