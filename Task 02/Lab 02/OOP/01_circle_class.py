
# =============
# Circle class
# =============
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


# =================
# Testing the class
# =================

while True:
    try:
        r = float(input("Enter the radius of the circle: "))
        if r < 0:
            print("Radius cannot be negative.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")


my_circle = Circle(r)


print(f"\nCircle with radius {r}")
print(f"Area: {my_circle.get_area():.2f}")
print(f"Perimeter: {my_circle.get_perimeter():.2f}")
