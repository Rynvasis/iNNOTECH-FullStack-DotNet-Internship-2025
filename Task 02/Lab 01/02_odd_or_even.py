# ==========================
#   Odd or Even Checker
# ==========================

while True:
    try:
        number = int(input("Enter an integer: "))
        if number & 1:
            print(f"{number} is odd.")
        else:
            print(f"{number} is even.")
        break
    except ValueError:
        print("Error: Please enter a valid integer.")