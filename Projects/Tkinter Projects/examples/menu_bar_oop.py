import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedStyle
import os


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent

        teachers_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=teachers_menu)
        teachers_menu.add_command(label="Press-1", underline=1, command=self.press1)

        groups_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="New", underline=0, menu=groups_menu)
        groups_menu.add_command(label="Press-2", underline=1, command=self.press2)

    def press1(self):
        p1 = ttk.Label(self.parent, text="Press-1")
        p1.pack()

    def press2(self):
        p2 = ttk.Label(self.parent, text="Press-2")
        p2.pack()

    def quit(self):
        sys.exit(0)


class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self)
        self.parent = parent

        menubar = MenuBar(self)
        self.config(menu=menubar)


if __name__ == "__main__":
    app = App(None)
    app.title("AutoRoad")
    app.geometry("400x400")
    style = ThemedStyle(app)
    style.set_theme("breeze")
    app.mainloop()
