# ==========================
#  Sum of Three Integers
# ==========================

while True:
    try:
        numbers = []
        for i in range(3):
            num = int(input(f"Enter integer {i+1}: "))
            numbers.append(num)

        if len(set(numbers)) < 3:
            result = 0
        else:
            result = sum(numbers)

        print(f"The result is: {result}")
        break
    except ValueError:
        print("Error: Please enter valid integers.")