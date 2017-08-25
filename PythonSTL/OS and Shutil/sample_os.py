# os module is used to access system resources

# It can run cmd commands from python

# It can copy files in computer from one location to other

# basically it can do every thing as it is equivalent to cmd now !!

import os

print(os.getcwd())  # Prints the current working directory

# os.chdir() changes the current working directory

os.system("ipconfig")  # Equivalent to typing ipconfig in cmd

# st.copyfile(source,dest) creates a copy of source with dest as name

# similarly st.move() moves the file
