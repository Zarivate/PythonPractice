# In Python the most common way to handle exceptions is too wrap everything around in a try catch block
# Similar to Java. Best practice is too first catch any exceptions that are already expected before
# catching any general ones. Just like in in other languages you can print out the error as well.

try:
    top = int(input("Enter a whole number please: "))
    bottom = int(input("Enter a whole number again please: "))
    result = top / bottom

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 you silly goose.")
except ValueError as e:
    print(e)
    print("Only numbers are acceptable.")
except Exception as e:
    print(e)
    print("Yeah something wrong happened, sorry.")
else:
    print(result)
finally:
    print("This will always execute, see?")