from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession)


async def init_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session
