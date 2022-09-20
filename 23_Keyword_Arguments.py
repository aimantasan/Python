# Keyword Arguments = Arguments preceded by an identifier when we pass them to a function
#                     The order of the arguements doesn't matter, unlike positional arguements
#                     Python knows the names of the arguments that our function receives

def hello(first,middle,last):
    print("Hello! " + first+ " " + middle+ " "+ last)

hello(middle = "Fakhrullah", last = "Mantasan", first = "Aiman") # Identify and Associate each of the arguments