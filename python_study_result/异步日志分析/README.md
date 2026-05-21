# 异步日志分析系统

多层生成器流水线处理日志文件，逐行读取、JSON 解析、级别筛选、聚合统计。

## 使用

```bash
python log_analyzer.py
```

## 流水线架构

```
read_log → parse_log → filter_level → aggregate → 结果
```

## 技术栈

- 生成器 (yield/yield from)
- 流水线模式
- JSON 处理
