# July 17, 2020 8:50 AM
# New Window popups
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("New Window")
root.iconbitmap('examples/photos/icon.ico')

def open():
    global my_image
    def popup():
        response = messagebox.askquestion("Print", "Do you want to print?")
        if response=="yes":
            Label(root, text="It is printing!").pack()
        else:
            Label(root, text="You pressed No!").pack()

    # Top Level Window
    top = Toplevel()
    top.title("Python Image")

    my_image = ImageTk.PhotoImage(Image.open("examples/photos/python-file-1.png"))
    my_label = Label(top, image=my_image).pack()
    Button(top, text="Print out", command=popup).pack()


btn = Button(root, text="Open the excel file of ... ...", command=open).pack()


mainloop()