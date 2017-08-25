""" Formatting of integers """

patt = '{0:b}'

# b denotes binary and nb denotes the number will be added 'n' spaces before

# d denotes decimal

# Python equivalent of Java's Integer.toBinaryString(int n) is patt.format(n)

patt.format(10)

# Z fill is used to make a number to required digits by adding zeros to that number

""" "10".zfill(3) makes 10 as 010"""

b = patt.format(10).zfill(6)

print(b)
