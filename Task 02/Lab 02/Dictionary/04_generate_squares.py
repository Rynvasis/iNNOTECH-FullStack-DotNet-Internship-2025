#================================================== 
# Generate Dictionary of Numbers and Their Squares
#==================================================

while True:
    try:
        n = int(input("Enter a positive number: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


squares_dict = {}
for i in range(1, n + 1):
    squares_dict[i] = i ** 2

print("\nDictionary of squares:")
print(squares_dict)