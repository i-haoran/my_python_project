import aiohttp, asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('ws://localhost:8080/ws') as ws:
            await ws.send_str("Hello")
            async for msg in ws:
                print(msg.data)
                break

asyncio.run(main())