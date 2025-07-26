# ==================
#  Reverse a String
# ==================

while True:
    text = input("Enter a non-empty string: ").strip()
    if not text:
        print("Input cannot be empty. Please try again.")
        continue
    break

# Way one
reversed_text_1 = text[::-1]

#Way two
reversed_text_2 = ""

for char in text:
    reversed_text_2 = char + reversed_text_2

print(f"Reversed string (Way One): {reversed_text_1}")
print(f"Reversed string (Way Two): {reversed_text_2}")
