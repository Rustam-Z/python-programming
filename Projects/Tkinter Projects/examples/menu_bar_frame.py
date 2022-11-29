# Tuesday, July 19, 2020
# By RΨST-4M 🚀
# How to clear the screen after pressing the menu item? The answer is here!
# Create a Frame widget for each menu item and also -> hide_all_frames()
# EightSoft Academy

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Menu Bar")
root.iconbitmap('examples/photos/icon.ico')
root.geometry("400x400")

# Crate a Menu
my_menu = Menu(root)
root.config(menu=my_menu)


# Create a functions for commands
def command_file_new():
    """When you press File->New ... the following function code will work"""
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    Label(file_new_frame, text="it is just for checking New->File").pack()
    Button(file_new_frame, text="Test", command=testing).pack()


def testing():
    Label(file_new_frame, text="hello World").pack()


def command_edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    Label(edit_cut_frame, text="it is just for checking Edit->Cut").pack()


def command_copy():
    Label(root, text="it is just for checking").pack()


def hide_all_frames():
    """Clears the screen after pressing the menu item"""
    for widget in file_new_frame.winfo_children():
        widget.destroy()

    for widget in edit_cut_frame.winfo_children():
        widget.destroy()

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# Create a Menu Item "File"
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=command_file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a Menu Item "Edit"
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=command_edit_cut)
edit_menu.add_separator()
edit_menu.add_command(label="Question", command=command_copy)

# Create some frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")

# for running the program
root.mainloop()
