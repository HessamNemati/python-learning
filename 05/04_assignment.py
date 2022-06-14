a = 12
b = a
print(a, b)

b= 13
print(a, b)

# ----------------
a = [1, 2, 3]
b = a
print(a, b)
print(id(a), id(b))

a.append(4)
print(a, b)
