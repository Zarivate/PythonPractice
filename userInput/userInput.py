# User input works similar to in JS where, instead of prompt(), use input() and save the answer in a variable
name = input("Howdy, what's your name?: ")
print("Howdy there, " + name)

# User input is always in the data type of string, this can be worked around however with typecasting
# Double typecasting is also possible but redundant, just typecast it as the outer one.
age = float(int(input("How long do you want to live too?: ")))

age = age + 70

# Just remember to typecast it as a string again if you ever need to print it out
print("I see, so you want to live up to " + str(age) + " years old huh?")

