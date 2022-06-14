# from copy import deepcopy

# without copy
a = [1, 2, 3, 4]
b = a

a.append(5)
b.append(6)

print(a)
print(b)
# ------------------------
# shallow copy
c = [1, 2, 3, 4]
d = c.copy()

c.append(5)
d.append(6)

print(c)
print(d)

# ------------------------
# deep copy
e = [1, 2, [3, 4]]
f = e.copy()

e[2].append(5)
f[2].append(6)

print(e)
print(f)

# ----------
m = [1, 2, [3, 4]]

from copy import deepcopy
n = deepcopy(m)

m[2].append(5)
n[2].append(6)

print(m)
print(n)


