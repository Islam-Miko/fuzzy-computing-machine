from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.configs.settings import get_settings

Settings = get_settings()


db_engine = create_async_engine(Settings.get_database_url())

SessionFactory = sessionmaker(
    db_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


async def get_session():
    session = SessionFactory()
    try:
        yield session
    finally:
        await session.close()
