# =======================================
# Iterate Over Dictionary using For Loops
# =======================================

# Sample dictionary
student_info = {
    "name": "Ahmed",
    "age": 21,
    "major": "Information Technology"
}

# Iterate over keys
print("Keys:")
for key in student_info:
    print(key)

# Iterate over values
print("\nValues:")
for value in student_info.values():
    print(value)

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in student_info.items():
    print(f"{key} : {value}")
