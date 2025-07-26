# =========================
#  Detect Range of Integer
# =========================

ranges = [
    (0, 10, "Range 1"),
    (11, 20, "Range 2"),
    (21, 30, "Range 3"),
    (31, 40, "Range 4")
]

while True:
    try:
        num = int(input("Enter an integer: "))
        found = False

        for start, end, label in ranges:
            if start <= num <= end:
                print(f"The number is in {label}: {start} to {end}")
                found = True
                break

        if not found:
            print("The number is outside the specified ranges.")
        break

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
