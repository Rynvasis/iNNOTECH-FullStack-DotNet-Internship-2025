# ====================================
#  Print All Even Numbers from 1 to n
# ====================================

while True:
    try:
        n = int(input("Enter a positive integer n: "))
        if n <= 1:
            print("Please enter a number greater than 1.")
            continue

        print(f"Even numbers from 1 to {n}:")
        for i in range(2, n + 1, 2):
            print(i, end=" ")

        print()  
        break

    except ValueError:
        print("Error: Please enter a valid integer.")