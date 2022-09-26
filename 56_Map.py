# map() = applies a function to each item in an iterable (list, tuple, etc.)
# 
# format: map(function,iterable)

# Iterable : Could be in a form of list, tuple, etc
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1] * 0.82)       # Assign variable to_euros data list at index = 0, index = 1 for prices
to_dollars = lambda data: (data[0],data[1] / 0.82)       # Assign variable to_euros data list at index = 0, index = 1 for prices


store_euros = list(map(to_euros,store))                 # list() -> Converts map into a list   # map(to_euros, store) calling the map function
store_dollars = list(map(to_dollars,store))                 # list() -> Converts map into a list   # map(to_euros, store) calling the map function

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)