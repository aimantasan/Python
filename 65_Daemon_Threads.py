# Daemon Thread = a thread that runs in background, not for important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non daemon threads cannot normally be killed, stay alive until task is completed

#                 ex. background tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ",count,"seconds")

x = threading.Thread(target=timer, daemon=True)
print(x.isDaemon())
x.start()

# x.setDaemon(True) # To set a daemon


answer = input("Do you wish to exit?")