"""
项目3：异步日志分析系统
功能：多层生成器流水线处理日志文件，逐行读取、解析、筛选、聚合统计
技术：生成器 + yield from + 流水线模式
"""

import json
from collections import defaultdict


def read_log(filepath):
    """第一层：逐行读取日志"""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def parse_log(lines):
    """第二层：解析 JSON 格式日志行"""
    skipped = 0
    for line in lines:
        if not line:
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            skipped += 1
    if skipped:
        print(f"跳过 {skipped} 行无效格式")


def filter_level(parsed, min_level="WARNING"):
    """第三层：按日志级别筛选"""
    levels = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
    threshold = levels.get(min_level, 2)
    for record in parsed:
        if levels.get(record.get("level", "INFO"), 0) >= threshold:
            yield record


def aggregate(records):
    """第四层：聚合统计"""
    stats = defaultdict(lambda: {"count": 0, "messages": []})
    for r in records:
        level = r.get("level", "UNKNOWN")
        stats[level]["count"] += 1
        stats[level]["messages"].append(r.get("message", ""))
    yield dict(stats)


def pipeline(filepath, min_level="WARNING"):
    """完整流水线"""
    return next(aggregate(filter_level(parse_log(read_log(filepath)), min_level)), {})


if __name__ == "__main__":
    result = pipeline("sample.log", min_level="WARNING")
    print("聚合结果：")
    for level, info in result.items():
        print(f"  [{level}] {info['count']} 条")
        for msg in info["messages"][:3]:
            print(f"    → {msg}")
        if len(info["messages"]) > 3:
            print(f"    ... 还有 {len(info['messages']) - 3} 条")
