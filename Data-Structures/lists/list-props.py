a = [1, 2, 3, 4, 5, 6]
b = [x for x in a if x % 2 == 0]
print(b)

c = [x for x in a if x % 2 == 1 and x is not 1]

print(c)

d = [2 * x for x in a if x % 2 == 1]

print(d)
