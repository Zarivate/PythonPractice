# Read a file

# Depending on whether the file is just in the same directory or somewhere else, like on the Desktop,
# You'll have to use the file path like, "C:\\Users\\userNameHere\\Desktop\\fileNameHere",
# Instead of just the file name

# Does not catch any possible exceptions that may occur, those have to be coded in
try:
    with open('test.txt') as file:
        # This auto closes the file as well after reading it
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("File doesn't seem to exist")

# Checks whether the file is closed or not
print(file.closed)