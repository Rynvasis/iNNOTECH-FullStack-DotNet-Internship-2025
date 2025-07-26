# =================================
# Check if Key Exists in Dictionary
# =================================


sample_dict = {
    "name": "Ahmed",
    "age": 25,
    "city": "Cairo"
}

key_to_check = input("Enter the key to check: ")

if key_to_check in sample_dict:
    print(f"The key '{key_to_check}' exists in the dictionary with value: {sample_dict[key_to_check]}")
else:
    print(f"The key '{key_to_check}' doesn't exist in the dictionary.")
