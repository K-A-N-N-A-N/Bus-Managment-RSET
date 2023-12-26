import tkinter
import customtkinter
import menu
import warnings
import registration
import mysql.connector
from customtkinter import *
from PIL import Image, ImageTk


def Prof():
    conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
    busdb=conn.cursor()
    flagb=0
    flagenroll=0
    busdb.execute('select * from current')
    for row in busdb:
        if row[1]==7:
            bbuid=row[0] 
    Pro_app = CTk()
    Pro_app.geometry("600x440")
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    
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
            flagb=1
            busid= row[0]    
    if flagb==0:
        busid = "NIL"        
    def pback():
        Pro_app.destroy()
        menu.main()               
    warnings.filterwarnings('ignore') 
    bg_image = ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    img = customtkinter.CTkLabel(master=Pro_app, image=bg_image)
    img.pack()

    def deenroll():
        busdb.execute('delete from bstudent where UID =%s',(bbuid,))
        busdb.execute('update student set payment_status= 0 where UID =%s',(bbuid,))
        conn.commit()
        Pro_app.destroy()
        menu.main()    

    def enrol():
        Pro_app.destroy()
        registration.register()           

    
    
    warnings.filterwarnings('ignore') 
    img2=ImageTk.PhotoImage(Image.open("back33.png"))
    back_btn = CTkButton(master=Pro_app,width=50,text="", height=10,image=img2, compound="left", fg_color="#0c9bb3",command = pback)
    back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")

    frame = customtkinter.CTkFrame(master=img,width=360, height=380, corner_radius=20)
    frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

    Ttl_label = CTkLabel(master=frame, text= "PROFILE",font= ("Century Gothic", 25), text_color = "white" )
    Ttl_label.place(x = 120, y = 50 )

    name_label = CTkLabel(master=frame, text= "Name : ",font= ("Century Gothic", 20), text_color = "#FFCC70")
    name_label.place(x = 50, y = 100)
    name_db = CTkLabel(master=frame, text= bname,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    name_db.place(x = 170, y = 100)

    Stat_label = CTkLabel(master=frame, text= "Status : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Stat_label.place(x = 50, y = 130)
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
    BusId_db = CTkLabel(master=frame, text= busid,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    BusId_db.place(x = 170, y = 190)

    class_label = CTkLabel(master=frame, text= "CLASS : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    class_label.place(x = 50, y = 220)
    class_db = CTkLabel(master=frame, text= bclass,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    class_db.place(x = 170, y = 220)

    Year_label = CTkLabel(master=frame, text= "Year : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Year_label.place(x = 50, y = 250)
    Year_db = CTkLabel(master=frame, text= bYear,font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Year_db.place(x = 170, y = 250)

    Addr_label = CTkLabel(master=frame, text= "Address : ",font= ("Century Gothic", 20), text_color = "#FFCC70" )
    Addr_label.place(x = 50, y = 280)
    Addr_db = CTkLabel(master=frame, text= baddr,font= ("Century Gothic", 20), text_color = "#FFCC70", height=20 )
    Addr_db.place(x = 170, y = 280)

    busdb.execute('select * from student ')
    for row in busdb:
        if row[0]==bbuid and row[2]==1:
            flagenroll=1
    if flagenroll==1:        
        deenroll_btn = CTkButton(master=frame,width=50,text="DE-ENROLL", height=10, compound="left", fg_color="red",command = deenroll)
        deenroll_btn.place(relx = 0.65, rely = 0.9, anchor = "w")
    else:
        enroll_btn = CTkButton(master=frame,width=50,text="ENROLL", height=10, compound="left", fg_color="green",command = enrol)
        enroll_btn.place(relx = 0.65, rely = 0.9, anchor = "w")

    Pro_app.mainloop()