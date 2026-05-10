my_str = "apple banana apple orange banana apple"
num_str = {}
words = my_str.split(' ')
for s in words:
    num_str[s] = num_str.get(s,0) + 1
for k,v in num_str.items():
    print(f"{k}出现{v}次")
lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
print("交集：", end='  ')
print(list(set(lst1) & set(lst2)))
print("并集：", end='  ')
print(list(set(lst1) | set(lst2)))
print("差集：", end='  ')
print(list(set(lst1) - set(lst2)))