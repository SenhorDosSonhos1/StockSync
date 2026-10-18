import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.mark.anyio
async def test_health_check():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url='http://test'
    ) as ac:
        response = await ac.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'Hello, World!'}
