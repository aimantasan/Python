# if statement = a block of code that will execute if its condition is true

age = int(input("What is your age? :"))

if age >= 100: 
    print("You are a century old")
elif age >= 18:
    print ("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print ("You are a child!")