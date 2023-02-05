# Python variables work much the same as in other languages, In Python they act as a container for a value,
# with the value being determined by whatever the user decides to store in it

# Examples, no need to declare type which is nice
name = "Biff"
number = 7
math = 5 + 5

# Can all be printed out and even have their data types printed out if done correctly
print(name), print(type(name))
print(number), print(type(number))
print(math), print(type(math))

# Can also combine two variables into one so long as same data type like so
first_name = "Quig"
# The space at the start is still counted as part of the string here
last_name = " Shiggy"
cursed_name = first_name + last_name
print("\nAn awful name to have is " + cursed_name)

# int data type
age = 97
age += 1
# Can't print out a string along with an int variable unless you type cast it like so, similar to other languages
print("\nI hope you live to at least be " + str(age))

# float data type, decimals pretty much
height = 753.7
# This results in 7753.7, instead of just adding 7 to the height. This is because of how it was type cast as a string
print("\n" + str(number) + str(height))
# However this adds the two normally to get 760.7
print(number + height)
# Can type cast a float into an int and even print them out together but truncates the decimal value, gets you 760.0
print(float(number) + int(height))

# boolean, true or false. Works same as in other languages
smart = False
print("\nHave your peers judged you too be smart? The answer is " + str(smart))

# Multiple assignments
# These two result in the same thing
# name2 = "Shig"
# height2 = 755
# happy = True

name2, height2, happy = "Shig", 755, True
print(name2)
print(height2)
print(happy)