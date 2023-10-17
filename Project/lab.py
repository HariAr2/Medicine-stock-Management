import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database


def update():
    selected_item =tree.focus()
    if not selected_item:
        messagebox.showerror("ERROR","Choose a product to update")
    else:
        id=id_entry.get()
        name=name_entry.get()
        stock=stock_entry.get()
        database.update_products(name,stock,id)
        add_to_treeview()
        clear()
        #create_chart()
        messagebox.showinfo("SUCCESS","Data has been updated")

def delete():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror("ERROR","Choose a product to Delete")
    else:
        id=id_entry.get()
        database.delete_product(id)
        add_to_treeview()
        clear()
        #create_chart()
        messagebox.showinfo("SUCCESS","Data has been Deleted")  

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row=tree.item(selected_item)["values"]
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        stock_entry.insert(0,row[2])
    else:
        pass

def add_to_treeview():
    products = database.fetch_products()
    tree.delete(*tree.get_children())
    for product in products:
        tree.insert('',END,values=product)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    stock_entry.delete(0,END)

def insert():
    id=id_entry.get()
    name=name_entry.get()
    stock=stock_entry.get()
    if not(id and name and stock):
        messagebox.showerror("ERROR","Enter all fields.")
    elif database.id_exists(id):
        messagebox.showerror("ERROR","ID already exists")
    else:
        try:
            stock_value=int(stock)
            database.insert_product(id,name,stock_value)
            add_to_treeview()
            clear()
            #create_chart()
            messagebox.showinfo("SUCCESS","Data has been added")
        except ValueError:
            messagebox.showerror("ERROR","Stock should be an integer")



app=customtkinter.CTk()
app.title('Medical Store Stock Management')
app.geometry("800x680")
app.config(bg='#29B2F8')
app.resizable(False,False)


font1=('Serif',25,'bold')
font2=('Serif',18,'bold')
font3=('Serif',13,'bold')


title_label = customtkinter.CTkLabel(app,font=font1,text="Product Details",text_color='#fff',bg_color='#0A0B0C')
title_label.place(x=35,y=15)


frame=customtkinter.CTkFrame(app,bg_color="#80ACC2",fg_color="#221B1B",corner_radius=10,border_width=2,border_color='#fff',width=200,height=350)
frame.place(x=25,y=45)


image1=PhotoImage(file="1-2.png")
image1_label=Label(frame,image=image1,bg="#1B1B21")
image1_label.place(x=70,y=15)


id_label = customtkinter.CTkLabel(frame,font=font2,text="Medicine ID:",text_color="#000",fg_color="#fff",bg_color="#1B1B21")
id_label.place(x=40,y=70)

id_entry=customtkinter.CTkEntry(frame,font=font2,text_color="#000",fg_color="#fff",bg_color="#B20160")
id_entry.place(x=20,y=105)


name_label = customtkinter.CTkLabel(frame,font=font2,text="Name:",text_color="#000",fg_color="#fff",bg_color="#1B1B21")
name_label.place(x=65,y=135)

name_entry=customtkinter.CTkEntry(frame,font=font2,text_color="#000",fg_color="#fff",bg_color="#B20160")
name_entry.place(x=20,y=165)

stock_label=customtkinter.CTkLabel(frame,font=font2,text="In Stock",text_color="#000",fg_color="#fff",bg_color="#1B1B21")
stock_label.place(x=55,y=195)

stock_entry=customtkinter.CTkEntry(frame,text_color="#000",fg_color="#fff",bg_color="#B20160")
stock_entry.place(x=20,y=225)

add_button=customtkinter.CTkButton(frame,command=insert,font=font2,text_color="#fff",text="ADD",fg_color="#DA70D6",hover_color="#9370DB",bg_color="#1B1B21",cursor="hand2",corner_radius=8,width=80)
add_button.place(x=15,y=265)

clear_button=customtkinter.CTkButton(frame,command=lambda:clear(True),font=font2,text="New",text_color="#fff",fg_color="#4682B4",hover_color="#7B68EE",bg_color="#1B1B21",cursor="hand2",width=80,corner_radius=8)
clear_button.place(x=108,y=265)

update_button=customtkinter.CTkButton(frame,command=update,font=font2,text="Update",text_color="#fff",fg_color="#BC8F8F",bg_color="#1B1B21",hover_color="#D2691E",cursor="hand2",width=80,corner_radius=8)
update_button.place(x=15,y=305)


delete_button=customtkinter.CTkButton(frame,command=delete,font=font2,text="Delete",text_color="#fff",fg_color="#FF7F50",bg_color="#1B1B21",hover_color="#FF4500",cursor="hand2",corner_radius=8,width=80)
delete_button.place(x=108,y=305)

style=ttk.Style(app)


style.theme_use('clam')
style.configure('Treeview',font=font3,foreground="#fff",background="#0A0B0C",fieldbackground="1B1B21")
style.map('Treeview',background=[("selected","#AA04A7")])

tree=ttk.Treeview(app,height=17)

tree['columns']=('ID','Name','In stock')

tree.column("#0",width=0,stretch=tk.NO)
tree.column("ID",anchor=tk.CENTER,width=150)
tree.column("Name",anchor=tk.CENTER,width=150)
tree.column("In stock",anchor=tk.CENTER,width=150)

tree.heading("ID",text="ID")
tree.heading("Name",text="Name")
tree.heading("In stock",text="In stock")

tree.place(x=300,y=25)
tree.bind('<ButtonRelease>',display_data)

add_to_treeview()

app.mainloop()