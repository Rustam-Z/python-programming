from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv

# Main Window
root = Tk()
root.title("CRM Database")
root.geometry("320x480")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="codemy",
)

# Check to see if connection to MySQL was created
# print(my_db)

# ============== Create a cursor and initialize it ==============
my_cursor = my_db.cursor()

# Create a db --we need only for the first time --then comment it
# my_cursor.execute("CREATE DATABASE codemy")

# ============= Test to see if db was created ============
# for db in my_cursor:
#     print(db)

# =========== Create A Table ============
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers ("
                  "first_name VARCHAR(255),"
                  "last_name VARCHAR(255),"
                  "zip_code INT(10),"
                  "price_paid DECIMAL(10, 2),"
                  "user_id INT AUTO_INCREMENT PRIMARY KEY "
                  ")")


# # =========== Alter Table ===========
# my_cursor.execute("ALTER TABLE customers ADD (\
#     email VARCHAR(255),\
#     address_1 VARCHAR(255),\
#     address_2 VARCHAR(255),\
#     city VARCHAR(50),\
#     state VARCHAR(50),\
#     country VARCHAR(255),\
#     phone VARCHAR(255),\
#     payment_method VARCHAR(50),\
#     discount_code VARCHAR(255))")

# =========== Show Table ===========
# my_cursor.execute("SELECT * FROM customers")
# print(my_cursor.description)
# OR
# for t in my_cursor.description:
#     print(t)


def clear_fields():
    """Clears the text fields"""
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zip_code_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    username_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)


# Submit Customer To Database
def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, zip_code, price_paid, email, address_1, address_2, " \
                  "city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, " \
                  "%s, %s, %s, %s, %s, %s) "
    values = (first_name_box.get(), last_name_box.get(), zip_code_box.get(), price_paid_box.get(), email_box.get(),
              address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(),
              phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    # Commit the changes to the database
    my_db.commit()
    # Clear the fields
    clear_fields()


def list_customers():
    def write_to_csv(res):
        with open('customers.csv', 'a', newline='') as f:
            w = csv.writer(f, dialect='excel')
            for record in res:
                w.writerow(record)

    global index
    list_customer_query = Tk()
    list_customer_query.title("List of All Customers")
    list_customer_query.geometry('400x600')

    my_cursor.execute("select * from customers ")
    res = my_cursor.fetchall()

    for index, i in enumerate(res):
        num = 0
        for j in i:
            list_label = Label(list_customer_query, text=j)
            list_label.grid(row=index, column=num)
            num += 1

    csv_button = Button(list_customer_query, text="Save to Excel", command=lambda: write_to_csv(res))
    csv_button.grid(row=index+1, column=0, padx=10)
    csv_open_button = Button(list_customer_query, text="Open Excel", command=lambda: write_to_csv(res))
    csv_open_button.grid(row=index+2, column=0, padx=10)


# =========== Create Main Form To Enter Customer Form ===========
title_label = Label(root, text="Codemy Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, padx=15)
first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="Sate").grid(row=6, column=0, sticky=W, padx=10)
zip_code_label = Label(root, text="Zip Code").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
username_label = Label(root, text="Username").grid(row=11, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=13, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)

# =========== Create Entry Box ===========
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=3)
last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=3)
address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=3)
address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=3)
city_box = Entry(root)
city_box.grid(row=5, column=1, pady=3)
state_box = Entry(root)
state_box.grid(row=6, column=1, pady=3)
zip_code_box = Entry(root)
zip_code_box.grid(row=7, column=1, pady=3)
country_box = Entry(root)
country_box.grid(row=8, column=1, pady=3)
phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=3)
email_box = Entry(root)
email_box.grid(row=10, column=1, pady=3)
username_box = Entry(root)
username_box.grid(row=11, column=1, pady=3)
payment_method_box = Entry(root)
payment_method_box.grid(row=12, column=1, pady=3)
discount_code_box = Entry(root)
discount_code_box.grid(row=13, column=1, pady=3)
price_paid_box = Entry(root)
price_paid_box.grid(row=14, column=1, pady=4)

# =========== Create Buttons ===========
add_customer_button = Button(root, text="Add Customer", fg="blue", padx=20, command=add_customer)
add_customer_button.grid(row=15, column=0, pady=5)
clear_fields_button = Button(root, text="Clear Fields", fg="red", padx=28, command=clear_fields)
clear_fields_button.grid(row=15, column=1, pady=5)
# List customers button
list_customers_button = Button(root, text="List Customers", padx=19, command=list_customers)
list_customers_button.grid(row=16, column=0, padx=10)

root.mainloop()
