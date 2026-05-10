raw_data = "101,3.14159,True,hello,42,2.718,False,world,101,0"
processed_data = []
raw_data_list = raw_data.split(',')
for item in raw_data_list:
    # 转换正整数
    if item.isdigit():
        processed_data.append(int(item))
    # 转换正小数
    elif item.replace('.', '', 1).isdigit() and item.count('.') <= 1:
        processed_data.append(float(item))
    # 转换负数
    elif item.startswith('-'):
        if item[1:].isdigit():
            processed_data.append(int(item))
        elif item[1:].replace('.', '', 1).isdigit() and item.count('.') <= 1:
            processed_data.append(float(item))
    elif item == "True":
        processed_data.append(True)
    elif item == "False":
        processed_data.append(False)
    else:
        processed_data.append(item)
sum_result = 0
str_set = set()
flag = False
result_float = []
for item in processed_data:
    if type(item) == int:
        sum_result += item
    elif type(item) == float:
        result_float.append(round(item, 2))
    elif type(item) == str:
        str_set.add(item)
    elif item == True:
        flag = True
print("---数据处理报告---")
print(f"所有的整数和为：{sum_result}")
print("处理后的浮点数为：", end=' ')
print(*result_float, sep=' ', end='\n')
print("发现的唯一字符串：", end=' ')
print(*str_set, sep=' ', end='\n')
print(f"数据中包含True值吗：{flag}")