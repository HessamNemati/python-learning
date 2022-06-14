# a, b, c

# a , b , c
# a , c , b

a = int(input("enter "))
b = int(input("enter "))
c = int(input("enter "))

"""
a: 20 
b: 21 
c: 19

19 20 21
"""

if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c , b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
     print(b, a, c)
elif c < b < a:
    print(c, b, a)
elif c < a < b:
    print(c, a, b)
