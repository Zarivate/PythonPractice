# Write a file

# Files are written very similar to how they are opened, read, and detected. Difference being the
# second value held within the second parameter

append_test = "\nThis text has been added\nSo pro, I know."
new_file_text = "This text is used for a completely new file"
overwritten_text = "This file has been overwritten."

# If you just want to append something, use "a" for the second parameter
with open('test.txt', 'a') as file:
    file.write(append_test)

# If you just want to write and create a new file, use "w" for the second parameter
with open('test2.txt', 'w') as file:
    file.write(new_file_text)

# You can completely overwrite what's already within a file using the write method too
# with open('test2.txt', 'w') as file:
   # file.write(overwritten_text)
