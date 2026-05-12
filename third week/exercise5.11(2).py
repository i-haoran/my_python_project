from pathlib import Path

# 1. 设置文件路径
log_path = Path("D:/learning of ai application development/python/third week/my_log")


def read_log():
    """生成器：负责读取文件，每次吐出一行清洗过的数据"""
    # 增加 exists() 检查，防止文件不存在报错
    if not log_path.exists():
        print(f"错误：找不到文件 {log_path}")
        return

    with log_path.open("r", encoding="utf-8") as f:
        header = next(f, None)  # 读取并跳过表头
        if header:
            yield header.strip()  # 先把表头吐出来，方便后面解析列名

        for line in f:
            if line.strip():  # 过滤空行
                yield line.strip()


def parse_log():
    """解析器：将文本行转换为字典列表"""
    lst_results = []
    gen = read_log()

    try:
        # 1. 获取表头 (第一行)
        header_line = next(gen)
        # 修复：处理表头可能带空格的情况
        keys = [k.strip() for k in header_line.split(",")]

        # 2. 遍历剩余行
        for line in gen:
            values = [v.strip() for v in line.split(",")]

            # 修复：必须在循环内部创建新字典，否则所有列表项都会指向同一个内存地址
            record = {}

            # 使用 zip 自动对齐键和值，更加稳健
            for k, v in zip(keys, values):
                # 特殊处理：如果是金额，转为数字
                if k == "amount":
                    try:
                        record[k] = float(v)
                    except ValueError:
                        record[k] = 0.0
                else:
                    record[k] = v

            lst_results.append(record)

    except StopIteration:
        pass  # 文件为空或处理完毕

    return lst_results


def filter_purchase(data):
    """过滤器：只保留 action 为 'purchase' 的记录"""
    # 修复：不要在遍历列表时直接 pop，使用列表推导式更安全高效
    return [item for item in data if item.get("action") == "purchase"]


def aggregate_by_user(data):
    """聚合器：按用户统计"""
    users = {}

    for item in data:
        uid = item.get("user_id")
        if not uid:
            continue  # 防止空数据报错
        if uid not in users:
            users[uid] = {"count": 0, "total": 0.0, "last": ""}

        users[uid]["count"] += 1
        users[uid]["total"] += item.get("amount", 0)
        users[uid]["last"] = item.get("timestamp", "")

    # 计算平均值
    for uid in users:
        if users[uid]["count"] > 0:
            users[uid]["avg"] = users[uid]["total"] / users[uid]["count"]
        else:
            users[uid]["avg"] = 0

    return users


# ==========================================
# 测试函数部分
# ==========================================


def run_test():
    print("=" * 30)
    print("开始测试日志分析系统...")
    print("=" * 30)

    # 1. 测试读取与解析
    print("\n[步骤1] 解析原始数据...")
    raw_data = parse_log()
    if not raw_data:
        print("❌ 解析失败或文件为空，请检查路径。")
        return

    print(f"✅ 成功解析 {len(raw_data)} 条记录。")
    print("   第一条数据示例:", raw_data[0])

    # 2. 测试过滤
    print("\n[步骤2] 过滤非消费记录...")
    purchase_data = filter_purchase(raw_data)
    print(f"✅ 过滤后剩余 {len(purchase_data)} 条消费记录。")
    # 打印一条消费记录确认金额是否为数字
    if purchase_data:
        print("   消费数据示例:", purchase_data[0])
        print(f"   金额类型检查: {type(purchase_data[0]['amount'])}")

    # 3. 测试聚合
    print("\n[步骤3] 按用户聚合统计...")
    user_stats = aggregate_by_user(purchase_data)

    print(f"✅ 统计完成，共涉及 {len(user_stats)} 位用户。")
    print("-" * 30)
    print(
        f"{'用户ID':<10} | {'次数':<5} | {'总金额':<10} | {'平均值':<10} | {'最近时间':<20}"
    )
    print("-" * 30)

    # 格式化打印结果
    for uid, stats in user_stats.items():
        print(
            f"{uid:<10} | {stats['count']:<5} | {stats['total']:<10.2f} | {stats['avg']:<10.2f} | {stats['last']:<20}"
        )

    print("=" * 30)
    print("测试结束！")


# 运行入口
if __name__ == "__main__":
    run_test()
