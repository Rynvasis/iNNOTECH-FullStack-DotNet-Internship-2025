# ====================================
#  Inches to Centimeters Converter
# ====================================

while True:
    try:
        inches = float(input("Enter length in inches: "))
        if inches < 0:
            print("Length cannot be negative. Please enter a positive value.")
            continue
        centimeters = inches * 2.54
        print(f"{inches:.2f} inches is equal to {centimeters:.2f} cm.")
        break
    except ValueError:
        print("Error: Please enter a valid number.")
