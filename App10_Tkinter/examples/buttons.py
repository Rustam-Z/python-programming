# By RΨST-4M 🚀

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="I clicked a Button!",)
    myLabel.pack()

myButton=Button(root, text="Click me!", command=myClick, fg="blue", bg="yellow")
myButton.pack()

# Button's arguments
# state=DISABLED
# size: padx=50, pady=50
# text color: fg="blue", 
# command=myFunction

root.mainloop()