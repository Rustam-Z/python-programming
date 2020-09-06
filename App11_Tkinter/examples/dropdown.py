from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("DropDown")
root.geometry("400x400")

# Drop Down Boxes

clicked = StringVar()
clicked.set("1")

OPTIONS = [
    "1", "2", "3", "4", "5",
]

def show():
    Label(root, text=clicked.get()).pack()

drop = OptionMenu(root, clicked, *OPTIONS).pack()
my_button = Button(root, text="Show selection", command=show).pack()

root.mainloop()