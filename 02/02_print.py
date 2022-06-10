# built-in function
# print

# terminal , console
print("Hello world")
print("Hello", "world") # sep: default: " "
print("Hello", "world", sep="_")
print("Hello", "world", sep="*")
print("Hello", "my",              "name",            "is", "hessam", sep="*")
print("Hello", "my",              "name",            "is", "hessam") # there is a comment 
print("Hello", "my", "name", "is", "hessam", sep="*")
print("------------------------------------------------------")

# "Hello world\n"
# override default value of `end`
print("Hello world",  end="\n") # \n: next line
print("Hello", "world", end="-")
print("Hello", "world", end="-----\n")
print("Hello", "world") 

# print(sep=, end=)
print("Hello", "world", sep="-*-", end="=\n") 
print("Hello", "world") 

