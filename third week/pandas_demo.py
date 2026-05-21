import pandas as pd

# ============================================================
# 1. 读 CSV
# ============================================================
df = pd.read_csv("sales.csv")
print("前5行:")
print(df.head())
print()

# ============================================================
# 2. 概览
# ============================================================
df.info()
print()
print(df.describe())
print()

# ============================================================
# 3. 筛选
# ============================================================
beijing = df[df["city"] == "北京"]
print(f"北京订单: {len(beijing)} 条")
print()

big_orders = df[df["amount"] > 1000]
print(f"大额订单(>1000): {len(big_orders)} 条")
print()

# ============================================================
# 4. 分组聚合
# ============================================================
print("各城市销售额:")
city_sales = df.groupby("city")["amount"].sum().sort_values(ascending=False)
print(city_sales)
print()

print("各品类销售额:")
cat_sales = df.groupby("category")["amount"].sum().sort_values(ascending=False)
print(cat_sales)
print()

print("各城市各品类销售额:")
city_cat = df.groupby(["city", "category"])["amount"].sum()
print(city_cat)
print()

# ============================================================
# 5. 新增列
# ============================================================
# 总价 = 单价 x 数量（但 amount 已经是总价了，所以算平均单价）
df["unit_price"] = (df["amount"] / df["quantity"]).round(2)
print("新增平均单价列:")
print(df[["product", "quantity", "amount", "unit_price"]].head())
df.to_csv("sales.csv", index=False, encoding="utf-8-sig")
print()

# ============================================================
# 6. 排序
# ============================================================
print("销售额前5的订单:")
top5 = df.sort_values("amount", ascending=False).head(5)
print(top5[["date", "city", "product", "amount"]])
print()

# ============================================================
# 7. 输出为代码中可以直接用的结构
# ============================================================
# 分组结果转回 DataFrame
city_sales_df = city_sales.reset_index()
city_sales_df.columns = ["城市", "销售额"]
print("分组结果转 DataFrame:")
print(city_sales_df)
# 导出为 CSV
city_sales_df.to_csv("分组结果.csv", index=False, encoding="utf-8-sig")
print()

# 转字典
print("转字典:")
print(city_sales_df.to_dict(orient="records"))
