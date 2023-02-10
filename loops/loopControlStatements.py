# Loop Control statements changes a loops execution from its normal pattern

# The three available are the same as in JS and Java

# break = terminates loop all together
# continue = skips to next iteration of loop
# pass = does nothing, placeholder essentially

# Break example, can break out of a while loop once gotten information that was requested
while True:
    name = input("Howdy, what would you like your name to be?: ")
    if name!="":
        break

# Continue example, can be used to skip unwanted characters when printing something
phone_number = "1234-567-8913"
for number in phone_number:
    if number =="-":
        continue
    print(number, end="")

# Pass example, can be used to skip certain elements that are unwanted, below skips the number 13
for number in range(1,21):
    if number == 13:
        continue
    else:
        print(number)