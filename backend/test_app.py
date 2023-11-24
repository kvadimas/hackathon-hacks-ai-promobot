import pytest
from httpx import AsyncClient
from fastapi import FastAPI

app = FastAPI(version="1.0")


@pytest.mark.anyio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
