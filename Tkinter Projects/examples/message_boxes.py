# July 16, 2020 11:38 PM
# Message Boxes
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("MessageBox")
root.iconbitmap('examples/photos/icon.ico')

def popup():
    response = messagebox.askquestion("This is my pupup!", "hello world")
    Label(root, text=response).pack()
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    if response=="yes":
        Label(root, text="You pressed Yes!").pack()
    else:
        Label(root, text="You pressed No!").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()