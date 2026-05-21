"""
项目1：多城市天气聚合器
功能：并发查询多个城市天气，保存到 CSV，用 pandas 分析
技术：httpx + asyncio + pandas + Semaphore 限流
"""

import asyncio
import json
import pandas as pd
import httpx

API_KEY = "SGiJMqsJ-UAWcPLcR"
CITIES = ["北京", "上海", "广州", "深圳", "杭州", "南京", "成都", "盐城"]
sem = asyncio.Semaphore(3)


async def fetch_one(client, city):
    async with sem:
        try:
            resp = await client.get(
                "https://api.seniverse.com/v3/weather/now.json",
                params={
                    "key": "SGiJMqsJ-UAWcPLcR",
                    "location": city,
                    "language": "zh-Hans",
                    "unit": "c",
                },
                timeout=5,
            )
            resp.raise_for_status()
            data = resp.json()["results"][0]
            return {
                "城市": data["location"]["name"],
                "天气": data["now"]["text"],
                "温度": data["now"]["temperature"],
                "湿度": data["now"].get("humidity", "N/A"),
            }
        except Exception as e:
            return {"城市": city, "天气": "失败", "温度": str(e), "湿度": ""}


async def main():
    print("正在查询多城市天气...")
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one(client, c) for c in CITIES]
        results = await asyncio.gather(*tasks)

    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    df.to_csv("weather_report.csv", index=False, encoding="utf-8-sig")
    print(f"\n已保存到 weather_report.csv")


if __name__ == "__main__":
    asyncio.run(main())
