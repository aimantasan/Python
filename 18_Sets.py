# Set = Collection which is unordered, unindexed. No duplicate value

utensils = {"fork","spoon","knife"} # Eventhough there are multiple data that have the same value, sets will fetch only one
dishes = {"bowl","plate","cup","knife"}

# utensils.add("napkin")  # Add new elements
# utensils.remove("fork") # Remove elements
# utensils.clear()        # Clear all elements
# utensils.update(dishes)  # set1.update(set2), make the 1st set updated with the data from the 2nd set

# dinner_table = utensils.union(dishes) # Union the sets (Make all elements in different sets together)

#for x in dinner_table:
#    print(x)

print(utensils.difference(dishes)) # Print what utensils have that dishes doesnt, what is the difference of set1 and set2
print(utensils.intersection(dishes)) # Print what they have in common