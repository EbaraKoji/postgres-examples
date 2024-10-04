import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, Relationship, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession


class HeroTeamLink(SQLModel, table=True):
    team_id: int | None = Field(
        default=None, foreign_key='team.id', primary_key=True
    )
    hero_id: int | None = Field(
        default=None, foreign_key='hero.id', primary_key=True
    )


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list['Hero'] = Relationship(
        back_populates='teams',
        link_model=HeroTeamLink,
        sa_relationship_kwargs={'lazy': 'selectin'},
    )


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key='team.id')
    teams: list[Team] = Relationship(
        back_populates='heroes',
        link_model=HeroTeamLink,
        sa_relationship_kwargs={'lazy': 'selectin'},
    )


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

        hero_deadpond = Hero(
            name='Deadpond',
            secret_name='Dive Wilson',
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name='Rusty-Man',
            secret_name='Tommy Sharp',
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name='Spider-Boy',
            secret_name='Pedro Parqueador',
            teams=[team_preventers],
        )
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        await session.commit()

        await session.refresh(hero_deadpond)
        await session.refresh(hero_rusty_man)
        await session.refresh(hero_spider_boy)

        print('Deadpond:', hero_deadpond)
        print('Deadpond teams:', hero_deadpond.teams)
        print('Rusty-Man:', hero_rusty_man)
        print('Rusty-Man Teams:', hero_rusty_man.teams)
        print('Spider-Boy:', hero_spider_boy)
        print('Spider-Boy Teams:', hero_spider_boy.teams)


if __name__ == '__main__':
    asyncio.run(main())
