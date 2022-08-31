from tkinter import *
from tkinter import ttk
#Tk is not having an update
root= Tk()
frame= Frame(root)
 
labelText = StringVar()
 
label=Label(frame,textVariable = labelText)
labelText.set('THis is a label')
 
button = Button(frame,text="click me")

label.pack()
button.pack()
frame.pack()

root.mainloop()