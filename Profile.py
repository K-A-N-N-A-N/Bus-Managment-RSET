import tkinter
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk

#import mysql.connector
#conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
#busdb=conn.cursor()

def V_BusID():
    bbuid="U2102"
    VID_app = CTk()
    VID_app.geometry("600x440")
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    
    ''''
    busdb.execute('select * from student')
    for row in busdb:
         if row[0]==bbuid:
              bclass=row[4]
              bYear=row[3]
              baddr=row[5]
              bname=row[6]
              bstat= row[2]
    busdb.execute('select * from bstudent')
    for row in busdb:
         if row[1]==bbuid:
            busid= row[0]       
    '''

    bg_image = ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    img = customtkinter.CTkLabel(master=VID_app, image=bg_image)
    img.pack()

    back_btn = CTkButton(master=VID_app,width=50, height=10, text = "<- Back", compound="left", corner_radius=40, fg_color="black")
    back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")

    frame = customtkinter.CTkFrame(master=img,width=320, height=340, corner_radius=40)
    frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

    Ttl_label = CTkLabel(master=frame, text= "PROFILE",font= ("Century Gothic", 25), text_color = "white" )
    Ttl_label.place(x = 120, y = 50 )

    name_label = CTkLabel(master=frame, text= "Name : ",font= ("Century Gothic", 20), text_color = "#FFCC70")
    name_label.place(x = 50, y = 100)
    bname = "lannan"
    name_db = CTkLabel(master=frame, text= bname,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    name_db.place(x = 170, y = 100)

    Stat_label = CTkLabel(master=frame, text= "Status : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Stat_label.place(x = 50, y = 130)
    bstat = 1
    if bstat==1:
        Stat_db = CTkLabel(master=frame, text= "ACTIVE!",font= ("Century Gothic", 20), text_color = "green" )
        Stat_db.place(x = 170, y = 130)
    else:
        Stat_db = CTkLabel(master=frame, text= "EXPIRED ",font= ("Century Gothic", 20), text_color = "red" )
        Stat_db.place(x = 170, y = 130)

    Uid_label = CTkLabel(master=frame, text= "UID : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Uid_label.place(x = 50, y = 160)
    Uid_db = CTkLabel(master=frame, text= bbuid,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Uid_db.place(x = 170, y = 160)

    BusId_label = CTkLabel(master=frame, text= "BusID : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    BusId_label.place(x = 50, y = 190)
    busid = "U210"
    BusId_db = CTkLabel(master=frame, text= busid,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    BusId_db.place(x = 170, y = 190)

    class_label = CTkLabel(master=frame, text= "CLASS : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    class_label.place(x = 50, y = 220)
    bclass = "CSE"
    class_db = CTkLabel(master=frame, text= bclass,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    class_db.place(x = 170, y = 220)

    bYear = "2"
    Year_label = CTkLabel(master=frame, text= "Year : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Year_label.place(x = 50, y = 250)
    Year_db = CTkLabel(master=frame, text= bYear,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Year_db.place(x = 170, y = 250)

    baddr = "Aluva"
    Addr_label = CTkLabel(master=frame, text= "Address : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Addr_label.place(x = 50, y = 280)
    Addr_db = CTkLabel(master=frame, text= baddr,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Addr_db.place(x = 170, y = 280)

    VID_app.mainloop()
V_BusID()