from customtkinter import *
from PIL import Image

import mysql.connector
conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='bustrial')
busdb=conn.cursor()

def V_BusID():
    bbuid="U2101"
    VID_app = CTk()
    VID_app.geometry("500x400")
    set_appearance_mode("white")
    
    busdb.execute('select bstudents.UID,bstudents.BusID,bstudents.BusNo,busdet.Route from bstudents join busdet on bstudents.Busno=busdet.Busno')
    for row in busdb:
         if row[0]==bbuid:
              busid=row[1]
              busno=row[2]
              busroute=row[3]
              

    #frame = CTkFrame(master=app, fg_color="red", border_color="blue", border_width=2)
    #frame.pack(expand = True)

    logo_image = CTkImage(dark_image=Image.open("background_1.png"), size = (500,80))

    logo_label = CTkLabel(VID_app,image = logo_image, text="")
    logo_label.grid(row = 0, column = 0)

    Ttl_label = CTkLabel(master=VID_app, text= "Virtual Bus ID",font= ("courier new", 30), text_color = "red" )
    Ttl_label.place(relx = 0.5, rely = 0.3, anchor = "center" )

    barcode_image = CTkImage(dark_image=Image.open("barcode.png"), size = (500,80))

    #barcode_label = CTkLabel(VID_app,image = barcode_image, text="")
    #barcode_label.grid(row = 0, column = 0)

    Uid_label = CTkLabel(master=VID_app, text= "UID : uii",font= ("courier new", 15), text_color = "red" )
    Uid_label.place(relx = 0.2, rely = 0.5, anchor = "e" )
    Uid_db = CTkLabel(master=VID_app, text= bbuid,font= ("courier new", 15), text_color = "red" )
    Uid_db.place(relx = 0.5, rely = 0.5, anchor = "w" )

    BusId_label = CTkLabel(master=VID_app, text= "Bus ID : ",font= ("courier new", 15), text_color = "red" )
    BusId_label.place(relx = 0.2, rely = 0.6, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busid,font= ("courier new", 15), text_color = "red" )
    BusId_db.place(relx = 0.5, rely = 0.6, anchor = "center")

    BusNo_label = CTkLabel(master=VID_app, text= "Bus No : ",font= ("courier new", 15), text_color = "red" )
    BusNo_label.place(relx = 0.2, rely = 0.7, anchor = "e" )
    BusNo_db = CTkLabel(master=VID_app, text= busno,font= ("courier new", 15), text_color = "red" )
    BusNo_db.place(relx = 0.5, rely = 0.7, anchor = "center" )

    Route_label = CTkLabel(master=VID_app, text= "Route : ",font= ("courier new", 15), text_color = "red" )
    Route_label.place(relx = 0.2, rely = 0.8, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busroute,font= ("courier new", 15), text_color = "red" )
    BusId_db.place(relx = 0.5, rely = 0.8, anchor = "center" )

    VID_app.mainloop()

def Pay():
    Pay_app = CTk()
    Pay_app.geometry("500x300")
    set_appearance_mode("dark")

    Ttl_label = CTkLabel(master=Pay_app, text= "Register / Payment",font= ("courier new", 30), text_color = "red" )
    Ttl_label.place(relx = 0.5, rely = 0.1, anchor = "center" )

    Route_entry = CTkEntry(master=Pay_app, placeholder_text="Enter Route", width = 300, text_color="#FFCC70")
    Route_entry.place(relx = 0.5, rely = 0.3, anchor = "center")

    Rate_entry = CTkEntry(master=Pay_app, placeholder_text="Rate..", width = 300, text_color="#FFCC70")
    Rate_entry.place(relx = 0.5, rely = 0.45, anchor = "center")

    def check():
        route=Route_entry.get()
        busdb.execute("select * from busdet")
        flagr=0 
        for row in busdb:
            if route ==row[1]:
                flagr=1
                if row[3]>0:
                    print("Seats are Available")
                else:
                    print("Unavailable")
        if flagr==0:
                print("given route doesn't exist")            
        

    def pay():
        route=Route_entry.get()
        busdb.execute("select * from busdet")
        flagr=0 
        for row in busdb:
            if route ==row[1]:
                flagr=1
                if row[3]>0:
                    print("payment succesfull")
                else:
                    print("seats Unavailable")
        if flagr==0:
                print("given route doesn't exist") 

    Check_btn = CTkButton(master=Pay_app, text = "Check", corner_radius=25, fg_color="#4158D0", hover_color="#C850C0",
                          border_color="#FFCC70", border_width= 2, command=check)
    Check_btn.place(relx = 0.4, rely = 0.6, anchor = "e")

    Check_btn = CTkButton(master=Pay_app, text = "Pay", corner_radius=25, fg_color="#4158D0", hover_color="#C850C0",
                          border_color="#FFCC70", border_width= 2, command=pay)
    Check_btn.place(relx = 0.9, rely = 0.6, anchor = "e")

    Pay_app.mainloop()

V_BusID()
#Pay()
