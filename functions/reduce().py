# reduce() does what it's name implies, it reduces an iterable to a single cumulative value by applying
# a function to it. The function is performed on the first two elements and repeated until there is only 1 value
# Syntax goes same as filter9), map(), and reduce()
# reduce(function, iterable)

import functools

letters = ["H", "O", "W", "D", "Y"]

# Many ways to combine letters into 1 word but this is just a simple example
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

# Works great for factorials too
factorial = [7,6,5,4,3,2,1]
# What's happening is it's multiplying 7*6 together first to get 42, then multiply 42 by 5 and so forth
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)