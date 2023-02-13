# Delete a file and or folder with files

import os
import shutil

path = 'delete_this.txt'
folder_path = 'toBeDeleted'

# This is for deleting files
try:
    os.remove(path)
except FileNotFoundError as e:
    print(e)
    print("File was not found.")
# If trying to delete a folder, you'll get permission errors
except PermissionError as e:
    print(e)
    print("You don't have permission to delete this")
else:
    print(path + " was deleted")

# This is for deleting folders, you may encounter OSErrors if it has files within
try:
    os.rmdir(folder_path)
except OSError as e:
    print(e)
    print("That folder has files within, not allowed!")
else:
    print(folder_path + " was deleted")

# This is to delete a folder alongside the files within, very dangerous so use carefully
try:
    shutil.rmtree(folder_path)
except OSError as e:
    print(e)
    print("That folder has files within, not allowed!")
else:
    print(folder_path + " was deleted")
