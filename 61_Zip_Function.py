# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, set, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Aiman","Alexander","Mantasan"]    # List of usernames 
password = ("p@SSw0rD","abc123","guest")        # Tuples of password
login_date = ["1/1/21","1/2/21","1/3/21"]

# Goal: Zip elements from each iterable together so that they're in pairs
#       Each pairs would be stored as tuple within a zip object

# users = zip(usernames,password,login_date)    # Pairs the username and password together as a tuple ('usernames','password')
# users = list(zip(usernames,password))         # Could also be changed to other iterables, put list(zip())
users = dict(zip(usernames,password))           # Make into a dictionary (Changing to other iterables)

print(type(users))                              # Check what type is the user variable. (A zip, obviously)

for key,value in users.items():                 # Print out the outcome
    print(key + ":" + value)



users = zip(usernames,password,login_date)      # Making a zip with 3 iterables

for i in users:
    print(i)
