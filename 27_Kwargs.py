#  **kwargs = parameter that will pack all arguments into a dictionary
#             useful so that a function can accept a varying amount of keyword arguments
# **kwargs naming convention : **name, the ** define the kwargs (**kwargs is common)

# Useable Situation
# def hello(first,last):
#     print("Hello " +  first + "" + last)

# hello(first="Aiman",middle="Fakhrullah",last="Mantasan") # Expected error as 'middle' is undefined and unexpected

# Solution

def hello(**kwargs):
    # print("Hello" + kwargs["first"] + " " + kwargs["last"])

    print("Hello",end= " ") # Example of fetching up args data from kwargs dictionary (array).
    for key,value in kwargs.items():
        print(value, end =" ")

hello(title = "Mr.", first="Aiman",middle="Fakhrullah",last="Mantasan") 
        # No error expected as 'middle' has been save in memory

# Every arguments are addable as long as it is stored in the kwargs dictionary (array)