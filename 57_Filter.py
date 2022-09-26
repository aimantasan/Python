# filter() = creates a collection of elements from an iteratable for which a function returns
# Basically like a search results that meet a criteria
# format: filter(function, iterable)

# Iterable: Could in form of Tuples, List, etc.

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18                    # Checks data for age 18 and above using lambda at index = 1

drinking_buddies = list(filter(age,friends))       # Filter will return the data that has the listed conditions  # list() -> Put iterable in list

for i in drinking_buddies:
    print(i)