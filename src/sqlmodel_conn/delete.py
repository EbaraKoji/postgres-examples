import asyncio

from create_table import Hero, engine
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def main():
    async with AsyncSession(engine) as session:
        hero = Hero(name='Astral', secret_name='Will Smith', age=30)
        session.add(hero)
        await session.commit()

        db_hero = (
            await session.exec(select(Hero).where(Hero.name == 'Astral'))
        ).one()
        print(f'db_hero: {db_hero}')

        await session.delete(db_hero)
        await session.commit()
        
        db_hero = (
            await session.exec(select(Hero).where(Hero.name == 'Astral'))
        ).first()
        print(f'db_hero_after_delete: {db_hero}')

        await session.commit()


if __name__ == '__main__':
    asyncio.run(main())
