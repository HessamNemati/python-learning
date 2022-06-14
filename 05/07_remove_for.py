my_list = [1, 2, 3, 4]

# counter: 0
# counter: 1
# counter: 2
for item in my_list:
    # item: my_list[counter]
    # item: 1
    # item: 3
    print(item)
    my_list.remove(item)
    # my_list: [2, 3, 4]
    # my_list: [2, 4]

print(my_list)