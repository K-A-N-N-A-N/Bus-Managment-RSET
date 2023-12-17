from customtkinter import *
from PIL import Image

import mysql.connector
conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='bustrial')
busdb=conn.cursor()
#busdd=conn.cursor()

def V_BusID():
    bbuid="U2103"
    VID_app = CTk()
    VID_app.title("Virtual Bus ID")
    VID_app.geometry("500x600")
    set_appearance_mode("Light")
    set_default_color_theme("green")
    
    busdb.execute('select bstudents.UID,bstudents.BusID,bstudents.BusNo,busdet.Route from bstudents join busdet on bstudents.Busno=busdet.Busno')
    for row in busdb:
         if row[0]==bbuid:
              busid=row[1]
              busno=row[2]
              busroute=row[3]
    busdb.execute("select * from student")
    for row in busdb:
         if row[0]==bbuid:   
            bname = row[7]      

    logo_image = CTkImage(dark_image=Image.open("VBid.png"), size = (500,600))

    logo_label = CTkLabel(VID_app,image = logo_image, text="")
    logo_label.grid(row = 0, column = 0)

    Ttl_label = CTkLabel(master=VID_app, text= "Virtual Bus ID",font= ("courier new", 40), text_color = "maroon")
    Ttl_label.place(relx = 0.5, rely = 0.22, anchor = "center" )

    name_label = CTkLabel(master=VID_app, text= bname,font= ("courier new", 30), text_color = "black" )
    name_label.place(relx = 0.5, rely = 0.315, anchor = "center" )

    Uid_label = CTkLabel(master=VID_app, text= "   UID : ",font= ("courier new", 17), text_color = "maroon" )
    Uid_label.place(relx = 0.3, rely = 0.55, anchor = "e" )
    Uid_db = CTkLabel(master=VID_app, text= bbuid,font= ("courier new", 17), text_color = "maroon" )
    Uid_db.place(relx = 0.45, rely = 0.55, anchor = "w" )

    BusId_label = CTkLabel(master=VID_app, text= "Bus ID : ",font= ("courier new", 17), text_color = "maroon" )
    BusId_label.place(relx = 0.3, rely = 0.62, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busid,font= ("courier new", 17), text_color = "maroon" )
    BusId_db.place(relx = 0.5, rely = 0.62, anchor = "center")

    BusNo_label = CTkLabel(master=VID_app, text= "Bus No : ",font= ("courier new", 17), text_color = "maroon" )
    BusNo_label.place(relx = 0.3, rely = 0.69, anchor = "e" )
    BusNo_db = CTkLabel(master=VID_app, text= busno,font= ("courier new", 17), text_color = "maroon" )
    BusNo_db.place(relx = 0.5, rely = 0.69, anchor = "center" )

    Route_label = CTkLabel(master=VID_app, text= " Route : ",font= ("courier new", 17), text_color = "maroon" )
    Route_label.place(relx = 0.3, rely = 0.76, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busroute,font= ("courier new", 17), text_color = "maroon" )
    BusId_db.place(relx = 0.5, rely = 0.76, anchor = "center" )

    VID_app.mainloop()

V_BusID()
