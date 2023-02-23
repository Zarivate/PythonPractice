# Multiprocessing is running multiple tasks in parallel on different cpu cores, this bypasses the
# GIL used for threading
# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (idle/waiting tasks)

from multiprocessing import Process, cpu_count
import time
start = time.perf_counter()

# This will be a heavy cpu usage task as the number it will count up to will be ridiculous for the sake of example
def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    # Depending on how many cpu cores you have, your performance will not get better if you do more than how many
    # cores you have because of the overhead in creating and deleting processes
    print(cpu_count())
    
    # How processes are made, similar to how threads are. Since only 1 argument as well and a tuple needs
    # to be passed in, a blank comma is left afterwards
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    # Process synchronization with main process, main will now wait for child a process to finish before continuing
    a.join()
    b.join()
    c.join()
    d.join()
    print("Finished in ", time.perf_counter()-start, " seconds")


# This is here because, since this could be run on a Windows machine, a child process born from the main process
# /module will copy the module that is currently being worked on, which could then create its own children
# processes and so forth unless this is here that stops it from automatically executing
if __name__ == '__main__':
    main()