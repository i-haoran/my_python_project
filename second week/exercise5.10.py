from abc import ABC, abstractmethod


class Shape(ABC):

    # 定义实例类型color
    def __init__(self, color: str):
        self.color = color

    # 定义抽象方法
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def info(self) -> str:
        return f"{self.__class__.__name__}(color = {self.color})"


# 创建子类继承父类
class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius

    # 继承父类方法
    def area(self) -> float:
        return round((3.14 * self.radius ** 2), 2)

    def perimeter(self) -> float:
        return round((3.14 * self.radius * 2), 2)


class Rectangle(Shape):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return round((self.width * self.height), 2)

    def perimeter(self) -> float:
        return round((self.width * 2 + self.height * 2), 2)


# 定义多态
# 接收有area方法的对象
def print_shape_info(obj) -> None:
    print(f"面积大小是：{obj.area()}")


# 接收图形列表，返回总面积
def total_area(items: list[Shape]) -> float:
    result = 0
    for i in items:
        result += i.area()
    return round(result, 2)


# 筛选面积大于指定值的图形
def filter_by_area(items: list[Shape], temp: float) -> list:
    lst = []
    for i in items:
        if i.area() > temp:
            lst.append(i)
    return lst


# 5. 测试代码
if __name__ == "__main__":
    # 创建图形对象
    circle = Circle("红色", 3)
    rect = Rectangle("蓝色", 4, 5)

    # 多态调用
    print_shape_info(circle)  # Circle(color=红色) - 面积:28.27 周长:18.85
    print_shape_info(rect)  # Rectangle(color=蓝色) - 面积:20.00 周长:18.00

    # 类型验证
    print(f"circle是Circle的实例: {isinstance(circle, Circle)}")
    print(f"circle是Shape的实例: {isinstance(circle, Shape)}")
    print(f"Circle是Shape的子类: {issubclass(Circle, Shape)}")

    # 计算总面积
    shapes = [circle, rect, Circle("黄色", 5)]
    print(f"总面积: {total_area(shapes)}")

    # 筛选图形
    large_shapes = filter_by_area(shapes, 30)
    print(f"面积大于30的图形: {[s.info() for s in large_shapes]}")
