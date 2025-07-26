# ===============================
#   Check if a Number is Prime
# ===============================

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 1:
            print(f"{num} is not a prime number.")
            break

        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
        break

    except ValueError:
        print("Error: Please enter a valid integer.")
