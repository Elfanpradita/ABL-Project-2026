import httpx
import os

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

async def get_status():
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{API_URL}/status",
            headers={"x-api-key": API_KEY}
        )
        return res.json()