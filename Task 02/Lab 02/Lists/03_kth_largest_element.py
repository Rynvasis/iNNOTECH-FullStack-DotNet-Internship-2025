# ===================================
#  Find kth Largest Element in a List
# ===================================

def find_kth_largest(lst, k):
    if k <= 0 or k > len(lst):
        return None
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[k - 1]

while True:
    try:
        user_input = input("Enter a list of integers separated by commas (e.g. 5,1,9,3): ").strip()
        lst = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
        if not lst:
            print("List cannot be empty.")
            continue

        k = int(input("Enter the value of k (e.g. 2 for 2nd largest): "))
        result = find_kth_largest(lst, k)

        if result is None:
            print("Invalid value of k. Must be between 1 and length of list.")
        else:
            print(f"The {k}th largest element is: {result}")
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
