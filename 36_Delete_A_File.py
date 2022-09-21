import os
import shutil

path = "delete_text.txt" # or path C:\\Users\\User\\Desktop\\delete_text.txt or path = "folder" 
                         # Create delete_text.txt before execute

try:
    os.remove(path)     # To remove file
    #os.rmdir(path)     # To remove a folder
    #shutil.rmtree(path) # To remove a folder that contains files (Proceed with caution)
    

except FileNotFoundError: # Exception on file not found
    print("That file was not found")
except PermissionError:
    print("You did not have the permission to delete that")

else:
    print(path + " was deleted")



