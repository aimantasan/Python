# Radio button - similar to checkbox, but you can only select one from a group

from tkinter import *

date =  ["1/1/20","2/2/22","5/7/90"] 
def order():
    if(x.get()==0):
        print("You set at 1/1/20")
    elif(x.get()==1):
        print("You set at 2/2/22")
    elif(x.get()==2):
        print("You set at 5/7/90")
    else:
        print("huh?")

window = Tk()
photo = PhotoImage(file='date.png')

# if theres multiple images:
# dateImages = [image1,image2,image3]

x = IntVar()

for index in range(len(date)):  
    radiobutton = Radiobutton(window,
                              text=date[index], # add text to radio button
                              variable= x,      # groups radiobuttons together if they share the same variable 
                              value=index,       # assigns each radiobutton a different value
                              padx= 25,          # adds padding on x-axis
                              font= ("Impact",50),
                              image = photo,    # if multiple dateImage[index] # Addimages to radio button
                              compound= 'left', # adds image & text (on left side)
                              indicatoron= 0,    # eliminate circle indicators
                            # width = 400       # Set width of radio buttons
                              command= order # set command of radiobutton to function
                              )      
    radiobutton.pack(anchor=W)
window.mainloop()