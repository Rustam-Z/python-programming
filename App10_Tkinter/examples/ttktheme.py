# pip install ttktheme
# Tuesday, July 19, 2020
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

root = ThemedTk(theme="breeze")
root.title("Menu Bar")
root.iconbitmap('examples/photos/icon.ico')
root.geometry("400x400")

# Crate a Menu
my_menu = Menu(root)
root.config(menu=my_menu)


# Create a functions for commands
def command_new():
    """When you press File->New ... the following function code will work"""
    ttk.Label(root, text="You Clicked New ...").pack()


def command_cut():
    ttk.Label(root, text="Awesome, it is working!").pack()


def question():
    response = messagebox.askquestion("Question", "Do you liked Menu Bars?")
    if response == "yes":
        ttk.Label(root, text="Ugh!!!").pack()
    else:
        ttk.Label(root, text="Sorry ...").pack()


def command_copy():
    ttk.Button(root, text="Popup", command=question).pack()


# Create a Menu Item "File"
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=command_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a Menu Item "Edit"
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Ask", menu=edit_menu)
edit_menu.add_command(label="Press me :)", command=command_cut)
edit_menu.add_separator()
edit_menu.add_command(label="Question", command=command_copy)


# for running the program
root.mainloop()
