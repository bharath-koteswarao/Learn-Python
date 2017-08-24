"""
Dictionaries are simple key value pairs

Adding elements to dictionary is same as adding elements to objects in javascript

"""

# Initialization

a = {
    "name": "bk",
    "name2": "bharath"
}

print(a)

print(a['name'])

a['new prop'] = 'some new property'

print(a)

del a['name2']

print(a)

print('name' in a)  # Prints whether 'name' key is there in dictionary or not

# List comprehensions can be used in dictionaries as well

for i in a:
    print(i)
# Above one prints all keys in the dictionary
