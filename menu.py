import tkinter
import customtkinter as ctk
import warnings
import registration
import Bus_ID
import busroutes
import Profile
import mysql.connector
from PIL import ImageTk,Image
from customtkinter import *


def main():
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("dark-blue")  

    root = ctk.CTk()  
    root.geometry("600x440")
    root.title('BUS DETAILS')

    def bus_app_gui():
        root.destroy()
        Profile.Prof()
    def fees_payment_gui():
        root.destroy()
        registration.register()

    def VirtualBID_gui():
        fflag=0
        conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
        busdb=conn.cursor()
        busdb.execute('select * from current')
        for row in busdb:
            if row[1]==7:
                bbuid=row[0]
        busdb.execute('select * from student')        
        for row in busdb:
            if row[0]==bbuid:
                if row[2]==1:
                    fflag=1
                    root.destroy()
                    Bus_ID.V_BusID()
        if fflag==0:
                l2=ctk.CTkLabel(master=frame, text="Bus ID not Available",font=('Century Gothic',15),text_color="red")
                l2.place(x=50, y=280)       


    def bus_details_gui():
        root.destroy()
        busroutes.buss()

    warnings.filterwarnings('ignore') 
    img1=ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    l1=ctk.CTkLabel(master=root,image=img1)
    l1.pack()


    frame=ctk.CTkFrame(master=l1, width=320, height=360, corner_radius=40)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="MENU",font=('Century Gothic',20))
    l2.place(x=50, y=45)

    button2 = ctk.CTkButton(master=frame, width=220, text="Virtual ID", command=VirtualBID_gui, corner_radius=30)
    button2.place(x=50, y=110)

    button2 = ctk.CTkButton(master=frame, width=220, text="Profile", command=bus_app_gui, corner_radius=30)
    button2.place(x=50, y=150)

    button3 = ctk.CTkButton(master=frame, width=220, text="Fees Payment", command=fees_payment_gui, corner_radius=30)
    button3.place(x=50, y=190)


    button4 = ctk.CTkButton(master=frame, width=220, text="Bus Details", command=bus_details_gui, corner_radius=30)
    button4.place(x=50, y=230)

    root.mainloop()

if __name__== "__main__":
     main()

