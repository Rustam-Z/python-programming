# July 16, 2020 12:15 PM
# Frames
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *

root = Tk()
root.title("Frames")
root.iconbitmap('examples/photos/icon.ico')

frame = LabelFrame(root, padx=5, pady=5) # inside # we can add -> text="My Frame", 
frame.pack(padx=10, pady=10) # outside

button = Button(frame, text="Click me!").pack()

root.mainloop()