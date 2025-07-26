# =========================
# Sort Dictionary by Value
# =========================

sample_dict = {
    'a': 3,
    'b': 1,
    'c': 5,
    'd': 2
}


items = list(sample_dict.items())
#-------------- Way One ----------------------
#  Sort Ascending 
for i in range(len(items)):
    min_index = i
    for j in range(i+1, len(items)):
        if items[j][1] < items[min_index][1]:
            min_index = j
    items[i], items[min_index] = items[min_index], items[i]

asc_sorted_1 = dict(items)

# Sort Descending 
items = list(sample_dict.items())

for i in range(len(items)):
    max_index = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_index][1]:
            max_index = j
    items[i], items[max_index] = items[max_index], items[i]

desc_sorted_1 = dict(items)

#-------------- Way Two ----------------------
# Sort Ascending
asc_sorted_2 = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

# Sort Descending
desc_sorted_2 = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))


print("\nOriginal Dictionary:")
print(sample_dict)

print("\nSorted by value (Ascending):")
print(f"Way One : {asc_sorted_1}")
print(f"Way Two : {asc_sorted_2}")

print("\nSorted by value (Descending):")
print(f"Way Two : {desc_sorted_1}")
print(f"Way Two : {desc_sorted_2}")

