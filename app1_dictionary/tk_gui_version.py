''' references
https://www.delftstack.com/howto/python-tkinter/how-to-change-the-tkinter-label-text/
http://effbot.org/tkinterbook

'''

import tkinter as tk
from tkinter import messagebox, IntVar, END, TOP, RIGHT, NW, Y, SINGLE
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedStyle

import json
import webbrowser
from difflib import get_close_matches

# Open the json file with db
data = json.load(open("app1_dictionary/data.json"))

# Bookmarks
BOOKMARKS = []
HISTORY = []

class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        self.frame = ttk.Frame(master)
        self.frame.pack()

        self.master = master

        # Create a Menu Item for Searching
        search_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Info --EightSoft dev
        info_menu = tk.Menu(self, tearoff=False)

        # Add the cascades for menu bar
        self.add_cascade(label="Dictionary", menu=search_menu)
        self.add_cascade(label="Help", menu=info_menu)

        # Searching
        search_menu.add_command(label="Search", command=self.dict_search)
        search_menu.add_command(label="Bookmarks", command=self.bookmarks)

        # Help
        info_menu.add_command(label="About", command=self.info_about)

        # Create frames for each new window --MenuBar-Cascade-Commands
        self.dict_search_frame = ttk.Frame(master)
        self.bookmarks_frame = ttk.Frame(master)
        self.info_about_frame = ttk.Frame(master)

    # Hide the frames when you switch the menu
    def hide_all_frames(self):
        """Cleans the screen after pressing the menu item"""
        for widget in self.dict_search_frame.winfo_children():
            widget.destroy()

        for widget in self.bookmarks_frame.winfo_children():
            widget.destroy()

        for widget in self.info_about_frame.winfo_children():
            widget.destroy()

        self.dict_search_frame.pack_forget()
        self.bookmarks_frame.pack_forget()
        self.info_about_frame.pack_forget()

    # Create methods for Teachers
    def dict_search(self):
        self.hide_all_frames()
        self.dict_search_frame.pack(fill="both", expand=1)

        # Creating a Notebook
        notebook = ttk.Notebook(self.dict_search_frame)
        notebook.pack(pady=10, padx=10)

        # Initialize frame for notebooks
        self.frame1 = ttk.Frame(notebook)
        self.frame2 = ttk.Frame(notebook)

        # Place the frame on the screen
        self.frame1.pack(fill="both", expand=1)
        self.frame2.pack(fill="both", expand=1)

        # Add the notebooks
        notebook.add(self.frame1, text="Search")
        notebook.add(self.frame2, text="History")

        # ===================== Frame 1 ===================
        l1 = ttk.Label(self.frame1, text="Enter word")
        l1.grid(row=0, column=0, padx=10, pady=10)

        self.e1 = ttk.Entry(self.frame1)
        self.e1.grid(row=0, column=1, padx=10, pady=10)
    
        self.l2 = ttk.Label(self.frame1, text="", wraplength=250)
        self.l2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        b1 = ttk.Button(self.frame1, text="Search", command=self.translate, width=30)
        b1.grid(row=1, column=0, columnspan=2)

        # ===================== Frame 2 ===================
        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.list_box = tk.Listbox(self.frame2, yscrollcommand=scrollbar.set, width=50, height=50, borderwidth=0, highlightthickness=0, selectmode=SINGLE)
        self.list_box.pack(padx=10, pady=10, side=TOP, anchor=NW)
        
        self.list_box.bind("<<ListboxSelect>>", self.from_history)
        scrollbar.config(command=self.list_box.yview)
    

    def translate(self):
        w = self.e1.get()
        w = w.lower()
    
        if w in data:
            self.l2['text'] = data[w]
            self.list_box.insert(END, w) # History
            HISTORY.append(w)

        elif w.title() in data:
            self.l2['text'] = data[w.title()] 
            self.list_box.insert(END, w.title()) # History
            HISTORY.append(w.title())


        elif w.upper() in data: # in case user enters words like USA or NATO
            self.l2['text'] = data[w.upper()]
            self.list_box.insert(END, w.upper()) # History
            HISTORY.append(w.upper())

        elif len(get_close_matches(w, data.keys())) > 0:
            yn = messagebox.askquestion("Hint", "Did you mean '%s' instead?" % get_close_matches(w, data.keys())[0])
            if yn == "yes":
                self.l2['text'] = data[get_close_matches(w, data.keys())[0]]
                self.list_box.insert(END, get_close_matches(w, data.keys())[0]) # History
                HISTORY.append(get_close_matches(w, data.keys())[0])

            elif yn == "no":
                self.l2['text'] = "The word doesn't exist. Please double check it."
            else:
                self.l2['text'] = "We didn't understand your entry."

        else:
            self.l2['text'] = "The word doesn't exist. Please double check it."

        print("Translated successfully!")

        # Bookmarks
        self.var = IntVar()
        c = ttk.Checkbutton(
            self.frame1, text="Add to bookmarks",
            variable=self.var,
            command=self.boookmark_it)

        c.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # delete the last word
        # self.e1.delete(0, END)


    # For translate the words from History
    def from_history(self, *args):
        for i in self.list_box.curselection():
            print('Translate from History:', HISTORY[i])

            if HISTORY[i] in data:
                messagebox.showinfo("{}".format(HISTORY[i]), data[HISTORY[i]])


    def bookmarks(self):
        self.hide_all_frames()
        self.bookmarks_frame.pack(fill="both", expand=1)
        p2 = ttk.Label(self.bookmarks_frame, text="Here you can your boookmarks")
        p2.pack(padx=10, pady=10)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.bookmarks_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.list_box_1 = tk.Listbox(self.bookmarks_frame, yscrollcommand=scrollbar.set, width=50, height=50, borderwidth=0, highlightthickness=0, selectmode=SINGLE)
        self.list_box_1.pack(padx=10, pady=10, side=TOP, anchor=NW)

        self.list_box_1.insert('end', *BOOKMARKS)
        
        self.list_box_1.bind("<<ListboxSelect>>", self.from_boormarks)
        scrollbar.config(command=self.list_box_1.yview)
    

    def boookmark_it(self):
        if self.var.get() == 1:
            BOOKMARKS.append(self.e1.get())
            print("Bookmarks: {}".format(BOOKMARKS))
        else:
            pass

    # For translate the words from Bookmarks
    def from_boormarks(self, *args):
        for i in self.list_box_1.curselection():
            print('Translate from Bookmarks:', BOOKMARKS[i])

            if BOOKMARKS[i] in data:
                messagebox.showinfo("{}".format(BOOKMARKS[i]), data[BOOKMARKS[i]])
  

    def info_about(self):

        def callback(url):
            webbrowser.open_new(url)

        self.hide_all_frames()
        self.info_about_frame.pack(fill="both", expand=1)
        ttk.Label(self.info_about_frame, text="ABOUT", background='#c5e3e0').pack()
        ttk.Label(self.info_about_frame, text="EightSoft Academy | Rustam-Z | Alimov-8").pack()
        
        link1 = tk.Label(self.info_about_frame, text="Source Code", fg='#215fdb')
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/Rustam-Z/python-projects-eightsoft/tree/master/App1_Dictionary"))

    

 

class App(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.master = master

        menubar = MenuBar(self)
        self.config(menu=menubar)


if __name__ == "__main__":

    # Create object
    app = App(None)
    app.title("My Dictionary App")
    app.geometry("400x400")
    style = ThemedStyle(app)
    style.set_theme("breeze")
    app.mainloop()
