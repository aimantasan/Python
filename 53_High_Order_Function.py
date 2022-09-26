# High Order Function = A function thet either:
#                       1. Accepts a function as an Argument
#                       2. Returns a function
#                       (In python, functions are also treated as objects)

#  Example 1: Accepts function as Argument
def loud(text):
    return text.upper() 

def quiet(text):
    return text.lower()

def hello(func):        # Passing function as Argument
    text = func("Hello")
    print(text)

hello(loud)             # Passing function as Argument
hello(quiet)            # Passing function as Argument

# Example 2: Returns a Function
#  Situation: dividend / divisor = quotient

def divisor(x):         # Example:  1. Divisor is assigned with the value 2
    def dividend(y):    #           2. The inner function are skipped first (Not yet called)
        return y/x
    return dividend     #           3. The dividend are returned

divide = divisor(2)     #           4. The dividend are assigned as variable
print(divide(10))       #           5. The variable are called as it have the same memory as the function, value 10 is inserted for dividend

                        #           6. y = 10 and x = 2, return y/x = 5
