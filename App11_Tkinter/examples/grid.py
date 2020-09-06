from tkinter import *

window = Tk()

# to rename the title of the window window.title("GUI")
window.title("GUI")
# pack is used to show the object in the window

label = Label(window, text="Hello World!").grid(row=0, column=0)
label2 = Label(window, text="   Hello World!").grid(row=1, column=1)

# for running the program
window.mainloop()