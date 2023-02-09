# for loops work the same here as they would in other langugages, only with minor differences
import time

# 10 here is exclusive so will print 0 up to 9
for i in range(10):
    print(i)

# In this case the 50 is inclusive while the 100 is exclusive. If you wanted to include the second number
# all you would have to do is add 1 to it. Would make it become 100+1 instead
for i in range(50, 100):
    print(i)

# Can also include a third argument, it's the step argument that says how much it should count up by
# the loop below counts up by 2. From 50 up to 100
for i in range(50,100+1,2):
    print(i)

# for loops can still be used to iterate over anything iterable like strings. This prints out every letter
for i in "Howdy":
    print(i)

# Example clock countdown code
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Countdown complete! You will now be annihilated!")