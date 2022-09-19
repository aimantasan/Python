#Logical Operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside? :"))

#Condition 1 (and,or)
if temp >= 0 and temp <= 30: # Both conditions need to be true
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30: # Either one conditions need to be true
    print ("The temperature is bad today!")
    print ("Stay Inside!")

#Condition 2: (not) not is inversed. False = True & True = False
if not(temp >= 0 and temp <= 30): # Both conditions need to be true
    print ("The temperature is bad today!")
    print ("Stay Inside!")

elif not(temp < 0 or temp > 30): # Either one conditions need to be true
    print("The temperature is good today!")
    print("Go outside!")

