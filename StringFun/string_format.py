# str.format() is an optional method for users when they want more control over how
# output is displayed

# Normal way of printing something
print("The moon is beautiful, isn't it?")

# Also normal way of printing something
object = "moon"
adjective = "beautiful"

print("The " + object + " is " + adjective + ", isn't it?")

# The big bois way of printing something out. could also just replace the variables
# below with straight-up text. The {} are referred to as "format fields"
print("The {} is {}, isn't it?".format(object, adjective))

# Positional argument version too
print("The {1} is {0}, isn't it?".format(object, adjective))

# Keyword argument version
print("The {object} is {adjective}, isn't it?".format(object="moon", adjective="beautiful"))
# You can reuse values as well
print("The {object} is {object}, isn't it?".format(object="moon", adjective="beautiful"))

# Most elegant way of doing this
text = "The {} is {}, isn't it?"
print(text.format(object, adjective))
print()

# Can also be used for formatting like so
name = "Obor"
print("Howdy, my name is {}".format(name))
# Can give padding, this gives 10 padding to the right
print("Howdy, my name is {:10}. Get lost now.".format(name))
# This gives 10 padding to the right
print("Howdy, my name is {:<10}. Get lost now.".format(name))
# This gives 10 padding to the left
print("Howdy, my name is {:>10}. Get lost now.".format(name))
# This center aligns the text/padding into the middle
print("Howdy, my name is {:^10}. Get lost now.".format(name))
print()

# Can be used to format numbers too
number = 3.14159
grands = 1000000
print("The value for pi is {}".format(number))
# If you want too only show a few decimal places can do so like this, be wary tho as will round value
print("The value for pi rounded is {:.3f}".format(number))
# Can also automatically add commas to every 1000 place
print("Look I automatically added commas too {:,}".format(grands))
# Can also convert value too binary, octal, hexa, and even scientific notation
print("The value in binary is {:b}".format(grands))
print("The value in octal is {:o}".format(grands))
print("The value in hexa(large) is {:X}".format(grands))
print("The value in scientific notation is {:E}".format(grands))