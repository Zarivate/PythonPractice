# Logical operators (and, or, not)

mood = int(input("On a scale of 1 to 10, from bad to best, how are you feeling?: "))
# "And" along with "or" work the same way as they would in other languages

# "and" only goes through if both conditions are met, same as in JS and Java
if mood >= 0 and mood <= 10:
    print("Dang, happy to see you're feeling so positive today!")
    print("Wish you the best")
# "or" goes through so long as one or the other condition is met, same as in JS and Java
elif mood < 0 or mood > 10:
    print("Man, sorry to hear you're feeling kinda down")
    print("Here's to thinks getting better!")

mood2 = int(input("On a scale of 1 to 10, from bad to best, how are you feeling?: "))
# The "not" operator just turns a condition into reverse like so. Prints out the same result, since the "not"
# operator has now reversed the true to false and vice versa

if not(mood2 >= 0 and mood2 <= 10):
    print("Man, sorry to hear you're feeling kinda down")
    print("Here's to thinks getting better!")
elif not(mood2 < 0 or mood2 > 10):
    print("Dang, happy to see you're feeling so positive today!")
    print("Wish you the best")
