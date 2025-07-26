#===================
# Max Of Two Numbers
#===================

def get_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter valid numbers.")

max_value = get_max(a, b)
print(f"The largest of the two numbers is: {max_value}")
