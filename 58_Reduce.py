# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
# Could also be done using for loop
# Format: reduce(function, iterable)

import functools    # Import functools module

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y : x + y ,letters)       # 1. reduce() applies function to first 2 elements within iterable
print (word)                                                # 2. Performs the function expression
                                                            # 3. Repeat process from the results from the previous expression
                                                            #    Example: "H","E","L","L","O"
                                                            #             "HE","L","L","O"
                                                            #             "HEL","L","O" and so on...
                                                            #  More like recycling the letteres and create a finished product

# Another Example:
factorial = [5,4,3,2,1]                                     # 5,4,3,2,1 
results = functools.reduce(lambda x,y: x*y, factorial)      # 20,3,2,1
print(results)                                              # 60,2,1
                                                            # 120,1
                                                            # 120