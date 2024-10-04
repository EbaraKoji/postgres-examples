import asyncio
from pprint import pprint

from create_table import Hero, engine
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

    heroes = [
        Hero(name='Deadpond', secret_name='Dive Wilson'),
        Hero(name='Spider-Boy', secret_name='Pedro Parqueador'),
        Hero(name='Rusty-Man', secret_name='Tommy Sharp', age=48),
        Hero(name='Tarantula', secret_name='Natalia Roman-on', age=32),
        Hero(name='Black Lion', secret_name='Trevor Challa', age=35),
        Hero(name='Dr. Weird', secret_name='Steve Weird', age=36),
        Hero(
            name='Captain North America',
            secret_name='Esteban Rogelios',
            age=93,
        ),
    ]

    async with AsyncSession(engine) as session:
        print('before adding heroes')
        pprint(heroes)

        session.add_all(heroes)
        print('after adding heroes')
        pprint(heroes)

        await session.commit()
        print('after commiting heroes')
        pprint(heroes)

        for hero in heroes:
            await session.refresh(hero)
        print('after refreshing heroes')
        pprint(heroes)

        stmt = select(Hero)
        db_heroes = (await session.exec(stmt)).all()
        print('selecting heroes')
        pprint(db_heroes)
        await session.commit()
    print('after closing session')
    pprint(heroes)


if __name__ == '__main__':
    asyncio.run(main())
