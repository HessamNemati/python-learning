
c0 = 12.2
c1 = 12.9

c2 = float(c0) # float -> float
c3 = float(c1) # float -> float
# c4 = float("12.1") 
c4 = float("12") # str -> float | 12.0
c5 = float("12.2") # str -> float
c6 = float(12) # int -> float | 12.0
# ValueError: could not convert string to float: 'Hessam'
# c7 = float("Hessam") # str -> float | raise exception
c8 = float(True) # bool -> float | 1.0
c9 = float(False) # bool -> float | 0.0

print("c0", c0, type(c0))
print("c1", c1, type(c1))
print("c2", c2, type(c2))
print("c3", c3, type(c3))
print("c4", c4, type(c4))
print("c5", c5, type(c5))
print("c6", c6, type(c6))
# print("c7", c7, type(c7))
print("c8", c8, type(c8))
print("c9", c9, type(c9))


