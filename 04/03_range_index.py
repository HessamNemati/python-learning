# negative index
#         -6  -5  -4  -3  -2  -1 
# positive index
#          0   1   2   3   4   5 
my_list = [12, 13, 11, 10, 14, 15]

# access / read
# [start:end(not included): step]

#          start 
print(my_list[2:]) # [11, 10, 14, 15]
print(my_list[2:: -1]) # [11, 13, 12]
print(my_list[:-2]) # [12, 13, 11, 10]
print(my_list[:-2: -1]) # [15]
print(my_list[2:-2: -1]) # []

# brackets []

# my_list[:-2: -1]: [15]
# [15][0]
print(my_list[:-2: -1][0]) # 15
print(my_list[::-1]) 
# [15, 14, 10, 11, 13, 12]
