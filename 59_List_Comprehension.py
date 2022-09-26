# list comprehension = a way to create a new list with less syntax
#                      can mimic with certain lambda functions, easier to read
#                      list = [expression for item in iterable]

#  Example for simple expression
squares = []                # Create an empty list
for i in range(1,11):       # Create a for loop
    squares.append(i*i)     # Insert new elements for square list in each iteration (Define what to do for each loop)
print(squares)

#  Example for list comprehension
squares = [i*i for i in range(1,11)]        # list = [(expression) for (item) in (iterables)]
print(squares)

#  Example for lambda functions
students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x:x >= 60, students))      # Filter function in lambda and create data on a list
print(passed_students)

#  Example for lambda functions using list comprehension
#  Find for score > 60
passed_stud = [i for i in students if i >= 60]             # list = [(expression) for (item) in (iterables) if (conditional)]
print(passed_stud)

#  Find for score < 60 and change data to "Failed"
passed_stud = [i  if i >= 60 else "Failed" for i in students]             # list = [(expression) for (item) in (iterables) if (conditional)]
print(passed_stud)