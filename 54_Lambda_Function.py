# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only have one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

#  Format = lambda parameters: expression

# Typical function calling:

def double(x):
    return x * 2

print(double(5))

# Lambda function calling

#  Single parameters
double = lambda x:x * 2
print(double(6))

# Multiple parametres (2)
multiply =  lambda x, y : x * y
print(multiply(2,3))

# Multiple parametres (3)
add = lambda x,y,z: x + y + z
print (add(5,6,7))

#  Passing strings
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Aiman","Fakhrullah"))

#  Check age
age_check = lambda age: True if age >= 18 else False
print(age_check(13))
print(age_check(18))