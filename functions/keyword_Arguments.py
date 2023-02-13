# keyword arguments, different from positional arguments that depend on data being sent
# to a function in the correct order. Keyword arguments instead are preceded by an
# identifier when passed to a function, Python knows the names of the arguments that
# a function receives

def howdy(first, second, last):
    print("Hello " + first + " " + second + " " + last)

# Positional arguments example
howdy("Bort", "Chiggy", "Doem")

# Keyword arguments example
howdy(last="Chiggy", second="Doem", first="Chiggy")