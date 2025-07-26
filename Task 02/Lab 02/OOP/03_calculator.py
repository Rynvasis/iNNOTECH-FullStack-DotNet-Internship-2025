# =================
# Calculator Class
# =================
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b


# =================
# Testing the class
# =================
calc = Calculator()

while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        break
    except ValueError:
        print("Error: Please enter valid numbers.")

print("Addition:", calc.add(x, y))
print("Subtraction:", calc.subtract(x, y))
print("Multiplication:", calc.multiply(x, y))
print("Division:", calc.divide(x, y))
