# ====================================
#  Celsius to Fahrenheit Converter
# ====================================

while True:
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
        break

    except ValueError:
        print("Error: Please enter a valid number.")
