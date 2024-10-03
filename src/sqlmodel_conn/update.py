import asyncio

from create_table import Hero, engine
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def main():
    async with AsyncSession(engine) as session:
        stmt = select(Hero).where(Hero.name == 'Spider-Boy')
        hero = (await session.exec(stmt)).one()
        print(hero)
        hero.age = 16
        session.add(hero)
        await session.commit()
        await session.refresh(hero)
        print(hero)


if __name__ == '__main__':
    asyncio.run(main())
