import os

source = "text_sample.txt " # Could be a directory (folder)
destination = "C:\\Users\\User\\Desktop\\text_sample.txt" # \\ because \ is an escape sequence for string

try:
    if os.path.exists(destination):      # Check if the file exists in the destination so that you don't save over it
        print("There is already a file there")
    else:                                # Move the file to a new destination
        os.replace(source,destination)
        print(source + "was moved")

except FileNotFoundError:                # Make an exeption on the file
    print(source+ " was not found")