#==================
# Add Employee Data
#==================

employee_dict = {}

while True:
    try:
        emp_id = input("Enter employee number (or type 'done' to stop): ").strip()
        if emp_id.lower() == 'done':
            break

        if not emp_id.isdigit():
            print("Employee number must be numeric.")
            continue

        if emp_id in employee_dict:
            print("This employee number already exists.")
            continue

        name = input("Enter employee name: ").strip()
        job = input("Enter job title: ").strip()

        employee_dict[emp_id] = {
            'name': name,
            'job': job
        }
    except Exception as e:
        print(f"Unexpected error: {e}")

print("\nEmployee Data:")
for emp_id, data in employee_dict.items():
    print(f"ID: {emp_id} | Name: {data['name']} | Job: {data['job']}")

