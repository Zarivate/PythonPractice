# dictionary = A changeable, unordered, collection of unique key:value pairs
# utilizes hashing, so it's very fast, allows quick access to values

capitals = { "Mexico": "Mexico City", "India": "New Dehli", "Detroit": "Hell 2", "France": "Paris"}

# If you want to check whether a value exists in a dictionary, best to use the get() method
# Zimbabwe doesn't exist in the dictionary but instead of getting an error it will return none
print(capitals.get("Zimbabwe"))

# Print only the keys
print(capitals.keys())
print("")

# Print only the values
print(capitals.values())
print("")

# Prints everything
print(capitals.items())
print("")

# A for loop can also be used to print everything too
for key, value in capitals.items():
    print(key, value)
print("")

# Dictionaries are mutable, meaning we can change them even after the program is already going
capitals.update({"Japan": "Tokyo"})
# Changes existing value pair
capitals.update({"Detroit": "Hell 3"})
# Removes a key value pair
capitals.pop("India")

for key, value in capitals.items():
    print(key, value)
print("")