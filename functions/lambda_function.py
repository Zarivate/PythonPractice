# lambda function is a function that's written in 1 line using the "lambda" keyword.
# It accepts any number of arguments but only has 1 expression. Something of a shortcut,
# useful if needed for a short while, thrown-away almost right after though.
# Follows the following syntax
# lambda parameters:expression

# Can turn functions like this
def double(x):
    return x*2

print(double(10))

double_again = lambda x: x*2
print(double_again(10))
# More examples
multiply = lambda x, y: x * y
print(multiply(5,11))
add = lambda x, y, z: x + y + z
print(add(1,1,2))
# Can even be used with strings and have checks within them
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Dongus", "Dingle"))
age_check = lambda age:True if age >= 18 else False
print(age_check(9))