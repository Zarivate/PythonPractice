# *args = A possible parameter in a function that packs all arguments into a tuple
# helps when you need to make a function that accepts a varying amount of arguments

# Normal function
def normal_way(num1, num2):
    return num1 + num2

print(normal_way(5,3))

# Doing something like below wouldn't work because only accepts 2 arguments, this is where *args comes in
#normal_way(5,3,1)

# Doesn't have to be called "args" either, so long as star is there can be named whatever
# Don't forget that tuples are ordered and unchangeable, so they can't be altered in the function
def star_way(*ooga_booga):
    sum = 0
    # If you do need to alter the values within, just change them into something that is mutable like so
    ooga_booga = list(ooga_booga)
    ooga_booga[2] = 2
    for value in ooga_booga:
        sum += value
    return sum

print(star_way(5,3,1))