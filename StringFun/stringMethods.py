# Various methods available to manipulate strings
name = "Dongus chen"

# Most are self-explanatory,
print(len(name))
print(name.find("o")) # Returns first instance of whatever it is you're looking for, this case being position 1
print(name.capitalize()) # Capitalizes first letter of first word, but not following word. So would only capitalize Dongus but not chen
print(name.upper())
print(name.lower())
print(name.isdigit()) # Returns whether something is all numerical digits
print(name.isalpha()) # Returns whether something is all alphabetical letters or not, if there is a space at all returns false
print(name.count("c"))
print(name.replace("n", "q"))
# Can also print multiple of the same thing shorthand like so, no space between them obviously
print(name*3)