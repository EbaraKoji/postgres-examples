import asyncio
from pprint import pprint

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, Relationship, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list['Hero'] = Relationship(back_populates='team')


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key='team.id')
    team: Team | None = Relationship(back_populates='heroes')


url = 'postgresql+asyncpg://postgres:pg_secret@localhost:5432/postgres'
engine = create_async_engine(url, echo=True)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

    async with AsyncSession(engine) as session:
        team_preventers = Team(name='Preventers', headquarters='Sharp Tower')
        team_z_force = Team(
            name='Z-Force', headquarters="Sister Margaret's Bar"
        )
        session.add(team_preventers)
        session.add(team_z_force)
        await session.commit()

        await session.refresh(team_preventers)
        await session.refresh(team_z_force)

        heros = [
            Hero(
                name='Deadpond',
                secret_name='Dive Wilson',
                team_id=team_z_force.id,
            ),
            Hero(name='Spider-Boy', secret_name='Pedro Parqueador'),
            Hero(
                name='Rusty-Man',
                secret_name='Tommy Sharp',
                age=48,
                team_id=team_preventers.id,
            ),
            Hero(name='Tarantula', secret_name='Natalia Roman-on', age=32),
            Hero(name='Black Lion', secret_name='Trevor Challa', age=35),
            Hero(name='Dr. Weird', secret_name='Steve Weird', age=36),
            Hero(
                name='Captain North America',
                secret_name='Esteban Rogelios',
                age=93,
            ),
        ]

        session.add_all(heros)
        await session.commit()

        for hero in heros:
            await session.refresh(hero)
        pprint(heros)

        await session.refresh(team_preventers)
        stmt = select(Hero).where(Hero.team_id == team_preventers.id)
        hero_preventers = (await session.exec(stmt)).first()
        pprint(hero_preventers)

        stmt = select(Hero, Team).join(Team, isouter=True)
        results = await session.exec(stmt)
        for hero, team in results:
            print('Hero:', hero.name, 'Team:', team.name if team else None)


if __name__ == '__main__':
    asyncio.run(main())
