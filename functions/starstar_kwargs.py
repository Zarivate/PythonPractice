# **kwargs = parameters that pack all arguments into a dictionary, helps when needing
# functions that can accept varying amount of keyword arguments
# Difference between *args is how that accepts positional arguments into a tuple while this
# one accepts keyword arguments into a dictionary

def howdy(**kwargs):
    print("Howdy " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])
    print("This is another way to do it too")
    print("Howdy", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

howdy(title="God King", first="Dongus", middle="Quandale", last="Dingle")
