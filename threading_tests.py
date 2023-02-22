# A thread is like a flow of execution, a separate order of instructions. However, each thread
# takes a turn running in order to achieve concurrency.
# GIL = Global interpreter lock, allows only 1 thread to hold the control of the Python interpreter

# Can run concurrently, but not truly, in parallel
# Programs and tasks can be divided into 2 different categories

# 1. cpu bound = program/task that spends most of it's time waiting for internal events (CPU intensive).
# preferable to use multiprocessing for these kinds of tasks

# 2. io bound = program/task that spends most of it's time waiting for external events (user input, web scraping, etc)
# preferable to use multithreading for these

import threading
import time

# Print how many ongoing threads there are
print(threading.active_count())
# Prints list of threads active
print(threading.enumerate())


# Example of multithreading, where before leaving someplace 3 separate methods/things need to be taken care of.
# Each of these tasks are IO bound, wait for their sleep function to finish before moving on
def pet_turtle():
    time.sleep(5)
    print("Turtles have been pet!")


def change_clothes():
    time.sleep(4)
    print("Clothes have been changed")


def drink_water():
    time.sleep(3)
    print("Replenished liquids")

# All 3 will be run on the main thread and take approximately 15 seconds to finish
# pet_turtle()
# change_clothes()
# drink_water()


# In order to make this more realistic, each task can have their own thread created, will take about 5 seconds now
x = threading.Thread(target=pet_turtle, args=())
x.start()

y = threading.Thread(target=change_clothes, args=())
y.start()

z = threading.Thread(target=drink_water, args=())
z.start()


# Thread synchronization, concept of a thread waiting around for another thread to finish before continuing
# Now main thread has to wait for x to finish before it can move onto it's instructions sets below
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
# Print off how long it takes for the main thread to finish, in this case the main thread would be the one
# creating all the extra threads above and calling the 3 print statements/functions within them (active_count(),
# enumerate(), perf_counter(), etc))
print(time.perf_counter())


