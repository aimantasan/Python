#text = "Yaww whats up\n I'm writing a file by using code!\n" # Changing this will overwrite the whole file
text = "Have a nice day\n See You\n" # Use this when changing to a (append)

with open('text_sample.txt','w') as file: # Format open('File Name','w (write mode) or a (append/update)')
    file.write(text)