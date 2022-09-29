# Thread = A flow of execution. Like a seperate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the Python interpreter at any one time

# CPU Bound = Program / Taskl spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing

# i/o Bound = Program / Task spends most of its time waiting for external event (User Input,Web scraping)
#             use multithreading

import threading
import time

# Example of making different threads at different part of the program and run concurrently:

def eat_breakfast():                
    time.sleep(3)                   # These kinds of tasks is I/O Bound
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)                   # These kinds of tasks is I/O Bound
    print("You drank coffee")

def study():
    time.sleep(5)                   # These kinds of tasks is I/O Bound
    print("You finished studying")

# eat_breakfast()
# drink_coffee()
# study()                             # Tasks were completed sequentially but not concurrently

#  Total Time Executed using these method: 3 + 4 + 5 = 12 Seconds , because of the sequential process


x = threading.Thread(target=eat_breakfast, args=())         # Creating a thread
x.start()                                                   # Begin thread

y = threading.Thread(target=drink_coffee, args=())          # Creating a thread
y.start()                                                   # Begin thread

z = threading.Thread(target=study, args=())                 # Creating a thread
z.start()                                                   # Begin thread

#  Total Time Executed using these method: 5 Seconds because of the concurrent process\


# Making Thread Synchronization
x.join()
y.join()
z.join()
#  Total Time Executed using these method: Much slower because did a lot of time to wait around x,y and z to finish

print(threading.active_count()) # Count active threads in process
print(threading.enumerate())    # Make more than one threads run and take turns while one of them are idle
print(time.perf_counter())      # Count how long does it takes on calling the thread on to the main thread to finish


