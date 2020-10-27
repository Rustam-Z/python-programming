from tkinter import *  # from x import * is bad practice
from tkinter import messagebox
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk


# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

# Scrollbar working with Sample App Class
class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)


# For testing the VerticalScrolledFrame
class SampleApp:
    def __init__(self, master):
        self.frame = VerticalScrolledFrame(master)
        self.frame.pack()
        self.label = ttk.Label(text="Shrink the window to activate the scrollbar.")
        self.label.pack()
        buttons = []
        for i in range(100):
            buttons.append(ttk.Button(self.frame.interior, text="Button " + str(i)))
            buttons[-1].pack(pady=5)


class Root:
    def __init__(self, master):
        frame = ttk.Frame(master)
        frame.pack()
        self.my_menu = Menu(master)
        master.config(menu=self.my_menu)

        # Create a Menu Item "File"
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.command_file_new)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        # Create a Menu Item "Edit"
        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.command_edit_cut)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Question", command=master.quit)

        # Create some frames
        self.file_new_frame = ttk.Frame(master, width=400, height=400)
        self.edit_cut_frame = ttk.Frame(master, width=400, height=400)

    def hide_all_frames(self):
        """Clears the screen after pressing the menu item"""
        for widget in self.file_new_frame.winfo_children():
            widget.destroy()

        for widget in self.edit_cut_frame.winfo_children():
            widget.destroy()

        self.file_new_frame.pack_forget()
        self.edit_cut_frame.pack_forget()

    # Create a functions for commands
    def command_file_new(self):
        """When you press File->New ... the following function code will work"""
        self.hide_all_frames()
        self.file_new_frame.pack(fill="both", expand=1)
        lab0 = ttk.Label(self.file_new_frame, text="it is just for checking New->File")
        btn0 = ttk.Button(self.file_new_frame, text="asdf", command=self.test)
        btn0.pack()
        lab0.pack()

    def test(self):
        ttk.Label(self.file_new_frame, text="asdf").pack()

    def command_edit_cut(self):
        self.hide_all_frames()
        self.edit_cut_frame.pack(fill="both", expand=1)
        lab1 = ttk.Label(self.edit_cut_frame, text="it is just for checking Edit->Cut")
        lab1.pack()


def main():
    root = ThemedTk(theme="breeze")
    root.geometry("500x500+250+100")
    app = Root(root)
    root.mainloop()


if __name__ == '__main__':
    main()
