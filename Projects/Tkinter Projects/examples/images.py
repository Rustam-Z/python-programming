# Images, icons, and exit button

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('EightSoft Academy')

# For changing the icon
root.iconbitmap('examples/photos/icon.ico')

# images
my_img = ImageTk.PhotoImage(Image.open('examples/photos/image.jpg'))
my_label = Label(image=my_img)
my_label.pack()

# Exit Button
button_quit = Button(root, text="Exit program!", command=root.quit)
button_quit.pack()

root.mainloop()