# dictionary comprehension is similar to list comprehension but instead for dictionaries. They can be created
# using an expression and can replace for loops and certain lambda functions

# Like list comprehensions they also follow various patterns, below is the 1st one
# dictionary = {key: expression for (key/value) in iterable}

cities_in_fahrenheit = {'New Dank City': 39, 'Boston':55, 'Los Angeles': 271, 'Seatlle':79}

# Conversion pattern 1st way below, .items() is used since working with dictionary
cities_in_celsius = {key: round((value-32)*(5/9)) for (key,value) in cities_in_fahrenheit.items()}
print(cities_in_celsius)

# Can also add if conditional to end of pattern which would go like so
# dictionary = {key: expression for (key/value) in iterable if conditional}

weather = {'New Dank City': 'windy', 'Boston':'raining', 'Los Angeles': 'Hell', 'Seatlle':'windy'}
# Second pattern here, also not much of an expression here so instead just put plain "value"
sunny_places = {key: value for (key,value) in weather.items() if value == "windy"}
print(sunny_places)

# There is also a third version where you can also put an extra if/else conditional near the start
# dictionary = {key: (if/else) for (key/value) in iterable}
cities_in_fahrenheit2 = {'New Dank City': 39, 'Boston':55, 'Los Angeles': 271, 'Seatlle':79}
desc_cities = {key: ("Warm" if value >= 40 else "Don't go here") for (key,value) in cities_in_fahrenheit2.items()}
print(desc_cities)

# There's even a 4th way of doing this that involves calling a separate function in order to keep
# code a bit more organized that goes like so
# dictionary = {key: function(value) for (key/value) in iterable}
cities_in_fahrenheit3 = {'New Dank City': 39, 'Boston':55, 'Los Angeles': 271, 'Seatlle':69}
# Created function
def check_temp(value):
    if value >= 70:
        return "This is Los Angeles, isn't it?"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Chilly"

desc_cities2 = {key: check_temp(value) for (key,value) in cities_in_fahrenheit3.items()}
print(desc_cities2)