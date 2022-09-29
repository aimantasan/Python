# if __name__ == '__main__'

# 1. Modules can be run as a standalone program
# 2. Modules can be imported ad used by other modules

# Python interpreter sets "Special Variables", one of which is __name__ 
# then Python will execute the code found within __main__

# Python will assign the __name__ variable a value of '__main__' if its the initial module being run

# Before run: Change the name of 62_If__name__ == '__main__'.py to module_one.py

# Example is in module two

def hello():                                    # Defining variables to be accessed at Module Two
    print("Hello")                                      

#  The main function, main() could also be written in these

if __name__ == '__main__':
    print("running this module directly")       # If you run in module_one.py
    hello()                                     # Could be called here since module one cannot be run as a standalone program
else:
    print("running this module indirectly")     # If you run in module_two.py

