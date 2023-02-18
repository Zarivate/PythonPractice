# Higher order functions are functions that do 1 of 2 things
# 1. Accepts a function as an argument
# or
# 2. Returns a function (In Python, functions are also treated as objects)

def yell(text):
    return text.upper()

def quiet(text):
    return text.lower()

# Higher order function
def howdy(func):
    # Equivalent of saying text = yell("Howdy") or quiet("Howdy) depending on what is sent in
    text = func("Howdy")
    print(text)

howdy(yell)
howdy(quiet)


# Example of second case, since divisor is returning dividend

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

# Would be called like this, first a variable is assigned to the outer function
# At first the inner function is skipped since it was not called yet, dividend is returned
# and assigned to the variable divide. Now because the variable has the memory address
# of the function dividend, it can be called
divide = divisor(2)
# Now dividend is being called and passed in 10
print(divide(10))