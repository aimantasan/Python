import module_one           # Importing another module from 62_If__name__ == '__main__' (change the file name first to module one)

print(__name__)             # Checking the __name__ in module name, it will fetch the name as main


print(module_one.__name__)  # Checking the __name__ in module one
module_one.hello()          # Accessing Module One function from Module Two