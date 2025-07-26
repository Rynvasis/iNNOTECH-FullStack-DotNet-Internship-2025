# ==========================
#  Circle Area Calculator
# ==========================
import math

while True:
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Please enter a positive number.")
        else:
            area = math.pi * radius ** 2
            print(f"The area of the circle with radius {radius} is {area:.2f}")
            break
    except ValueError:
        print("Error: Please enter a valid number.")