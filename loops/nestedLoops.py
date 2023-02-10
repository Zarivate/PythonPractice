# nested loops are logically the same here as they are in other languages, where the inner loop
# finishes before the outer one

# The code below prints out a shape of a certain character, with the number of rows and columns being done through loops

rows = int(input("How many rows do you want?: "))
columns = int(input("How many columns do you want?: "))
symbol = input("Enter a character/symbol to be used: ")

for row in range(rows):
    for column in range(columns):
        # dding the end="" here prevents each print being done on a new line like normal
        print(symbol, end="")
    # Prints new line once done with inner loop
    print()