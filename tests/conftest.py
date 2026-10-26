import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import async_sessionmaker


@pytest.fixture
async def db() -> AsyncSession:  # type: ignore
    async with async_sessionmaker() as session:
        yield session
        await session.rollback()
