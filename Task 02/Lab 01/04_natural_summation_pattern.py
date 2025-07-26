# =====================================
#   Natural Numbers Summation Pattern
# ======================================

while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
            continue

        current_sum = 0
        for i in range(1, n + 1):
            current_sum += i
            expression = " + ".join(map(str, range(1, i + 1)))
            print(f"{expression} = {current_sum}")
        break

    except ValueError:
        print("Error: Please enter a valid integer.")
