import customtkinter as ctk
import warnings
import tkinter
import menu
import busroutes
from PIL import ImageTk,Image

import mysql.connector
conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
busdb=conn.cursor()

      

def details(x):
    try:
            ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
            ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
    except AttributeError:
            print("Invalid command name in ctk")

    b_app = ctk.CTk()  #creating cutstom tkinter window
    b_app.geometry("1200x640")
    b_app.title('BUS DETAILS')


    warnings.filterwarnings('ignore') 
    img1=ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    l1=ctk.CTkLabel(master=b_app,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=880, height=500,bg_color="transparent",corner_radius=30)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    busdb.execute('select * from bus where busno = %s',(x,))
    for row in busdb :
        bname = row[5]
        bRS = row[3]
        bAS = row[4]
        b_rate = row[2]
        b_route = row[1]
                

    def bback():
        b_app.destroy()
        busroutes.buss()

    warnings.filterwarnings('ignore') 
    img3=ImageTk.PhotoImage(Image.open("back33.png"))
    back_btn = ctk.CTkButton(master=b_app,width=50,text="", height=10,image=img3, compound="left", fg_color="#0c9bb3",command = bback)
    back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")

    l2=ctk.CTkLabel(master=frame, text="BUS DETAILS",font=('Century Gothic',30),text_color="#7CB9E8",width=40)
    l2.place(x=50, y=45)

    l3=ctk.CTkLabel(master=frame, text="Driver's Name: "+bname,font=('Century Gothic',20), anchor="center")
    l3.place(x=50, y=110)


    l4=ctk.CTkLabel(master=frame, text="Route: "+b_route,font=('Century Gothic',20), anchor="center")
    l4.place(x=50, y=165)

    l5=ctk.CTkLabel(master=frame, text="Rate: "+str(b_rate),font=('Century Gothic',20), anchor="center")
    l5.place(x=50, y=220)


    l5=ctk.CTkLabel(master=frame, text="Seats Available: "+str(bRS),font=('Century Gothic',20), anchor="center")
    l5.place(x=50, y=275)

    l6=ctk.CTkLabel(master=frame, text="Total Seats: "+str(bAS),font=('Century Gothic',20), anchor="center")
    l6.place(x=50, y=330)

    string1="busloc"+str(x)+".png"

    img2=ImageTk.PhotoImage(Image.open(string1))
    l7=ctk.CTkLabel(master=frame,image=img2)
    l7.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

    b_app.mainloop()
