
# ====================
#  Volume of a Sphere
# ====================
import math

while True:
    try:
        radius = float(input("Enter the radius of the sphere: "))
        if radius < 0:
            print("Radius cannot be negative. Please enter a positive number.")
            continue

        volume = (4 / 3) * math.pi * radius ** 3
        print(f"The volume of the sphere with radius {radius:.2f} is {volume:.2f}.")
        break

    except ValueError:
        print("Error: Please enter a valid number.")
