# WebSocket 实时通信

基于 aiohttp 的 WebSocket 聊天服务端+客户端，支持多客户端实时广播消息。

## 使用

```bash
pip install -r requirements.txt
# 终端1：启动服务端
python server.py
# 终端2：启动客户端
python client.py
```

## 技术栈

- aiohttp (WebSocket 服务端+客户端)
- async/await (异步IO)
