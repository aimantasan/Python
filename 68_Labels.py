# Label =  an area widget that holds text and/or an image within a window

from cgitb import text
from tkinter import RAISED, Label, PhotoImage, Tk


window = Tk()                   # Creating window that acts as container

photo = PhotoImage(file='date.png') # Defining Location of a file must include \\ as \ would be escaping a string

# Defining and instantiating label  
label = Label(window,
              text = "Hello World",
              font=('Arial',40,'bold'),
              fg='#00FF00',     # The color could be defined by hex, name
              bg='black',
              relief=RAISED,    # Border Style : RAISED,SUNKEN
              bd = 10,           # Make the border more visible
              padx= 20,          # Padding on X
              pady= 10,          # Padding on Y
              image=photo,       # Defining the image with the called PhotoImage()
              compound='bottom'  # Define which layer that the image will be called: top,left,right
              )          

                            
label.pack()                # Pack place widget in the center of the window
#label.place(x=0,y=0)       # Place label at anywhere in the widget

window.mainloop()