"""
项目2：WebSocket 实时通信
功能：aiohttp WebSocket 服务端，支持多客户端连接，实时收发消息
技术：aiohttp + WebSocket + async with
"""

from aiohttp import web

clients = set()


async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    clients.add(ws)
    print(f"[+] 新客户端连接, 当前在线: {len(clients)}")

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            print(f"[消息] {msg.data}")
            for c in clients:
                if c != ws and not c.closed:
                    await c.send_str(f"[{len(clients)}人在线] {msg.data}")
        elif msg.type == web.WSMsgType.ERROR:
            print(f"[错误] {ws.exception()}")

    clients.discard(ws)
    print(f"[-] 客户端断开, 当前在线: {len(clients)}")
    return ws


app = web.Application()
app.router.add_get("/ws", ws_handler)
print("WebSocket 服务端启动: ws://localhost:8080/ws")
web.run_app(app, port=8080)
