#================ 
# Square Number
#================

def square_number(num):
    return num * num


while True:
    try:
        user_input = input("Enter a number to square: ")
        number = float(user_input)
        break
    except ValueError:
        print("Please enter a valid number.")


result = square_number(number)
print(f"The square of {number} is: {result}")
