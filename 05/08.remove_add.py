my_list = ["A", "A", "B", "C", "A", "B", "A"]
copied_my_list = my_list.copy()

for item in copied_my_list:
    if item == "A":
        my_list.remove(item)

print(my_list)