# Start: Tuesday, July 14, 2020, 3:02 PM
# Address Book Application
# Videos 19-23
# EightSoft Academy

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Database 1")
root.iconbitmap('examples/photos/icon.ico')
root.geometry("325x400")
# root.configure(bg="black")

# Create table
'''
c.execute("""CREATE TABLE addresses ( 
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zip_code int
    )""")
'''


def delete():
    """Function to delete a record"""
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Delete a record
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())

    delete_box.delete(0, END)
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


def save_edit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("""UPDATE addresses SET 
        first_name = :f_name,
        last_name = :l_name,
        address = :address,
        city = :city,
        state = :state,
        zip_code = :zip_code
        
        WHERE oid = :oid""",
              {
                  'f_name': f_name_editor.get(),
                  'l_name': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zip_code': zip_code_editor.get(),
                  'oid': delete_box.get()
              }
              )
    conn.commit()
    conn.close()

    editor.destroy()


def edit():
    """Edits the record in db"""
    global editor
    editor = Tk()
    editor.title("Update the record")
    editor.iconbitmap('examples/photos/icon.ico')
    editor.geometry("325x300")

    # Create Globals
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zip_code_editor

    # Create a text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=4)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20, pady=4)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20, pady=4)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20, pady=4)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20, pady=4)
    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=5, column=1, padx=20, pady=4)

    # Create Text Box Labels
    f_name_editor_label = Label(editor, text="First Name")
    f_name_editor_label.grid(row=0, column=0, padx=20)
    l_name_editor_label = Label(editor, text="Last Name")
    l_name_editor_label.grid(row=1, column=0, padx=20)
    address_editor_label = Label(editor, text="Address")
    address_editor_label.grid(row=2, column=0, padx=20)
    city_editor_label = Label(editor, text="City")
    city_editor_label.grid(row=3, column=0, padx=20)
    state_editor_label = Label(editor, text="State")
    state_editor_label.grid(row=4, column=0, padx=20)
    zip_code_editor_label = Label(editor, text="Zip Code")
    zip_code_editor_label.grid(row=5, column=0, padx=20)

    save_btn = Button(editor, text="Save Record", command=save_edit, bg="grey")
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=106)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE OID = " + record_id)
    records = c.fetchall()

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_code_editor.insert(0, record[5])


def submit():
    """Adds the record to the database"""
    # Create a db or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code )",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zip_code': state.get(),
              }
              )
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)


def query():
    """Reads the records from db"""
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, OID FROM addresses")
    records = c.fetchall()
    # print(records) # printing in terminal

    # Loop through results
    print_records = ''
    for record_info in records:
        print_records += str(record_info[0]) + "/" + str(record_info[1]) + "/" + str(record_info[2]) + "/" + str(
            record_info[3]) + "/" + str(record_info[4]) + "/" + str(record_info[5]) + "/" + str(record_info[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2, )

    conn.commit()
    conn.close()


# Create a text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=4)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20, pady=4)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20, pady=4)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20, pady=4)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20, pady=4)
zip_code = Entry(root, width=30)
zip_code.grid(row=5, column=1, padx=20, pady=4)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0, padx=20)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0, padx=20)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0, padx=20)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0, padx=20)
zip_code_label = Label(root, text="Zip Code")
zip_code_label.grid(row=5, column=0, padx=20)
delete_box_label = Label(root, text="Select ID: ")
delete_box_label.grid(row=9, column=0, padx=10)

# Create Submit Button
submit_btn = Button(root, text="Add record", command=submit, fg="red")
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=109)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query, fg="red")
query_btn.grid(row=7, column=0, columnspan=2, pady=7, padx=10, ipadx=100)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete, bg="grey")
delete_btn.grid(row=10, column=0, columnspan=2, pady=8, padx=10, ipadx=101)

# Create an Update button
edit_btn = Button(root, text="Update Record", command=edit, bg="grey")
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, ipadx=98)

root.mainloop()
