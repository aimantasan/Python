# *args = parameter that will pack all arguments into tuple
#         useful so that a function can accept a varying amount of arguments

def add(*stuff):         # Instead of defining a numbers of arguments, *args will determine the arguments
    sum = 0              # *args naming convention : *name, the * define the args (*args is common)

    stuff = list(stuff)  # Example: Making a list so it could be changeable and mutable
    stuff[0] = 0         # Data to change

    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7)) # Output = 27 as index 0 was changed from 1 to 0