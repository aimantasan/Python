from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

windows = Tk()

scale = Scale(windows,
              from_ = 100,
              to= 0,
              length=600,
              orient=VERTICAL, #HORIZONTAL # Orientation of scale
              font = ('Consolas',20),
              tickinterval=10, # adds numiric indicators for value
              showvalue=0, # Hide current value
              resolution= 5, # increment of slider
              troughcolor= '#69EAFF',
              fg='#FF1C00'
              )
scale.set(((scale['from'] - scale['to'])/2) + scale ['to'])
scale.pack()

button = Button(windows,text='submit',command=submit)
button.pack()
windows.mainloop()