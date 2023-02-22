# filter() creates a collection of elements from an iterable for which a function returns
# Follows similar syntax to map
# filter(function, iterable)

enemies = [("Meka", 29),
           ("SEGA", 63),
           ("DF", 300000),
           ("Bob Ross", 55),
           ("Unga Bunga", 25),
           ("Sid the science kid",  11)]

age = lambda data: data[1] >= 33

eligible_to_eat_mangos = list(filter(age, enemies))

for i in eligible_to_eat_mangos:
    print(i)