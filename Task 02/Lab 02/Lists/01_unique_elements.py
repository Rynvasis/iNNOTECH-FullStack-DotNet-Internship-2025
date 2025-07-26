# ==========================
#  Unique Elements from List
# ==========================

while True:
    user_input = input("Enter a list of integers separated by commas (e.g. 1,2,3,3,4): ").strip()
    try:
        items = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
        if not items:
            print("List cannot be empty. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Make sure all items are integers.")

#Way One
unique_items_1 = []
for item in items:
    if item not in unique_items_1:
        unique_items_1.append(item)

#Way Two
unique_items_2 = list(set(items))
unique_items_2.sort()
print("Unique List (Way One):", unique_items_1)
print("Unique List (Way Two):", unique_items_2)
