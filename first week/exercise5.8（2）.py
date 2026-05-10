evens_lst = [x for x in range(1,101) if x%2 == 0]
print(evens_lst)
my_str = "hello"
up_str = [s.upper() for s in my_str]
print(''.join(up_str))
lst = [1,-2,3,-4,5]
new_lst = [x*3 for x in lst if x%2 == 0]
print(new_lst)
new_up_str = my_str.upper()
print(''.join(new_up_str))