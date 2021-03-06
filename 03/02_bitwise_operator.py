# bitwise operator
"""
10 ^ 0 = 1
10 ^ 1 = 10
10 ^ 2 = 100
10 ^ 3 = 1000
10 ^ 4 = 10000
------------------------------------------------
دهدهی
decimal
base: 10
range: 
  [0, 1, ..., 9][0, 1, 2, 3, 3, ..., 9]
  [0: base-1]

12     = [1 * (10 ^ 1)] + [2 * (10 ^ 0)] 
110    = [1 * (10 ^ 2)] + [1 * (10 ^ 1)] + [0 * (10 ^ 0)]
1111   = [1 * (10 ^ 3)] + [1 * (10 ^ 2)] + [1 * (10 ^ 1)] + [1 * (10 ^ 0)] 
------------------------------------------------
دودویی
binary
base: 2
range:
  [0, 1]
------------------------------------------------
deciaml -> binary
12 -> (?)

Bitwise operators:
    & AND
    | OR
    ^ XOR
    ~ NOT

& AND
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

| OR
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0

^ اگر تعداد 1هایم فرد باشد من به شما 1 میدهم XOR
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
1 ^ 1 ^ 1 = 1

~
0 = 1
1 = 0
------------------------------------------------
7 & 5 = 5 (Min)

7 -> 111
5 -> 101

111 
101 &
----
101 -> 5  
------------
7 | 5 = 7 (Max)

7 -> 111
5 -> 101

111 
101 |
----
111 -> 7  
------------
7 ^ 5 = 2 (Diff)

7 -> 111
5 -> 101

111 
101 ^
----
010 -> 2  
"""

print(5&7)
print(5|7)
print(5^7)
