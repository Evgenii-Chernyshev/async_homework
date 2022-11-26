import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/sales', json={'item_id': 12, 'store_id': 11}) as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(main())