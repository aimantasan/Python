# Button  = you click on it, you got stuff

from tkinter import *

count = 0
def click():
    global count
    count +=1
    print(count)


window = Tk()
photo =PhotoImage(file='date.png')

button =Button(window,
                text = "Click Me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00ff00",
                bg="black",
                activeforeground="#ffffff",
                activebackground="red",
                state= ACTIVE, #ACTIVE by Default, Could be DISABLE
                image=photo,
                compound='bottom') 
button.pack()
window.mainloop()