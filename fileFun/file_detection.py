# file detection
import os

# Use double backslashes as that's the escape sequence for them in a string
path = "C:\\Users\\userNameHere\\Desktop\\New folder"

if os.path.exists(path):
    print("The location does indeed exist.")
    if os.path.isfile(path):
        print("Yup, definitely a file")
    elif os.path.isdir(path):
        print("Turns out it's actually a directory.")
else:
    print("No location found")