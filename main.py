from func import Products

import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo

products = []

root = tk.Tk()
root.title('Ražas uzskaite')
root.geometry('1280x720')
root.resizable(False, False)

frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

product_name_label = ttk.Label(frame, text='Name')
product_name_label.grid(column=0, row=0, sticky='E', **options)

product_type_label = ttk.Label(frame, text='Sex')
product_type_label.grid(column=0, row=1, sticky='E', **options)

product_amount_label = ttk.Label(frame, text='Age')
product_amount_label.grid(column=0, row=3, sticky='E', **options)

product_name = tk.StringVar()
product_name = ttk.Entry(frame, textvariable=product_name)
product_name.grid(column=1, row=0, **options)
product_name.focus()

product_type = tk.StringVar(value="None")
R1 = tk.Radiobutton(frame, text="Dārzenis", variable=product_type, value="Dārzenis")
R1.grid(column=1, row=1, **options)
R2 = tk.Radiobutton(frame, text="Auglis", variable=product_type, value="Auglis")
R2.grid(column=1, row=2, **options)

product_amount = tk.IntVar(value="0")
product_amount = ttk.Entry(frame, textvariable=product_amount)
product_amount.grid(column=1, row=3, **options)
product_amount.focus()

new_product_name = tk.StringVar()
new_product_name = ttk.Entry(frame, textvariable=new_product_name)
new_product_name.grid(column=0, row=5, **options)
new_product_name.focus()

new_product_amount = tk.StringVar()
new_product_amount = ttk.Entry(frame, textvariable=new_product_amount)
new_product_amount.grid(column=4, row=5, **options)
new_product_amount.focus()

def add_button_clicked():
    product_amount1 = product_amount.get()
    product_type1 = product_type.get()
    product_name1 = product_name.get()
    print(product_name1, product_type1, product_amount1)
    products.append(Products(product_name1, product_type1, product_amount1))
    print(products)
    change_list()


def change_list():
    listbox.delete(0,END)
    for Products in products:
        listbox.insert("end",f"{Products.name},{Products.type},{Products.amount}")

def name_change_button_clicked():
    new_product_name1 = new_product_name.get()
    for selected in listbox.curselection():
        products[selected].name_change(new_product_name1)
    change_list()

def type_change_button_clicked():
    for selected in listbox.curselection():
        products[selected].type_change()
    change_list()

def amount_change_button_clicked():
    for selected in listbox.curselection():
        products[selected].amount_change()
    change_list()

production_button = ttk.Button(frame, text='Pievienot sarakstam')
production_button.grid(column=2, row=0, sticky='W', **options)
production_button.configure(command=add_button_clicked)

product_name_change_button = ttk.Button(frame, text='Produkta nosaukuma maiņa')
product_name_change_button.grid(column=1, row=5, sticky='W', **options)
product_name_change_button.configure(command=name_change_button_clicked)

product_type_change_button = ttk.Button(frame, text='Produkta veida maiņa')
product_type_change_button.grid(column=2, row=5, sticky='W', **options)
product_type_change_button.configure(command=type_change_button_clicked)

product_amount_button = ttk.Button(frame, text='Produkta daudzuma maiņa')
product_amount_button.grid(column=5, row=5, sticky='W', **options)
product_amount_button.configure(command=amount_change_button_clicked)

listbox = tk.Listbox(frame, height=6, width=70, selectmode=tk.EXTENDED)
listbox.grid(column=0, columnspan=3, row=4, **options)

label2 = ttk.Label(frame)
label2.grid(row=4, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()