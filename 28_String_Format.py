# str.format() = optional method that gives users more control when displaying output

# Usable Situation

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)

# The string format
print("The {} jumped over the {}".format(animal, item))   # Format fields : Act as an placeholder for variable
print("The {1} jumped over the {0}".format(animal, item)) # Positional Arguments (Define position based on index number)
print("The {haiwan} jumped over the {barang}".format(haiwan = "sheep", barang = "barn")) # Keyword Arguments

# Positional and Keyword Arguments could be reused: {1} {1}, {animal} {animal}

# Store string within a variable
text = "The {} jumped over the {}"
print (text.format(animal,item))

# Add padding to a string
name = "Aiman"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))  # Add Padding
print("Hello, my name is {:<10}. Nice to meet you".format(name)) # Left Align Value
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # Right Align Value
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # Center Align Value

# How to align if there positional or keyword arguments?
print("Hello, my name is {nama:10}. Nice to meet you".format(nama ="Alex"))  # Add Padding

# Formatting numbers
number = 3.14159
print("The number pi is {:.2f}".format(number)) #.2f defines 2 floating point numbers, it could be (n)f and it rounds number

numero = 1000
print("The number pi is {:,}".format(numero))   # Will add , to thousands place
print("The number pi is {:b}".format(numero))   # Make binary representation of numbers
print("The number pi is {:o}".format(numero))   # Make octal representation of numbers
print("The number pi is {:X}".format(numero))   # Make hexadecimal representation of numbers(could be lower or upper casing)
print("The number pi is {:E}".format(numero))   # Make scientific notation (could be lower or upper casing)