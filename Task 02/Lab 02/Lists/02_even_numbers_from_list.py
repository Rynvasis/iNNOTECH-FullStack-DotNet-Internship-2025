# ==============================
#  Filter Even Numbers from List
# ==============================

while True:
    user_input = input("Enter a list of integers separated by commas (e.g. 1,2,3,4): ").strip()
    try:
        numbers = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
        if not numbers:
            print("List cannot be empty. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Make sure all items are integers.")

even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers:", even_numbers)
