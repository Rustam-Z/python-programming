# Read more at: https://pythonprogramming.altervista.org/tkinter-show-the-files-in-the-folder-in-a-listbox/
# EightSoft Academy
# You must be in the same directory in which you have include the project

import tkinter as tk
import os

# WINDOW CREATION
win = tk.Tk()
geo = win.geometry
geo("400x400+400+400")
win['bg'] = 'orange'

# get the list of files
f_list = os.listdir()

l_box = tk.Listbox(win)
l_box.pack()

# THE ITEMS INSERTED WITH A LOOP
for item in f_list:
    l_box.insert(tk.END, item)

def show_content(event):
    x = l_box.curselection()[0]
    file = l_box.get(x)
    with open(file) as file:
        file = file.read()
    text.delete('1.0', tk.END)
    text.insert(tk.END, file)


text = tk.Text(win, bg='cyan')
text.pack()

l_box.bind("<<ListboxSelect>>", show_content)

win.mainloop()