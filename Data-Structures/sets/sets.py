# We can't access elements of sets.

# We can only iterate over the elements of sets

# Two type of sets

# First : Set of words and set of a single word

# First one :

a = {"name", "bk"}

b = set("bharath")

c = set("bharath koteswarao")

print(b, "This is set b")

# Sets support list type comprehensions

d = {x for x in c and b}

print(d, "This is set of common elements")

e = c - d  # Letters in c but not in d

print(e)

"""
c - d is letters in c or d but not in both

c | d is letters either in c or d   same as OR operation

c & d is letters in both c and d    Same as AND operation

c ^ d is letters in a or b but not in both   Same as XOR operation



"""
