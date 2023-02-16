# modules are files that have Python code, may have functions, classes, etc.
# Used to separate programs into parts, IE: Modular programming

# Many ways to import, could be with an alias name for easier typing or can just import
# the functions themselves.
# from module_example import hello, bye
# Could also import everything, however could be dangerous as some function names may overlap with others
# from module_example import *
import module_example as ie


ie.hello()
ie.bye()

# Print out a list of all available modules
help("modules")