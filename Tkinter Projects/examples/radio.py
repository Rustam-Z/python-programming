# July 16, 2020 12:41 PM
# Radio Button
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *
 
root = Tk()
root.title("Frames")
root.iconbitmap('examples/photos/icon.ico')

r = IntVar()
r.set(1) # default

def clicked(value):
    myLabel = Label(root, text=value).pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

label = Label(root, text=r.get()).pack(anchor=W)
myButton = Button(root, text="Click me!", command=lambda: clicked(r.get())).pack()

root.mainloop()