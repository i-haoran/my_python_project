class Student:
    school_name = "清华大学"

    # slots优化内存
    __slots__ = ('_no', '_name', '_age', '_scores')

    def __init__(self, no: str, name: str, age: int, scores: list[float] = None):

        # 参数校验
        if age < 6 or age > 25:
            raise ValueError("年龄必须在6到25岁之间")
        if not no or len(no) < 3:
            raise ValueError("学号不能为空且长度大于等于3")
        if not name:
            raise ValueError("姓名不能为空")

        # 列表传参的设置
        if scores is None:
            scores = []
        for s in scores:
            if s < 0 or s > 100:
                raise ValueError("成绩必须在0到100之间")

        self._no = no
        self._name = name
        self._age = age
        self._scores = scores

    # 创建内容的可读
    @property
    def no(self) -> str:
        return self._no

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def scores(self) -> list[float]:
        return self._scores

    # 附加属性grade
    @property
    def grade(self) -> int:
        return self._age - 6

    # 添加成绩方法
    def add_score(self, score: float) -> None:
        if score < 0 or score > 100:
            raise ValueError("成绩必须在0到100之间")
        self._scores.append(score)

    # 计算平均成绩
    def get_average(self) -> float:
        if not self._scores:
            return 0.0
        return round((sum(self._scores) / len(self._scores)), 2)

    # 获取最高分
    def get_max(self) -> float:
        if not self._scores:
            raise ValueError("列表为空，无法返回最大值")
        return max(self._scores)

    # 获取最低分
    def get_min(self) -> float:
        if not self._scores:
            raise ValueError("列表为空，无法返回最小值")
        return min(self._scores)

    # 工厂方法批量添加学生
    # 通过字典添加
    @classmethod
    def from_dict(cls,data: dict):
        return cls(
            no = data['no'],
            name = data['name'],
            age = data['age'],
            scores = data.get('scores', [])
        )

    # 通过姓名添加学生
    @classmethod
    def create_by_name(cls, name, age):
        import time
        auto_no = f"S{int(time.time())}"
        return cls(
            no = auto_no,
            name = name,
            age = age
        )

    # 开始测试代码
if __name__ == "__main__":

    # 基本功能
    s1 = Student("S001", "张三", 18, [85, 90, 78])
    print(f"学生: {s1.name}, {s1.age}岁, {s1.grade}年级")
    print(f"平均分: {s1.get_average()}")
    print(f"最高分: {s1.get_max()}, 最低分: {s1.get_min()}")

    # 添加成绩
    s1.add_score(95)
    print(f"添加后平均分: {s1.get_average():.2f}")

    # 工厂方法
    s2 = Student.from_dict({'no': 'S002', 'name': '李四', 'age': 19, 'scores': [88, 92]})
    s3 = Student.create_by_name("王五", 20)
    print(f"工厂方法创建: {s3.no}, {s3.name}")

    print(Student.school_name)