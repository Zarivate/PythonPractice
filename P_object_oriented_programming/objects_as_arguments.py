# Objects can be passed as arguments in functions the same way as they can in other
# programming languages, mainly just some syntax things that need to be wary of. That
# and how what can be passed in is limited to objects with matching attributes and
# variables to those being affected by the function.

class Turtle:

    color = None


class Motorcycle:

    color = "Orange"

# Similar to other programming languages, the name of the passed in variable doesn't have to be the same as the
# object being altered. In fact the function can even be used on multiple objects.
def change_color(objectWhatever, color):

    objectWhatever.color = color

turtle_1 = Turtle()
turtle_2 = Turtle()
turtle_3 = Turtle()
print(turtle_1.color, turtle_2.color, turtle_3.color)

change_color(turtle_1, "White")
change_color(turtle_2, "Teal")
change_color(turtle_3, "Yellow")
print(turtle_1.color, turtle_2.color, turtle_3.color)

moto_1 = Motorcycle()
change_color(moto_1, "Scrimblo")
print(moto_1.color)
