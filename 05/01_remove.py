my_list = ["A", "B", "C", "A", "B", "A"]
# my_list = [1, 2, "A", False, 20.1, [1, 2]]

# count
print(my_list.count("A"))
print(my_list.count("E"))

# remove
# remove ONE "item" ("A") from the left
my_list.remove("A")
print(my_list)

# ValueError: list.remove(x): x not in list
# my_list.remove("D")
# print(my_list)

# pop - INDEX
# pop last item
item = my_list.pop()
my_list.pop()

# pop(index)
my_list.pop(2)

# clear
my_list.clear()
print(my_list)

# 
print(len(my_list))



