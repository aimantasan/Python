# sort() method = used with lists
# sort() function = used with iterables

# Level 1
students = ["Squidward","Patrick","Sandy","Spongebob","Mr. Krabs"]  # If the list is Tuple (), then it does not work

# sort() method
students.sort()                     # Sort in Alphabetical Orders
students.sort(reverse=True)         # Sort in Reverse Alphabetical Orders

for i in students:  # Calling the lists
    print(i)

# sort() function                                 # Returns as a list but return an iterable as an arguments
sorted_students = sorted(students)                # Sort in Alphabetical Orders
sorted_students = sorted(students, reverse=True)  # Sort in Reverse Alphabetical Orders

for i in students:  # Calling the lists
    print(i)

# Level 2
#  Lists of Tuples [()]
pelajar = [("Squidward","F",60), # This somehows resembles as spreadshhet
           ("Sandy","A",33),
           ("Patrick","D",36),
           ("Spongebob","B",20),
           ("Mr. Krabs","C",78)]


pelajar.sort()                                              # Sort in Alphabetical Orders

grade = lambda grades:grades[1]                             # Defining that the variable grades are in index = 1, Index begins at 0
pelajar.sort(key = grade)                                   # Sort in Alphabetical Orders but using key to determine on other column
                                                            # Keyword argument, return the index of the targeted column

pelajar.sort(key = grade,reverse=True)                      # Sort in Reversed Alphabetical Orders but using key to determine on other column
                                                            # Keyword argument, return the index of the targeted column

for i in pelajar:  # Calling the lists
    print(i)

# Making an example for Ages
age = lambda ages:ages[2]
pelajar.sort(key = age)
pelajar.sort(key = age,reverse=True) 

for i in pelajar:  # Calling the lists
    print(i)


#  Example for tuple of tuples
sorted_students  = sorted (students, key=age)

for i in students:  # Calling the lists
    print(i)
