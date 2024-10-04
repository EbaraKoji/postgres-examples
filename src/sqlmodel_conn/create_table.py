import asyncio
from pprint import pprint

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, Relationship, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list['Hero'] = Relationship(
        back_populates='team',
        cascade_delete=True,
        sa_relationship_kwargs={'lazy': 'selectin'},  # async eager load
    )


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(
        default=None, foreign_key='team.id', ondelete='CASCADE'
    )
    team: Team | None = Relationship(back_populates='heroes')


url = 'postgresql+asyncpg://postgres:pg_secret@localhost:5432/postgres'
engine = create_async_engine(url, echo=False)


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

        heroes = [
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

        session.add_all(heroes)
        await session.commit()

        for hero in heroes:
            await session.refresh(hero)
        pprint(heroes)

        await session.refresh(team_preventers)
        stmt = select(Hero).where(Hero.team_id == team_preventers.id)
        hero_preventers = (await session.exec(stmt)).first()
        pprint(hero_preventers)
        await session.commit()

        for hero in heroes:
            await session.refresh(hero)
        await session.refresh(team_preventers)
        assert len(team_preventers.heroes) == 1
        pprint(heroes[1])
        team_preventers.heroes.append(heroes[1])
        session.add(team_preventers)

        await session.refresh(heroes[1])
        assert len(team_preventers.heroes) == 2
        pprint(heroes[1])

        for hero in heroes:
            await session.refresh(hero)
        await session.refresh(team_z_force)
        team_z_force_id = team_z_force.id
        stmt = select(Hero).where(Hero.team_id == team_z_force_id)
        z_force_heroes = (await session.exec(stmt)).all()
        pprint(z_force_heroes)
        await session.delete(team_z_force)

        z_force_heroes = (await session.exec(stmt)).all()
        pprint(z_force_heroes)


if __name__ == '__main__':
    asyncio.run(main())
