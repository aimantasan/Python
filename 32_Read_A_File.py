
try: # Try run all codes
    with open("text_sample.txt") as file: # Insert the file name or the path. #C:\\Users\\User\\Desktop\\text_sample.txt
    
        print(file.read()) # This will automatically closed the file after opening it
        print(file.closed) # Check if the file is closed after execution

except FileNotFoundError: # Exception will catch error if file does not exist
    print("File Does Not Exist")
    print("Check your spelling before executing")
