# map() applies a function to each item in an iterable (list, tuple, etc.)
# Loved using this one back in React, syntax is different here however
# Syntax is
# map(function, iterable)

store = [("shoe", 25.00),
         ("pants", 15.00),
         ("shirt", 10.00),
         ("mango", 50.00)]

convert_to_zimbabwe_dollars = lambda data: (data[0], data[1]*322)
convert_back_to_us = lambda data: (data[0], data[1]/322)

# Is converted into a list so can be stored as a new variable
store_zimbabwe = list(map(convert_to_zimbabwe_dollars, store))
store_normal = list(map(convert_back_to_us, store_zimbabwe))

for i in store_zimbabwe:
    print(i)
print()

# The same store but converted back from what it was
for i in store_normal:
    print(i)