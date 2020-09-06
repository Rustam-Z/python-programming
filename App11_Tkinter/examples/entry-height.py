from tkinter import *

root = Tk()
root.geometry('400x400')


def my_click():
    hello = "Hello " + e.get()
    label = Label(root, text=hello)
    label.pack(pady=10)


e = Entry(root, width=30).pack(pady=30, ipady=10, ipadx=50)

btn = Button(root, text="Enter your name", command=my_click)
btn.pack(pady=10)

root.mainloop()
