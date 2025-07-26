# ===================
#  Palindrome Checker
# ===================

while True:
    text = input("Enter a non-empty string: ").strip()
    if not text:
        print("Input cannot be empty. Please try again.")
        continue
    break


processed = ''.join(text.lower().split())

if processed == processed[::-1]:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
