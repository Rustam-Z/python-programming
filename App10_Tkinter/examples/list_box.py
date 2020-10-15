import tkinter as tk

# --- functions ---

def on_button():
    for i, var in enumerate(o_vars):
        print('OptionMenu {}: {}'.format(i, var.get()))
    print()

    print('ListBox:', l.curselection())
    for i in l.curselection():
        print('option:', OPTIONS[i])
    print()

    print('ChecboxBox:')
    for i, var in enumerate(cb_vars):
        if var.get():
            print('option:', OPTIONS[i])

# --- main ---

OPTIONS = ["Script 1","Script 2","Script 3","Script 4","Script 5"]

root = tk.Tk()

# --- OptionMenu ---

tk.Label(root, text='OptionMenus', bg='#aaa').pack(fill='x')

o_vars = []

for i in range(3):
    var = tk.StringVar(value='- select -')
    o_vars.append(var)
    o = tk.OptionMenu(root, var, *OPTIONS)
    o.pack()

# --- Listbox ---

tk.Label(root, text='Listbox', bg='#aaa').pack(fill='x')

l = tk.Listbox(root, selectmode='multiple')
l.pack()
l.insert('end', *OPTIONS)

# --- Checkbuttons ---

tk.Label(root, text='Checkbuttons', bg='#aaa').pack(fill='x')

cb_vars = []
for x in OPTIONS:
    var = tk.BooleanVar(value=False)
    cb_vars.append(var)
    c = tk.Checkbutton(root, text=x, variable=var)
    c.pack()

# --- others ---

b = tk.Button(root, text='OK', command=on_button)
b.pack(fill='x')

root.mainloop()