# Handling exceptions

# First the try block will be executed line by line and then

# If it come across some error then it checks for that exception in except block

# If the exception type is not there in except block then it will be treated as unhandled exception

try:
    a = 2 + 'bk'
except:
    print("Error occured")

    # a = 2 + 'bk' is an exception since an integer and string can't be added directly in python

    # If we know the type of exception that we are going to get then we can

    # mention it or just leave the except block as it is

    # If exception is some thing like AError then just give except(AError)
