# 多城市天气聚合器

并发查询多个城市天气，Semaphore 限流，结果存 CSV 并用 pandas 分析。

## 使用

```bash
pip install -r requirements.txt
python weather_aggregator.py
python analyze.py
```

## 技术栈

- httpx (异步 HTTP)
- asyncio + Semaphore (并发限流)
- pandas (数据分析)
