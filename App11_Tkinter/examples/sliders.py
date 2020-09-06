# Sliders
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *
 
root = Tk()
root.title("Sliders")
root.iconbitmap('examples/photos/icon.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

root.mainloop()