# list
# Ordered - ترتیب برایش مهم است
# Changeable - mutable - تغییر پذیر
# Duplication is allowed

a = 2
b = 2
my_list = [1, 2, 3 ,4, 1]

# append
my_list.append(5)
print(my_list)

# extend
my_list.extend([1, 2, 3])
print(my_list)

my_list.append([1, 2, 3])

# [1, 2, 3, 4, 1, 5, 1, 2, 3, [1, 2, 3]]
# [1, 2, 3, 10,         4, 1, 5, 1, 2, 3, [1, 2, 3]]

# insert
my_list.insert(3, 10)
print(my_list)
