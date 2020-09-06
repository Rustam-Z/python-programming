# Open Files Dialog Box
# By RΨST-4M 🚀
# EightSoft Academy

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

def open():
    global my_image # we always need global to open an image  
    root.filename = filedialog.askopenfilename(initialdir="examples/photos", title="Select a File", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))
    my_label = Label(root, text=root.filename).pack() # it returns the location of file as string

    my_image = ImageTk.PhotoImage(Image.open(root.filename)) 
    my_image_label = Label(root, image=my_image).pack()

     
my_btn = Button(root, text="Open file", command=open).pack()

mainloop()