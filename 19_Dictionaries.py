# Dictionary = A changeable, unordered collectionof unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals["Russia"])   # Print a key from a dictionary

print(capitals.get("Germany")) # Check if a key is in dictionary (Much safer way, with no errors)

print(capitals.keys())   # Print all the keys in the dictionary
print(capitals.values()) # Print all the values in the dictionary
print(capitals.items())  # Print everything in the dictinary

capitals.update({"Germany":"Berlin"}) # Update new kwy with new value
capitals.update({"USA":"Las Vegas"})  # Update existing key with new values

capitals.pop("China") # Remove a key and values
capitals.clear()      # Clear Dictionary

for key,value in capitals.items():
    print("The capital of " + key + " is " + value ) # Print entire dictionary
