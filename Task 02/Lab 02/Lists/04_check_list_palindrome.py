# ===============================
#  Check if a List is Palindrome
# ===============================

#Way One
def is_palindrome_with_slicing(lst):
    return lst == lst[::-1]
#Way Two
def is_palindrome_without_slicing(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1

    return True

while True:
    user_input = input("Enter a list of integers separated by commas (e.g. 1,2,3,2,1): ").strip()
    try:
        lst = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
        if not lst:
            print("List cannot be empty.")
            continue
        result_1 = is_palindrome_with_slicing(lst)
        result_2 = is_palindrome_without_slicing(lst)
        print("Is palindrome (Way One)?", result_1)
        print("Is palindrome (Way Two)?", result_2)
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
