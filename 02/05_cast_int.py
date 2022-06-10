# cast

# int
a0 = "12"
a1 = 12
a2 = int(a1) # int -> int
a3 = int("12") # str -> int
a4 = int(a0) # str -> int
a0 = int(a0) # re-assign
a5 = int(True) # bool -> int | 1
a6 = int(False) # bool -> int | 0
a7 = int(12.2) # float -> int | 12
a8 = int(12.9) # float -> int | 12
# ValueError: invalid literal for int() with base 10: 'hessam'

# a10 = int("hessam") raise exception

# int(a, b) two params
# int(a, b) only accept one param
hessam = 10
a9 = int(hessam) # str -> int | 

print("a0", a0, type(a0))
print("a1", a1, type(a1))
print("a2", a2, type(a2))
print("a3", a3, type(a3))
print("a4", a4, type(a4))
print("a5", a5, type(a5))
print("a6", a6, type(a6))
print("a7", a7, type(a7))
print("a8", a8, type(a8))
print("a9", a9, type(a9))