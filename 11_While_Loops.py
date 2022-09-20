# While Loop = a statement that will execute it's block of code
#              as long as it's condition remain true

# Infinite Loop
# while 1==1:
#    print("Help! I'm stuck in a loop")

name = "" # or name = None

while len(name) == 0: # or while not name:
    name = input("Enter your name: ")

print ("Hello " + name)


