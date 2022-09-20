# List = used to store multiple items in a single variable

food = ["pizza","hamburgers","hotdog","spagetthi","pudding"]

food[0] = "sushi"
#print(food[0]) # Print based on index elements

food.append("ice cream") # Insert new elements
food.remove("hotdog")    # Remove an element
food.pop()               # Remove the last elements
food.insert(0,"cake")    # Insert new elements at certain index
food.sort()              # Sort elements alphabetically
food.clear()             # Remove all elements in a list

for x in food:
    print(x)
