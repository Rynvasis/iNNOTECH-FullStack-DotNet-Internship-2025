# ================================
#  Accept Numbers Until Negative 
# ================================

while True:
    try:
        num = int(input("Enter a number (negative to stop): "))
        if num < 0:
            print("Negative number entered. Program stopped.")
            break
        print(f"You entered: {num} to stop enter negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
