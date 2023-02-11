# Work same as in other languages, where they're blocks of code that are only executed when it's called

# Small differences in syntax involved in creating them however
def howdy():
    print("Howdy there")

howdy()

# Functions can take in arguments same as in other languages as well, similar to other languages
# You can't call a function before its creation. Any attempt to invoke howdy2 before this line won't work
def howdy2(name):
    print("Howdy there " + name)

howdy2("bort")
test_name = "Biff Chigston"
howdy2(test_name)

# Functions can also have multiple arguments of various data types as well like in other languages too
def howdy3(name, hobby, age):
    print("Howdy there " + name)
    print("It looks like you're hobby is " + hobby + " , I worry for you")
    print("It also looks like you're " + str(age) + " years old, how nice")

howdy3("Dongus", "Birk", 709)