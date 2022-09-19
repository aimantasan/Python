# Slicing = Create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

#Starting & Stop Index
name = "Aiman Fakhrullah"
# Start at index 0 but Stop at i = (last letter index of a word + 1)
# The Letter A is i=0 

first_name = name[0:6] # or name [:6] as compiler assume empty = 0 
last_name = name[6:17] # or name [7:] to assume all letter after that is same word

print(first_name)
print(last_name)

# Step Index
# How much to increase index value by between starting and stopping
# Default Step is 1 (Increase step by 1) A -> B -> C
#                   (Increase step by 2) A -> C -> E

funky_name = name[0:17:2] # or name[::2] assuming every letter with 2 Steps
print(funky_name)

#Reverse Substring in Python
reversed_name = name[::-1] #Counting Backwards
print(reversed_name)

# Slice String
# In index : were used but in slice , were used.

website1 = "http:://google.com"
website2 = "http:://wikipedia.com"

slice = slice(8,-4) # Can use Positive or Negative Indexing

print(website1[slice])
print(website2[slice])
