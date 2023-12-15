from customtkinter import *
from PIL import Image

import mysql.connector
conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='bustrial')
busdb=conn.cursor()

def V_BusID():
    bbuid="U2117"
    VID_app = CTk()
    VID_app.geometry("500x600")
    set_appearance_mode("white")
    
    busdb.execute('select * from student')
    for row in busdb:
         if row[0]==bbuid:
              busid=row[2]
              bclass=row[5]
              bage=row[4]
              baddr=row[6]
              bname=row[7]
              bstat= row[3]
              

    #frame = CTkFrame(master=app, fg_color="red", border_color="blue", border_width=2)
    #frame.pack(expand = True)

    logo_image = CTkImage(dark_image=Image.open("background_1.png"), size = (500,80))

    logo_label = CTkLabel(VID_app,image = logo_image, text="")
    logo_label.grid(row = 0, column = 0)

    Ttl_label = CTkLabel(master=VID_app, text= "Profile",font= ("courier new", 30), text_color = "red" )
    Ttl_label.place(relx = 0.5, rely = 0.2, anchor = "center" )

    barcode_image = CTkImage(dark_image=Image.open("barcode.png"), size = (500,80))

    #barcode_label = CTkLabel(VID_app,image = barcode_image, text="")
    #barcode_label.grid(row = 0, column = 0)
    Uid_label = CTkLabel(master=VID_app, text= "NAME : ",font= ("courier new", 15), text_color = "red" )
    Uid_label.place(relx = 0.2, rely = 0.3, anchor = "e" )
    Uid_db = CTkLabel(master=VID_app, text= bname,font= ("courier new", 15), text_color = "red" )
    Uid_db.place(relx = 0.5, rely = 0.3, anchor = "w" )

    Uid_label = CTkLabel(master=VID_app, text= "UID : ",font= ("courier new", 15), text_color = "red" )
    Uid_label.place(relx = 0.2, rely = 0.5, anchor = "e" )
    Uid_db = CTkLabel(master=VID_app, text= bbuid,font= ("courier new", 15), text_color = "red" )
    Uid_db.place(relx = 0.5, rely = 0.5, anchor = "w" )

    BusId_label = CTkLabel(master=VID_app, text= "BusID : ",font= ("courier new", 15), text_color = "red" )
    BusId_label.place(relx = 0.2, rely = 0.6, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busid,font= ("courier new", 15), text_color = "red" )
    BusId_db.place(relx = 0.5, rely = 0.6, anchor = "center")

    BusNo_label = CTkLabel(master=VID_app, text= "CLASS : ",font= ("courier new", 15), text_color = "red" )
    BusNo_label.place(relx = 0.2, rely = 0.7, anchor = "e" )
    BusNo_db = CTkLabel(master=VID_app, text= bclass,font= ("courier new", 15), text_color = "red" )
    BusNo_db.place(relx = 0.5, rely = 0.7, anchor = "center" )

    Route_label = CTkLabel(master=VID_app, text= "AGE : ",font= ("courier new", 15), text_color = "red" )
    Route_label.place(relx = 0.2, rely = 0.8, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= bage,font= ("courier new", 15), text_color = "red" )
    BusId_db.place(relx = 0.5, rely = 0.8, anchor = "center" )

    Route_label = CTkLabel(master=VID_app, text= "Adress : ",font= ("courier new", 15), text_color = "red" )
    Route_label.place(relx = 0.2, rely = 0.9, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= baddr,font= ("courier new", 15), text_color = "red" )
    BusId_db.place(relx = 0.5, rely = 0.9, anchor = "center" )

    Route_label = CTkLabel(master=VID_app, text= "Status : ",font= ("courier new", 15), text_color = "red" )
    Route_label.place(relx = 0.2, rely = 0.4, anchor = "e" )
    if bstat==1:
        BusId_db = CTkLabel(master=VID_app, text= "ACTIVE!",font= ("courier new", 15), text_color = "green" )
        BusId_db.place(relx = 0.5, rely = 0.4, anchor = "center" )
    else:
        BusId_db = CTkLabel(master=VID_app, text= "EXPIRED :(",font= ("courier new", 15), text_color = "white" )
        BusId_db.place(relx = 0.5, rely = 0.4, anchor = "center" )


    VID_app.mainloop()
V_BusID()