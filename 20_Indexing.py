# Index operator [] = give access to a sequence's element (str,list,tuples)

name = "aiman Fakhrullah!"

# if(name[0].islower()):       # Check if aplhabet is lower form 
#    name = name.capitalize() # Change the capital is upper form

first_name = name[0:5].upper() # or name[:5]    # Change to Upper Form
last_name = name[6:].lower()                    # Change to Lower Form

last_character = name[-1] # Negative Indexing   # Print last character (L -> R: Positive Index, R -> L: Negative Index)

print(name)
print(first_name)
print(last_name)
print(last_character)