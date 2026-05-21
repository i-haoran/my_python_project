"""
数据分析：读取 weather_report.csv 并分析
"""

import pandas as pd

df = pd.read_csv("weather_report.csv", encoding="utf-8-sig")
print("原始数据：")
print(df.to_string(index=False))

print("\n--- 统计信息 ---")
print(f"共查询 {len(df)} 个城市")
print(f"成功: {(df['天气'] != '失败').sum()}")
print(f"失败: {(df['天气'] == '失败').sum()}")

# 按天气状况分组
if "温度" in df.columns:
    df["温度"] = pd.to_numeric(df["温度"], errors="coerce")
    print(f"\n平均温度: {df['温度'].mean():.1f}°C")
    print(f"最高温度: {df['温度'].max():.1f}°C")
    print(f"最低温度: {df['温度'].min():.1f}°C")
