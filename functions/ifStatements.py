# If statements, work very similar to other languages

age = int(input("How old are you?: "))

# In Python you need to watch out for the indentation after if statements that signal where if condition starts
if age >= 18:
    print("Congrats, you now pay taxes!")
# elif is shorthand for else if
elif age <= 0:
    print("How are you even answering this? Did you lie??????")
# else works the same in Python where it's the last option once the others have been exhausted
else:
    print("You are not a legal adult yet... lucky.")

# Have to be careful with how you order them in Python as well, as the first if statement will still be
# the first one printed over the others even if the other conditions are met