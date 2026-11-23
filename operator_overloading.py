"""OOP exercises: Operator overloading (problems 1-6)."""
import math


# 1. Complex numbers: + and -
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"


# 2. Person: > compares by age
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age}, {self.gender!r})"


# 3. Vector: * is the dot product
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# 4. Circle: all six comparisons, by radius
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __repr__(self):
        return f"Circle({self.radius})"


# 5. Point2D: comparisons by distance from the origin, sqrt(x^2 + y^2)
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __eq__(self, other):
        return math.isclose(self.distance(), other.distance())

    def __ne__(self, other):
        return not self == other

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"


# 6. Matrix: * is matrix multiplication
class Matrix:
    def __init__(self, rows):
        self.rows = rows  # list of lists

    def __mul__(self, other):
        n, m = len(self.rows), len(self.rows[0])
        if m != len(other.rows):
            raise ValueError("Incompatible dimensions")
        p = len(other.rows[0])
        result = [[0] * p for _ in range(n)]
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    result[i][j] += self.rows[i][k] * other.rows[k][j]
        return Matrix(result)

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return f"Matrix({self.rows})"


if __name__ == "__main__":
    # 1
    assert Complex(1, 2) + Complex(3, 4) == Complex(4, 6)
    assert Complex(5, 5) - Complex(2, 7) == Complex(3, -2)
    # 2
    assert Person("A", 30, "F") > Person("B", 20, "M")
    assert not (Person("A", 20, "F") > Person("B", 30, "M"))
    # 3
    assert Vector(1, 2, 3) * Vector(4, 5, 6) == 32
    assert repr(Vector(1, 2, 3)) == "Vector(1, 2, 3)"
    assert Vector(1, 2, 3) + Vector(1, 1, 1) == Vector(2, 3, 4)
    # 4
    a, b = Circle(1), Circle(2)
    assert a < b and b > a and a != b and a <= b and b >= a and a == Circle(1)
    # 5
    p, q = Point2D(3, 4), Point2D(1, 1)  # distances 5 and sqrt(2)
    assert q < p and p > q and p != q and q <= p and p >= q
    assert Point2D(3, 4) == Point2D(5, 0)
    # 6
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    assert m1 * m2 == Matrix([[19, 22], [43, 50]])
    assert Matrix([[1, 2, 3]]) * Matrix([[1], [2], [3]]) == Matrix([[14]])
    print("operator_overloading: all tests passed")
