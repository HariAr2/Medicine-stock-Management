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


frame=customtkinter.CTkFrame(app,bg_color="#80ACC2",fg_color="#221B1B",corner_radius=10,border_width=2,border_color='#fff',width=200,height=700)
frame.place(x=25,y=45)


image1=PhotoImage(file="1.png")
image1_label=Label(frame,image=image1,bg="#1B1B21")
image1_label.place(x=45,y=5)

app.mainloop()