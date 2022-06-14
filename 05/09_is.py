a = 12
b = a

print(a == b) # Check value
print(a is b) # Check reference id(a) == id(b)

b= 13
print(a == b) # Check value
print(a is b) # Check reference id(a)c == id(b)
print("----------------------------------")

# ----------------
a = [1, 2, 3]
b = a

print(a == b) # Check value
print(a is b) # Check reference id(a) == id(b)
print("----------------------------------")

a = [1, 2, 3]
b = a.copy()

print(a == b) # Check value
print(a is b) # Check reference id(a) == id(b)