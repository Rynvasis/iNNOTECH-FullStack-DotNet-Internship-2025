# ===================================
#  Extend Shopping List - Insert Item
# ===================================

shopping_list = []

print("Enter 10 items for your shopping list:")
while len(shopping_list) < 10:
    item = input(f"Item {len(shopping_list) + 1}: ").strip()
    if item == "":
        print("Item cannot be empty. Try again.")
        continue
    shopping_list.append(item)


print("\nFull Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")


new_item = input("\nEnter the new item to insert: ").strip()
while True:
    try:
        position = int(input(f"Enter the position to insert the item (1 to {len(shopping_list)+1}): "))
        if 1 <= position <= len(shopping_list) + 1:
            shopping_list.insert(position - 1, new_item)
            break
        else:
            print("Invalid position. Try again.")
    except ValueError:
        print("Please enter a valid integer.")


print("\nUpdated Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")
