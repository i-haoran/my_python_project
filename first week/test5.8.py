lst_result = []
for i in range(1, 6):
    num = int(input(f"请输入第{i}个整数："))  # 输入时直接转整数
    lst_result.append(num)

num_positive = 0
num_negative = 0
num_zero = 0

for v in lst_result:
    if v > 0:
        num_positive += 1
    elif v < 0:
        num_negative += 1
    else:
        num_zero += 1

max_num = lst_result[0]
min_num = lst_result[0]
for v in lst_result:
    if v > max_num:
        max_num = v
    if v < min_num:
        min_num = v

print("统计结果：")
print(f"正数个数：{num_positive}")
print(f"负数个数：{num_negative}")
print(f"零的个数：{num_zero}")
print(f"最大值：{max_num}")
print(f"最小值：{min_num}")