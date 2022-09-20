# Tuple = Collection which is ordered and unchangeable
#         used to group together related data

student = ("Aiman",23,"Male")

print(student.count("Aiman")) # Count how many the value Aiman appears

print(student.index("Male")) # Show the index position of the given data

for x in student:
    print(x)

if "Aiman" in student:
    print("Aiman is found !")