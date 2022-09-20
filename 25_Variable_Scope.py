#  Scope = The region that a variable is recognised
#          A variable is only available from inside the region it is created.
#          A global and locally scoped versions of a variable can be created.

name = "Aiman" # Global Scope / Global Variable (Available throughout the module or this file)
               # (inside and outside the functions)

def display_name(): 
    name = "Fakhrullah" # Local Scope/ Local Variable (Available and defined only inside this function)
    print(name)

print(name)     # Will fetch from only the Global Variable / Global Scope
display_name()  # Will fetch from the Local variable / Local Scope

# def display_name():  # If none of the local variables are defined, Python will fetch from Global Scope / Global Variable
#    print(name)
# Output: Aiman

# How Python read variables (L -> E -> G -> B)
# L : Local (Defined in created functions)
# E : Enclosing (Defined in the function that was enclosed within)
# G : Global (Defined in the module / file)
# B : Built-in (Already built-in with Python)