from math import pi, sqrt
from abc import ABC, abstractmethod

# =================================
# Base Shape Class (Abstract Class)
# =================================

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# ====================
# Circle Subclass
# ====================
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


# ====================
# Square Subclass
# ====================
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# ====================
# Triangle Subclass
# ====================
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# ====================
# Testing the Classes
# ====================
def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            else:
                print("Value must be positive.")
        except ValueError:
            print("Invalid number. Try again.")

print("Choose a shape: circle / square / triangle")

shape_type = ""
while shape_type not in ["circle", "square", "triangle"]:
    shape_type = input("Enter shape: ").strip().lower()
    if shape_type not in ["circle", "square", "triangle"]:
        print("Invalid shape. Try again.")

if shape_type == "circle":
    r = get_positive_float("Enter radius: ")
    shape = Circle(r)

elif shape_type == "square":
    s = get_positive_float("Enter side length: ")
    shape = Square(s)

elif shape_type == "triangle":
    while True:
        a = get_positive_float("Enter side a: ")
        b = get_positive_float("Enter side b: ")
        c = get_positive_float("Enter side c: ")
        if a + b > c and a + c > b and b + c > a:
            shape = Triangle(a, b, c)
            break
        else:
            print("Invalid triangle sides. Try again.")

print("\n--- Shape Info ---")
print(f"Area     : {shape.area():.2f}")
print(f"Perimeter: {shape.perimeter():.2f}")