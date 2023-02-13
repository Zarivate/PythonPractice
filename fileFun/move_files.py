# Moving a file

import os

# This can work on directories too, though you'll have too obviously change the name
# to the folder name and the destination to the folder name too
source = 'moving_file.txt'
# Moving the file to the outermost project folder
destination = "C:\\Users\\izara\\Desktop\\Projects\\PythonShennanigans\\moving_file.txt"

try:
    if os.path.exists(destination):
        print("Looks like either the file already exists or was already moved prior")
    else:
        os.replace(source,destination)
        print(source + " was moved!")
except FileNotFoundError:
    print(source + " was not found sadly")