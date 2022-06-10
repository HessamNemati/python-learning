# logical operator

"""
output: bool True/False
and 
or
not

and - at least one of them must not be False 
False and False = False
False and True = False
True and False = False
True and True = True

or - at the least one of the them must be True
False or False = False
False or True = True
True or False = True
True or True = True


"""
a = 12
b = 13
c = 14

#       False and False => False 
print(a > b and c < b)
#       False or False => False
print (a > b or c < b)
# 
print(a > b and c < b and b < a)
#     not False => True    
print(not (a > b))

# ZeroDivisionError: division by zero
# print("Before incident")
# print(12 / 0)
# print("After incident")

# and
#     False
print(a > b and c > b)
print(a > b and 12 / 0)

# or 
print(b > a or c < a)
print(b > a or 12 / 0)

x = 12
y = 0
print(y != 0 and x < y)
print(y != 0 and x / y)
# ZeroDivisionError: division by zero
print(y == 0 and x / y)
