import tkinter as tk
import time
from PIL import Image, ImageTk


class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Xabar")
        self.geometry("400x400+480+200")
        tk.Label(self, text="Kuting, ma'lumotlar bazasi yuklanmoqda.").pack()
        

        ## required to make window show before the program gets to the mainloop
        self.update()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
        ## simulate a delay while loading
        time.sleep(6)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

if __name__ == "__main__":
    app = App()
    app.mainloop()