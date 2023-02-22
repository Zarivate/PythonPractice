# Just a few handy and common use showcases of the time module
import time

# Retrieves a computer's epoch (date and time from which a computer measures system time)
# What happens is that converts whatever time was passed in, into seconds, and converts into a readable time
# Since passed in 0, we get the epoch time back
print(time.ctime(0))

# Returns the amount of seconds that have passed since the epoch time
print(time.time())

# Many ways to do it but just one of the ways to return the current data and time
print(time.ctime(time.time()))
# Other way of getting current date and time but with localtime method and the use of a time object
time_object = time.localtime()
print(time_object)
# Using the documentation page on strftime(), can alter how data is displayed
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

# For coordinated universal time (UCT), use the gmtime() method
time_object = time.gmtime()

# Get a time object from a string that represents a time and or date
example_string = "11 July, 2011"
time_object2 = time.strptime(example_string, "%d %B, %Y")
print(time_object2)

# When creating a time tuple, 9 possible values can be passed in
# (year, month, day, hours, minutes, secs, # day of week, # day of year, daylight savings time (dst))
time_tuple = (2005, 3, 11, 7, 25, 19, 0, 0, 0)

# Accepts a tuple representation of time/time object as well.
time_string = time.asctime(time_tuple)
# Seconds since epoch version
time_string_seconds = time.mktime(time_tuple)
print(time_string)
print(time_string_seconds)