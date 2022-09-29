import time                     # For further exploration, refer here: https://docs.python.org/3/library/time.html

print(time.ctime(0))            # Convert a time expressed in seconds since epoch to a readable string
                                # epoch = when your computer thinks time began (reference point)

print(time.time())              # Return current seconds since epoch
print(time.ctime(time.time()))  # Get current Time

# Time Object is a struct, made up of different keyword arguments

# time.strftime(format,time_object)     # Formats a time objects to a string
# time_object = time.local_time()       # Local Time
# time_object = time.gmtime()           # UTC Time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)


# Take a string an parse it into time object
# time_string = "20 April, 2020"
# time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# Asc Time Function: Accepts a tuple representation of a relative time
# time_tuple = (2020,4,20,4,20,0,0,0,0)
# time_string = time.asctime(time_tuple)
# time_string = time.mktime(time_tuple)     # Take tuple time objects ands converts into seconds
# print(time_string)