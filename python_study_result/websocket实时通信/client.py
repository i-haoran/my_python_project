"""
WebSocket 客户端：连接服务端，发送消息，接收回复
"""

import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            print("已连接到服务器，输入消息发送，输入 /quit 退出")

            async def receive():
                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        print(f"\n{msg.data}")
                    elif msg.type == aiohttp.WSMsgType.CLOSED:
                        break

            asyncio.create_task(receive())
            loop = asyncio.get_event_loop()
            while True:
                text = await loop.run_in_executor(None, input, "> ")
                if text == "/quit":
                    break
                await ws.send_str(text)


asyncio.run(main())
