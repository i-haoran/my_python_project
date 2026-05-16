from aiohttp import web


async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            await ws.send_str(f"Echo: {msg.data}")
    return ws


app = web.Application()
app.router.add_get("/ws", ws_handler)
web.run_app(app, port=8080)
