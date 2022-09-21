from genericpath import isfile
import os

# Check if file exists on computer

file_path = "C:\\Users\\User\\Desktop\\31_File_Detection.txt"       # \\ because \ is an escape sequence for a string
                                                                    # The path is based on where did you put your file

folder_path = "C:\\Users\\User\\Desktop\\31_File_Detection_Folder"  # Same goes with folder

if os.path.exists(file_path):        # Check if file exist in path
    print("That location exist")

    
    if os.path.isfile(file_path):    # Check if the path contains file
        print("That is a file")
    elif os.path.isdir(file_path):   # Check if path is directory (Later change the file_path to folder_path)
        print ("That is a directory")
else:
    print("That location does not exist")
    