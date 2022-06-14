my_list = [1, 2, 3 ,4]

#            0       1   
#           0  1    0  1
my_list = [[1, 2], [3, 4]]

print(my_list[0][1])

my_list = [[[1, 2], [3 ,4]]]

# m1 = my_list[0]: [[1, 2], [3 ,4]]
# m1[0][1]
# m2: m1[0] = [1, 2]
# m2[1]: 2
print(my_list[0][0][1])
print(my_list[0][1][1])