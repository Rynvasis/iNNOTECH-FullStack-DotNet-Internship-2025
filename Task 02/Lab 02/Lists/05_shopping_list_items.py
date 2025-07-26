# ======================
#  Shopping List Program
# ======================

shopping_list = []

print("Enter 10 items for your shopping list:")

while len(shopping_list) < 10:
    item = input(f"Item {len(shopping_list)+1}: ").strip()
    if item == "":
        print("Item cannot be empty. Try again.")
        continue
    shopping_list.append(item)


print("\nFull Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")


print("\nSelected Items:")
print(f"Item 2: {shopping_list[1]}")
print(f"Item 8: {shopping_list[7]}")
