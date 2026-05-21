# Async 异步编程笔记

## 一、核心概念

| 概念 | 说明 |
|------|------|
| `async def` | 定义异步函数（协程），调用时不执行，返回协程对象 |
| `await` | 等待异步操作完成，同时让出控制权给事件循环 |
| `asyncio.run(main())` | 创建事件循环，运行主协程直到结束 |

```python
async def fetch_data():
    await asyncio.sleep(1)
    return 42

result = asyncio.run(fetch_data())
```

**本质**：单线程并发（非并行）。IO 等待时切到其他任务，CPU 计算时不切。

---

## 二、并发执行

### asyncio.gather — 多个任务同时跑

```python
async def main():
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
```

总耗时 ≈ 最慢的那个任务，不排队。

### asyncio.Semaphore — 限制并发数

```python
sem = asyncio.Semaphore(3)

async def safe_fetch(url):
    async with sem:  # 超过3个就排队
        return await client.get(url)
```

---

## 三、HTTP 请求

### httpx（推荐，简洁）

```python
import httpx, asyncio

async def main():
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get("https://api.github.com")
        return resp.json()

asyncio.run(main())
```

### aiohttp（需要 WebSocket 时用）

```python
import aiohttp, asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://example.com") as resp:
            text = await resp.text()
```

| | httpx | aiohttp |
|---|---|---|
| API 风格 | requests 风格，简洁 | 偏底层 |
| WebSocket | ❌ 不支持 | ✅ 原生支持 |
| 性能 | 稍低 | 更高 |
| 适用 | 调 API，批量请求 | 爬虫、WebSocket、代理 |

---

## 四、WebSocket

### 服务端

```python
from aiohttp import web

async def handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            await ws.send_str(f"回复: {msg.data}")
    return ws

app = web.Application()
app.router.add_get('/ws', handler)
web.run_app(app, port=8080)
```

### 客户端

```python
async with aiohttp.ClientSession() as session:
    async with session.ws_connect("ws://host:8080/ws") as ws:
        await ws.send_str("你好")
        async for msg in ws:
            print(msg.data)
```

### 地址写法

| 写法 | 用途 |
|------|------|
| `ws://localhost:8080/ws` | 本地开发 |
| `ws://192.168.1.100:8080/ws` | 局域网 |
| `wss://example.com/ws` | 线上（需 SSL） |

---

## 五、异步上下文管理器

```python
# 使用（无需自己实现）
async with httpx.AsyncClient() as client:
    resp = await client.get(url)
# 退出时自动关闭连接池
```

**必须用 `async with` 的场景**：httpx 客户端、aiohttp session、WebSocket、异步文件、异步锁、数据库连接。

---

## 六、关键区别

| | 同步 | 异步 |
|---|---|---|
| 等待结果 | `time.sleep(1)` | `await asyncio.sleep(1)` |
| HTTP | `requests.get(url)` | `await client.get(url)` |
| 文件 | `open()` | `await aiofiles.open()` |
| 上下文 | `with` | `async with` |
| 迭代 | `for x in items` | `async for x in items` |
| 入口 | `func()` | `asyncio.run(main())` |

```python
# 不能在普通函数里 await
def foo():
    await bar()  # ❌ SyntaxError

# 异步函数里可以调普通函数
async def foo():
    bar()  # ✅
```

---

## 七、什么时候用 async

| 场景 | 推荐 | 原因 |
|------|------|------|
| 调外部 API | ✅ async | IO 等待多，并发收益大 |
| 读写文件 | ✅ async | 磁盘 IO 可重叠 |
| 本地计算 | ❌ sync | CPU 计算不释放事件循环 |
| 数据库查询 | ✅ async | 等待 DB 响应 |
| 简单脚本 | ❌ sync | 一个请求没必要 |

**一句话**：有大量 IO 等待时用 async，只有 CPU 计算时用 sync。
