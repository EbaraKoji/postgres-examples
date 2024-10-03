import asyncio
from pprint import pprint

from create_table import Hero, engine
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

    heros = [
        Hero(name='Deadpond', secret_name='Dive Wilson'),
        Hero(name='Spider-Boy', secret_name='Pedro Parqueador'),
        Hero(name='Rusty-Man', secret_name='Tommy Sharp', age=48),
    ]

    async with AsyncSession(engine) as session:
        session.add_all(heros)
        await session.commit()
        stmt = select(Hero)
        db_heros = (await session.exec(stmt)).all()
        pprint(db_heros)
        await session.commit()


if __name__ == '__main__':
    asyncio.run(main())
