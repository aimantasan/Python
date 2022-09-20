# Loop Control Statements = change a loop execution from its normal sequence

# break    = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass     = does nothing, acts as a placeholder

#while True: # Break Statement
#    name = input("Enter your name: ")
#    if name != "":
#        break

#phone_number = "012-345-6789" # Continue Statement

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

for i in range(1,21):   # Pass Statement
    if i == 13:
        pass
    else:
        print(i, end="")