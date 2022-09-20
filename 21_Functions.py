# Function = a block of code which is executed only when its called.

def hello(name): # Add parameter into function, A temporary function for variable
    print("Hello " + name +" ! This is the first function from Python")
    print("Have a nice day !")

my_name = "Aiman Fakhrullah"
hello(my_name) # Call Function # function(arguments)


def hi(first_name, last_name, age): # Inserting multiple arguements into functions
    print("Welcome back "+ first_name + " " + last_name + " ")
    print("You are now " + str(age) + " years old.")

hi("Alex","Toshiro", 23)

# Functions must be called at the end
# Number of arguements must matches the stated arguments