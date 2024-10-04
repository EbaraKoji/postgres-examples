import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, Relationship, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class HeroTeamLink(SQLModel, table=True):
    team_id: int | None = Field(
        default=None, foreign_key='team.id', primary_key=True
    )
    hero_id: int | None = Field(
        default=None, foreign_key='hero.id', primary_key=True
    )

    is_training: bool = False
    team: 'Team' = Relationship(back_populates='hero_links')
    hero: 'Hero' = Relationship(back_populates='team_links')


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    hero_links: list[HeroTeamLink] = Relationship(back_populates='team')


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

    team_links: list[HeroTeamLink] = Relationship(back_populates='hero')


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
        )
        hero_rusty_man = Hero(
            name='Rusty-Man',
            secret_name='Tommy Sharp',
            age=48,
        )
        hero_spider_boy = Hero(
            name='Spider-Boy',
            secret_name='Pedro Parqueador',
        )
        deadpond_team_z_link = HeroTeamLink(
            team=team_z_force, hero=hero_deadpond
        )
        deadpond_preventers_link = HeroTeamLink(
            team=team_preventers, hero=hero_deadpond, is_training=True
        )
        spider_boy_preventers_link = HeroTeamLink(
            team=team_preventers, hero=hero_spider_boy, is_training=True
        )
        rusty_man_preventers_link = HeroTeamLink(
            team=team_preventers, hero=hero_rusty_man
        )

        session.add(deadpond_team_z_link)
        session.add(deadpond_preventers_link)
        session.add(spider_boy_preventers_link)
        session.add(rusty_man_preventers_link)

        stmt = select(HeroTeamLink).join(Team).join(Hero)
        hero_links = (await session.exec(stmt)).all()

        for link in hero_links:
            print(
                'team: ',
                link.team.name,
                'hero: ',
                link.hero.name,
                'is_training: ',
                link.is_training,
            )


if __name__ == '__main__':
    asyncio.run(main())
