# File copying can be done in many ways but for this test it's done using 3 methods from the shutil module
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification time)

import shutil
import os

# Holds two parameters, the src and dst location. The destination location can be a
# file path if necessary. Something like destination to the desktop
# copy() and copy2() work the same and are written the same as well
shutil.copyfile('test.txt', 'copy.txt')

if os.path.exists('copy.txt'):
    print("The copy file was successfully made")