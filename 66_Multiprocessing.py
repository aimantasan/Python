# Python Multiprocessing

# multiprocessing = runnning tasks in a parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage) -> Run multiple process at 1 thread
#                   multithreading = better for io bound tasks (waiting bound) -> Run at 1 thread at a time

from multiprocessing import Process, cpu_count
import time
from tkinter import E

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())                                                  # Get the number of additional processes that you could run

    a = Process(target= counter, args=(125000000,))                     # A single process took about 57 seconds
    b = Process(target= counter, args=(125000000,))                     # A double processes took about 40 seconds
    c = Process(target= counter, args=(125000000,))
    d = Process(target= counter, args=(125000000,))                     # 4 Processes took about 27 Seconds
    e = Process(target= counter, args=(125000000,))                     
    f = Process(target= counter, args=(125000000,))                     # If process created more than CPU count, the time to process increases
    g = Process(target= counter, args=(125000000,))                     # Technically its hindering the performance
    h = Process(target= counter, args=(125000000,))

    a.start()   # Start the process
    b.start()   
    c.start()   
    d.start()   
    e.start()   
    f.start()   
    g.start()   
    h.start()   

    a.join()    # Join function of the process to make process synchronization
    b.join()    
    c.join()    
    d.join()    
    e.join()    
    f.join()    
    g.join()    
    h.join()    

    print("Finished in: ", time.perf_counter()," seconds" )



if __name__ == '__main__': # This only applies for the usage of windows OS
    main()

