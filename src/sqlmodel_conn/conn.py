import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Field, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    pages: int
    author: str


# sync url 'postgresql://postgres:pg_secret@localhost:5432/postgres' needs psycopg2, not psycopg3!
engine = create_async_engine(
    'postgresql+asyncpg://postgres:pg_secret@localhost:5432/postgres'
)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(
            SQLModel.metadata.create_all,
            # checkfirst=False,  # By default, checkfirst=True and doesn't recreate existing table
        )

    async with AsyncSession(engine) as session:
        stmt = select(Book).where(Book.id == 1)
        book = (await session.exec(stmt)).first()
        print(book.title)
        await session.commit()


if __name__ == '__main__':
    asyncio.run(main())
