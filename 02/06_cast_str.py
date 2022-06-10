b1 = "hessam"
b2 = "12"

b3 = str(b1) # str -> str
# a3_1 = int(b1) # str -> int raise exception
b4 = str(b2) # str -> str

b5 = str(12) # int -> str | "12"
b6 = str(12.3) # float -> str | "12.3"
b7 = str(12.9) # float -> str | "12.9"
b8 = str(True) # bool -> str | "True"
b9 = str(False) # bool -> str | "False"
# only accept one param
# TypeError: str() argument 2 must be str, not int
# b10 = str(12, 13) # raise exception
# concatenation 
# str + str -> str 
# "Hello" + "Hessam" = "HelloHessam"
# b11 = "Hessam12"
b11 = str(b1 + b2)

print("b1", b1, type(b1))
print("b2", b2, type(b2))
print("b3", b3, type(b3))
print("b3", b4, type(b3))
print("b5", b5, type(b5))
print("b6", b6, type(b6))
print("b7", b7, type(b7))
print("b8", b8, type(b8))
print("b9", b9, type(b9))
# print("b10", b10, type(b10))
print("b11", b11, type(b11))
