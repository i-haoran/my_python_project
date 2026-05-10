from typing import Union
import math


class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("坐标必须是数字")  # ✅ 修正：TypeError
        self.x = x
        self.y = y

    def distance(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):  # ✅ 加上类型检查
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.distance() < other.distance()

    def __le__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.distance() <= other.distance()

    def __gt__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.distance() > other.distance()

    def __ge__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.distance() >= other.distance()

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        return self * scalar

    def __len__(self) -> int:
        return 2

    def __abs__(self) -> float:
        return self.distance()


if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(repr(v1))
    print(str(v2))

    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 > v2: {v1 > v2}")

    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")

    v4 = v1 * 2
    print(f"v1 * 2 = {v4}")

    v5 = 3 * v2
    print(f"3 * v2 = {v5}")

    print(f"len(v1) = {len(v1)}")
    print(f"|v1| = {abs(v1):.2f}")