import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str = Field(index=True)
    age: int | None = None


my_hero = Hero(name='Spider-Boy', secret_name='Pedro Parqueador')

url = 'postgresql+asyncpg://postgres:pg_secret@localhost:5432/postgres'
engine = create_async_engine(url, echo=True)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(main())
