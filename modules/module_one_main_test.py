# if __name__ == '__main__' means 2 things for a Python file/module
# 1. The module can be run as a standalone program
# 2. It can be imported and used by other modules
# Gives the file a bit more flexibility to be used
# When used in a file, is checked to see if the user is doing 1 of the 2 reasons above,

# Behind the scenes what's happening is that Python is setting __name__ to a default value
# of '__main__' if it's the initial module being run like so
# Don't import this unless you want a circular error
# import module_two


# Should print out "__main__
# print(__name__)
# Should not print out __main__, instead prints out the name of the module, "module_two"
# print(module_two.__name__)

def main():
    print("Howdy")


if __name__ == '__main__':
    main()

# Checks to see whether module is being run directly or indirectly
# if __name__ == '__main__':
#   print("Being run directly")
# else:
# Prints when module_two is run
#   print("Running indirectly")
