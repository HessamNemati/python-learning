# False values: 0, 0.0, "", False

d0 = True
d1 = False
d2 = bool(d0) # bool -> bool
d3 = bool(d1) # bool -> bool
d4 = bool(12) # int -> bool |  True
d5 = bool(12.2) # float -> bool | True
d6 = bool(0.1) # float -> bool | True
d7 = bool(0) # float -> bool | False
d8 = bool(-6) # int -> bool | True 
d9 = bool("Hessam") # str -> bool | True
d10 = bool(" ") # str -> bool | True
d11 = bool("") # str -> bool | False

print("d0", d0, type(d0))
print("d1", d1, type(d1))
print("d2", d2, type(d2))
print("d3", d3, type(d3))
print("d4", d4, type(d4))
print("d5", d5, type(d5))
print("d6", d6, type(d6))
print("d7",d7 , type(d7))
print("d8",d8 , type(d8))
print("d9",d9 , type(d9))
print("d10", d10, type(d10))
print("d11",d11 , type(d11))

