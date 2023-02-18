# Assigning functions to variables is essentially storing the memory address of the function within the variable

def howdy():
    print("Howdy")

print(howdy)
# This stores the memory address of the howdy() function within hi
hi = howdy
print(hi)
# However because it now holds the same memory address, it can be used to call the function as well
hi()

# Works with built-in functions as well
say = print
say("This works somehow, amazing huh?")