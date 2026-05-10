from pathlib import Path
file_path = Path("D:/learning of ai application development/python/first week/test.txt")
with file_path.open("w", encoding="utf-8") as f:
    f.writelines(["hello world\n", "hello python\n", "hello shr\n"])
with file_path.open("r", encoding="utf-8") as f:
    content = f.read()
    print(content)
def count_words(str):
    new_lst = str.split()
    count_result = {}
    for s in new_lst:
        count_result[s] = count_result.get(s, 0) + 1
    return count_result
lst_result = count_words(content)
for k,v in lst_result.items():
    print(f"{k}:{v}")
file_path_test = Path("D:/learning of ai application development/python/first week/exercise5.8.py")
print(file_path_test.exists())
line_count = len(content.split('\n'))
print(f'文件行数：{line_count - 1}')
