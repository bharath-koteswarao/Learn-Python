string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vitae diam vestibulum, feugiat massa quis, 
luctus neque. In consectetur cursus urna quis rutrum. Nulla vel orci eget ipsum vulputate ultricies sit amet vitae 
felis. Nullam fringilla urna nibh, tempus sollicitudin leo mollis ac. Donec efficitur ullamcorper ipsum, ac interdum 
purus laoreet eget. Mauris id neque est. Suspendisse at risus lorem. Nam ut maximus augue. """
f = open("automatic file.txt", 'w')
f.write(string)
f.close()

""" 'w' is used to write into file and it deletes the previous file
    'a' is used to append the file
    'r' is used to open the file in read mode
    'r+' is used to read and write simultaneously
"""

f = open("automatic file.txt", 'r')

# f.readLine() is used to read a single line at a time

line = f.readline()

while line is not "":  # f.readLine() returns an empty string when it reaches the end of the file
    print(line)
    line = f.readline()

f.close()

f = open("automatic file.txt", 'r')

for line in f:
    print(line)

"""Extra methods of file handling :"""

# f.tell() returns the position of the caret in file

# f.seek() accepts two arguments one is the starting position and second is number of lines to be

# skipped from starting index
