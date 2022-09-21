# copyfile() = copies content of file
# copy() = copyfile + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil 

shutil.copyfile ('text_sample.txt','copy.txt') # Format for shutil.copyfile(source,destination) 
                                               # Define the path of where do you want to make a copy
                                               # C:\\Users\\User\\Desktop\\copy.txt
                                               # The arguments for copy() and copy2() are the same
