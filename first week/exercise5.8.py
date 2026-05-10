def calc_average(scores):
    """
    计算每个学生的平均成绩
    使用sum求和
    round进行四舍五入取前两位小数
    """
    return round(sum(scores) / len(scores), 2)
def get_grade_level(avg):
    """
    计算每个学生的平均成绩的等级：
    >= 90: 'A' | 80-89: 'B' | 70-79: 'C' | 60-69: 'D' | < 60: 'F'
    """
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
def process_students(students):
    """
    处理学生数据
    用map给每个学生添加average和grade字段
    用filter筛选出等级不是'F'的学生
    用sorted按平均分降序排序
    """
    new_students = list(map(lambda s: {**s,
                                       "average": calc_average(s["scores"]),
                                       "grade": get_grade_level(calc_average(s["scores"]))},
                            students))
    not_f_students = list(filter(lambda s:s["grade"] != 'F', new_students))
    final_students = sorted(not_f_students, key=lambda s:s["average"], reverse=True)
    return final_students
students = [
    {"name": "张三", "scores": [85, 90, 78]},
    {"name": "李四", "scores": [92, 88, 95]},
    {"name": "王五", "scores": [78, 82, 80]},
    {"name": "赵六", "scores": [95, 98, 92]},
    {"name": "孙七", "scores": [88, 90, 85]},
    {"name": "周八", "scores": [55, 58, 52]}
]
result = process_students(students)
for item in result:
    print(f"{item['name']} - {item['scores']} - {item['average']} - {item['grade']}")