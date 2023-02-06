# There are 2 methods that can be used for this
# indexing[] or slice()
# Options for slicing range from [start:stop:step] indexes

# IE
name = "Biff Chigston"

first_name = name[0:5] # Start index is inclusive while stop is exclusive, meaning won't include the last index
# Shorthand version also exists
also_first_name = name[:5]
last_name = name[5:]

print(first_name) # Biff
print(also_first_name) # Biff
print(last_name) # Chigston

# Step is how many letters you want to skip over when doing slicing, for instance
funky_name = name[0:13:2] # Would only print out every second letter, including the first one
print(funky_name) #Bf hgston
# Shorthand also exists
also_funky_name = name[::2]
print(also_funky_name)

# Possible to reverse an entire string using the step feature, just by using -1
reversed_name = name[::-1]
print((reversed_name))

# Slice method can be used to create slice objects that can be reused like so
website = "https://turtle.com"

# The start, stop, and step features exist in slice as well but are done with commas instead
# This will return only the name of the site itself that's between the https:// and the .com
# Negative indexes can be used to know how far at the end of a string you want to go, in this case -4 to stop at the .
slice = slice(8,-4)
print(website[slice])