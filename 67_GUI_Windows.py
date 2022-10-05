from tkinter import *   # From GUI Toolkit

#  Widgets = GUI elements: buttons, textboxes, labels, images
#  Windows = Serves as a container to hold or contain these widgets

# Creating a simple window

window = Tk()                           # Instantiate an instance of a window
window.geometry("420x420")              # Set screen resolution, no space.
window.title("My First GUI Program")

# Replacing the Icon
icon = PhotoImage(file='date.png')      # Must be in PNG
window.iconphoto(True,icon)             # Set to true and place the variable name
window.config(background="black")       # Either put the color name or put in hex values

window.mainloop()                       # Display our window on our computer screen, lissten for events