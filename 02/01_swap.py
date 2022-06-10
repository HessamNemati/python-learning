# swap

a = 12
b = 13

# 1. solution
c = a
a = b
b = c

# 2. solution
# pythonic
a, b = b, a

# 3. solution
a = a + b
b = a - b
a = a - b