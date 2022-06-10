"""
get three numbers from user/input
print maximum
"""
# خروجی input همیشه str است

a = int(input())
b = int(input())
c = int(input())

if a < b:
    # a < b
    if b < c:
        # a < b < c
        print(c)
    else:
        # a < c < b
        print(b)
else:
    # a > b
    if a < c:
        # b < a < c
        print(c)
    else:
        # b < c < a
        print(a)