# A daemon thread is a thread that runs in the background, not important for a program to run
# Your program will not wait for daemon threads to complete before exiting , non daemon threads
# cannot normally be killed, they stay alive until the task is complete. Common uses would be for
#
# background tasks, garbage collection, waiting for input, long-running processes, etc

import threading
import time

# An example would be something like a background process keeping track of how long someone is logged in for
# while the main program runs

def timer():
    print()
    print()
    time_logged_in = 0
    while True:
        time.sleep(1)
        time_logged_in += 1
        print("Logged in for ", time_logged_in, " seconds")

# Can make a thread into a daemon thread by using the daemon parameter
x = threading.Thread(target=timer, daemon=True)
x.start()

# Can convert a thread into a daemon thread using this method as well
# x.setDaemon(True)
# Can check whether a thread is a daemon thread
print(x.daemon)

answer = input("Do you want to leave and go far away? ")