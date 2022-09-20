# Nested Function Calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function


# Initial Function
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)

print(num)

#Nested Function
print(round(abs(float(input("Now enter a new positive number: "))))) # Start with inner function and move on with the outer
