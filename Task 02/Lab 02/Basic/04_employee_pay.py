# =======================================
#  Employee Gross and Net Pay Calculator
# =======================================

while True:
    try:
        hours = float(input("Enter number of hours worked: "))
        rate = float(input("Enter hourly rate: "))

        if hours < 0 or rate < 0:
            print("Hours and rate must be positive numbers.")
            continue

        gross_pay = hours * rate
        net_pay = gross_pay * 0.8 

        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Net Pay (after 20% tax): ${net_pay:.2f}")
        break

    except ValueError:
        print("Error: Please enter valid numbers.")
