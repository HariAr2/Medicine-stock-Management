import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database


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

add_button=customtkinter.CTkButton(frame,font=font2,text_color="#fff",text="ADD",fg_color="#DA70D6",hover_color="#9370DB",bg_color="#1B1B21",cursor="hand2",corner_radius=8,width=80)
add_button.place(x=15,y=265)

clear_button=customtkinter.CTkButton(frame,font=font2,text="New",text_color="#fff",fg_color="#4682B4",hover_color="#7B68EE",bg_color="#1B1B21",cursor="hand2",width=80,corner_radius=8)
clear_button.place(x=108,y=265)

update_button=customtkinter.CTkButton(frame,font=font2,text="Update",text_color="#fff",fg_color="#BC8F8F",bg_color="#1B1B21",hover_color="#D2691E",cursor="hand2",width=80,corner_radius=8)
update_button.place(x=15,y=305)


delete_button=customtkinter.CTkButton(frame,font=font2,text="Delete",text_color="#fff",fg_color="#FF7F50",bg_color="#1B1B21",hover_color="#FF4500",cursor="hand2",corner_radius=8,width=80)
delete_button.place(x=108,y=305)



app.mainloop()