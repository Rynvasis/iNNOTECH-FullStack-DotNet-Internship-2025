# ===================================
#  Count Upper and Lower Case Letters
# ===================================

while True:
    text = input("Enter a non-empty string: ").strip()
    if not text:
        print("Input cannot be empty. Please try again.")
        continue
    break

upper_count = 0
lower_count = 0

for char in text:
    if char.isalpha(): 
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

print(f"No. of Upper case characters: {upper_count}")
print(f"No. of Lower case characters: {lower_count}")
