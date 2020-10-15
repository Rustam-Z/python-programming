from tkinter import *
from PIL import ImageTk, Image

# Main Window
root = Tk()
root.title("Image Viewer")
root.iconbitmap('examples/photos/icon.ico')

# Images location
img1 = ImageTk.PhotoImage(Image.open("examples/photos/python.png"))
img2 = ImageTk.PhotoImage(Image.open("examples/photos/python-file.png"))
img3 = ImageTk.PhotoImage(Image.open("examples/photos/python-file-1.png"))
img_list = [img1, img2, img3]

# Labels & Status bar in footer
my_label = Label(image=img1)
status = Label(root, text="Image 1 of " +  str(len(img_list)), relief=SUNKEN, anchor=E,
               font=("times new roman", 10))

# Functions for << and >>
def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_num+1),
                            font=("times new roman", 15), bg="black", fg="white")

    button_back = Button(root, text="<<",command=lambda: back(img_num-1),
                         font=("times new roman", 15), bg="black", fg="white")

    # cheaking for the last image
    if img_num == len(img_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    # footer - status bar
    status = Label(root, text="Image "+str(img_num) + " of " + str(len(img_list)), relief=SUNKEN, anchor=E,
                   font=("times new roman", 10))
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(img_num):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_num+1),
                            font=("times new roman", 15), bg="black", fg="white")
    button_back = Button(root, text="<<", command=lambda: back(img_num-1),
                         font=("times new roman", 15), bg="black", fg="white")

    # cheaking for the last image
    if img_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # footer - status bar
    status = Label(root, text="Image "+str(img_num) + " of " + str(len(img_list)), relief=SUNKEN, anchor=E,
                   font=("times new roman", 10))
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


# Buttons
button_quit = Button(root, text='Exit Program',
                    font=("times new roman", 15), command=root.quit, bg="black", fg="white")
button_back = Button(root, text="<<", command=back, state = DISABLED, 
                    font=("times new roman", 15), bg="black", fg="white")
button_forward = Button(root, text=">>", command=lambda: forward(2),
                    font=("times new roman", 15), bg="black", fg="white") 


# Showing on Window
my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# sticky is a line like ---------------------------
# anchor is the location 

root.mainloop()