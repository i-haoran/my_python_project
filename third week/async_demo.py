import asyncio
import httpx
from aiohttp import web, ClientSession


# ============================================================
# 1. async/await 基础
# ============================================================
async def mock_task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} 完成"


# ============================================================
# 2. 并发执行 + Semaphore 限流 + async with
# ============================================================
sem = asyncio.Semaphore(3)


async def fetch_one(client, url, i):
    async with sem:
        print(f"  [{i}] 开始: {url}")
        resp = await client.get(url, timeout=5)
        data = resp.json()
        print(f"  [{i}] 完成: 状态码 {resp.status_code}")
        return data


async def demo_concurrent():
    print("\n=== 并发请求（最多3个同时） ===")
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/get",
        "https://httpbin.org/get",
        "https://httpbin.org/get",
    ]
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one(client, url, i) for i, url in enumerate(urls)]
        results = await asyncio.gather(*tasks)
        print(f"共完成 {len(results)} 个请求")


# ============================================================
# 3. WebSocket 服务端
# ============================================================
async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("  [WS] 客户端已连接")
    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            print(f"  [WS] 收到: {msg.data}")
            await ws.send_str(f"回应: {msg.data}")
        elif msg.type == web.WSMsgType.CLOSE:
            break
    print("  [WS] 客户端断开")
    return ws


# ============================================================
# 4. WebSocket 客户端
# ============================================================
async def demo_websocket():
    print("\n=== WebSocket 通信 ===")

    # 启动服务端
    app = web.Application()
    app.router.add_get("/ws", ws_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8765)
    await site.start()
    print("  [WS] 服务端已启动: ws://localhost:8765/ws")

    # 连接客户端
    async with ClientSession() as session:
        async with session.ws_connect("ws://localhost:8765/ws") as ws:
            for msg in ["你好", "hello", "停止"]:
                await ws.send_str(msg)
                resp = await ws.receive()
                print(f"  [WS] 客户端收到: {resp.data}")
                if msg == "停止":
                    break

    await runner.cleanup()


# ============================================================
# 主函数
# ============================================================
async def main():
    print("Async 综合演示")
    print("=" * 50)

    # 基础
    result = await mock_task("任务1", 0.5)
    print(f"基础 await: {result}")

    # 并发
    await demo_concurrent()

    # WebSocket
    await demo_websocket()

    print("\n" + "=" * 50)
    print("全部完成")


asyncio.run(main())
