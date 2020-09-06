import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedStyle
import os


class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        self.frame = ttk.Frame(master)
        self.frame.pack()

        self.master = master

        # Create a Menu Item for Teachers
        teachers_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Groups
        groups_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Students
        students_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Info --EightSoft dev
        info_menu = tk.Menu(self, tearoff=False)

        # Add the cascades for menu bar
        self.add_cascade(label="Укитувчи", menu=teachers_menu)
        self.add_cascade(label="Гуруҳ", menu=groups_menu)
        self.add_cascade(label="Укивчилар", menu=students_menu)
        self.add_cascade(label="Инфо", menu=info_menu)

        # Teachers
        teachers_menu.add_command(label="Кошиш", command=self.teachers_add)
        teachers_menu.add_command(label="Янгилаш", command=self.teachers_edit)
        teachers_menu.add_command(label="Учириш", command=self.teachers_delete)

        # Groups
        groups_menu.add_command(label="Кошиш", command=self.groups_add)
        groups_menu.add_command(label="Янгилаш", command=self.groups_edit)
        groups_menu.add_command(label="Учириш", command=self.groups_delete)

        # Students
        students_menu.add_command(label="База", command=self.students_db)

        # Info
        info_menu.add_command(label="Дастур хакида малумот", command=self.info_about)
        info_menu.add_separator()

        # Create frames for each new window --MenuBar-Cascade-Commands
        self.teachers_add_frame = ttk.Frame(master)
        self.teachers_edit_frame = ttk.Frame(master)
        self.teachers_delete_frame = ttk.Frame(master)

        self.groups_add_frame = ttk.Frame(master)
        self.groups_edit_frame = ttk.Frame(master)
        self.groups_delete_frame = ttk.Frame(master)

        self.students_db_frame = ttk.Frame(master)

        self.info_about_frame = ttk.Frame(master)

    # Hide the frames when you switch the menu
    def hide_all_frames(self):
        """Cleans the screen after pressing the menu item"""
        for widget in self.teachers_add_frame.winfo_children():
            widget.destroy()

        for widget in self.teachers_edit_frame.winfo_children():
            widget.destroy()

        for widget in self.teachers_delete_frame.winfo_children():
            widget.destroy()

        for widget in self.groups_add_frame.winfo_children():
            widget.destroy()

        for widget in self.groups_edit_frame.winfo_children():
            widget.destroy()

        for widget in self.groups_delete_frame.winfo_children():
            widget.destroy()

        for widget in self.students_db_frame.winfo_children():
            widget.destroy()

        for widget in self.info_about_frame.winfo_children():
            widget.destroy()

        self.teachers_add_frame.pack_forget()
        self.teachers_edit_frame.pack_forget()
        self.teachers_delete_frame.pack_forget()
        self.groups_add_frame.pack_forget()
        self.groups_edit_frame.pack_forget()
        self.groups_delete_frame.pack_forget()
        self.students_db_frame.pack_forget()
        self.info_about_frame.pack_forget()

    # Create methods for Teachers
    def teachers_add(self):
        self.hide_all_frames()
        self.teachers_add_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.teachers_add_frame, text="Teachers Add")
        p1.grid(row=0, column=0)

    def teachers_edit(self):
        self.hide_all_frames()
        self.teachers_edit_frame.pack(fill="both", expand=1)
        p2 = ttk.Label(self.teachers_edit_frame, text="Teachers Edit")
        p2.pack()

    def teachers_delete(self):
        self.hide_all_frames()
        self.teachers_delete_frame.pack(fill="both", expand=1)
        p3 = ttk.Label(self.teachers_delete_frame, text="Teachers Delete")
        p3.pack()

    # Create methods for Groups
    def groups_add(self):
        self.hide_all_frames()
        self.groups_add_frame.pack(fill="both", expand=1)
        p4 = ttk.Label(self.groups_add_frame, text="Groups Add")
        p4.pack()

    def groups_edit(self):
        self.hide_all_frames()
        self.groups_edit_frame.pack(fill="both", expand=1)
        p5 = ttk.Label(self.groups_edit_frame, text="Groups Edit")
        p5.pack()

    def groups_delete(self):
        self.hide_all_frames()
        self.groups_delete_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.groups_delete_frame, text="Groups Delete")
        p1.pack()

    # Create methods for Students
    def students_db(self):
        self.hide_all_frames()
        self.students_db_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.students_db_frame, text="Students Database")
        p1.pack()

    def info_about(self):
        self.hide_all_frames()
        self.info_about_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.info_about_frame, text="About")
        p1.pack()

    #     teachers_menu = tk.Menu(self, tearoff=False)
    #     self.add_cascade(label="File", underline=0, menu=teachers_menu)
    #     teachers_menu.add_command(label="Press-1", underline=1, command=self.press1)
    #
    #     groups_menu = tk.Menu(self, tearoff=False)
    #     self.add_cascade(label="New", underline=0, menu=groups_menu)
    #     groups_menu.add_command(label="Press-2", underline=1, command=self.press2)
    #
    # def press1(self):
    #     p1 = ttk.Label(self.parent, text="Press-1")
    #     p1.pack()
    #
    # def press2(self):
    #     p2 = ttk.Label(self.parent, text="Press-2")
    #     p2.pack()
    #
    # def quit(self):
    #     sys.exit(0)


class App(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.master = master

        menubar = MenuBar(self)
        self.config(menu=menubar)


if __name__ == "__main__":
    app = App(None)
    app.title("AutoRoad")
    app.geometry("400x400")
    style = ThemedStyle(app)
    style.set_theme("breeze")
    app.mainloop()
