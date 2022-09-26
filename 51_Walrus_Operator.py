#  Walrus operator :=

# New for python 3.8
# Assignment expression aka walrus operator
# Assigns value to variables as part of a larger expression

# Example for using walrus operator:
# happy = True # Standard calling method
# print(happy)

# print(happy := False) # Call using walrus operator

foods = list()

# while True:
#     food = input("What food do you like?")
#     if food == "quit":
#         break
#     foods.append(food)

while food := input("What food do you like?") != "quit": # Same line of code as above
    food.append(food)
