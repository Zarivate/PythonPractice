# scope refers to the same as what it would in other languages, the region that a variable
# is recognized in. Global and locally scoped variables still exist and work the same way.
# Python utilizes variables using the LEGB  rule, Python will first try to use
# Local variables
# Enclosing variables
# Global variables
# Built-in variables

# Can name two variables the same thing so long as are in different scopes
test = "This is a Global variable"

def display_variable():
    test = "This is a local variable exclusive to this function"
    print(test)

display_variable()
print(test)