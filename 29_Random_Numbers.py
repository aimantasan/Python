import random

x = random,random.randint(1,6) # Random int within range
print(x)

y = random.random ()           # Random decimal
print(y)

myList = ['rock','paper','scissors'] # Fetch random values from list
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"] # Shuffle List
random.shuffle(cards)
print(cards)