# The index operator [] gives access to a sequence's elements (strings, lists, tuples, etc)

name = "bort Chiggy!"

# Can be used same as in other languages to check for certain elements in a variable
if(name[0].islower()):
    print("It looks like the first letter in your name is lower cased, let's change that!")
    name = name.capitalize()
    print(name)

# Can also be used to splice certain sections into other variables
first_name = name[:4].lower()
print(first_name)
last_name = name[5:].upper()
print(last_name)
last_character = name[-1]
print(last_character)