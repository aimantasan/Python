# Exception = events detected during execution that interupt the flow of a program

try: # Try will be surrounding any code that is considered dangerous
     numerator = int(input("Enter a number to divide: "))
     denominator = int(input("Enter a number to divide by: ")) # If a division by 0 occurs, an error will be prompt
     result = numerator/denominator
except ZeroDivisionError as e: #Exception blocks will catch Zero Division
    print(e) # e is to Print the exception or cause of exception to be triggered
    print("You cannot divide by 0! Baka!")
except ValueError as e:        #Exception blocks will catch Value Error (example: only number are allowed)
    print("Enter only number")
except Exception as e:         #Exception blocks will catch all exceptions
    print("Something went wrong")
else:   # Else could be put here if all the exceptions were not being able to catch
    print(result)
finally: # To be put wether an exception is catched or not (will execute all, mostly opens file)
    print("This will always execute")

   
# Not a good practice tom have a single except block to handle all exceptions