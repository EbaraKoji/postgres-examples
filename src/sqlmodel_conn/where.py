import asyncio
from pprint import pprint

from create_table import Hero, engine
from sqlmodel import or_, select, col
from sqlmodel.ext.asyncio.session import AsyncSession


async def main():
    async with AsyncSession(engine) as session:
        stmt = select(Hero).where(or_(col(Hero.age) <= 35, col(Hero.age) > 90))
        heros = (await session.exec(stmt)).all()
        print('selecting heros')
        pprint(heros)
        await session.commit()


if __name__ == '__main__':
    asyncio.run(main())
