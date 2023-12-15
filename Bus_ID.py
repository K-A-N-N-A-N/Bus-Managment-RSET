from customtkinter import *
from PIL import Image

#import mysql.connector
#conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='bustrial')
#busdb=conn.cursor()
#busdd=conn.cursor()

def V_BusID():
    bbuid="U2101"
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

    logo_image = CTkImage(dark_image=Image.open("VBid.png"), size = (500,600))

    logo_label = CTkLabel(VID_app,image = logo_image, text="")
    logo_label.grid(row = 0, column = 0)

    Ttl_label = CTkLabel(master=VID_app, text= "Virtual Bus ID",font= ("courier new", 40), text_color = "maroon")
    Ttl_label.place(relx = 0.5, rely = 0.22, anchor = "center" )

    name_label = CTkLabel(master=VID_app, text= "Kannan MD",font= ("courier new", 30), text_color = "black" )
    name_label.place(relx = 0.5, rely = 0.315, anchor = "center" )

    Uid_label = CTkLabel(master=VID_app, text= "   UID : ",font= ("courier new", 17), text_color = "maroon" )
    Uid_label.place(relx = 0.3, rely = 0.55, anchor = "e" )
    Uid_db = CTkLabel(master=VID_app, text= bbuid,font= ("courier new", 17), text_color = "maroon" )
    Uid_db.place(relx = 0.5, rely = 0.55, anchor = "w" )

    BusId_label = CTkLabel(master=VID_app, text= "Bus ID : ",font= ("courier new", 17), text_color = "maroon" )
    BusId_label.place(relx = 0.3, rely = 0.62, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busid,font= ("courier new", 17), text_color = "maroon" )
    BusId_db.place(relx = 0.5, rely = 0.62, anchor = "center")

    BusNo_label = CTkLabel(master=VID_app, text= "Bus No : ",font= ("courier new", 17), text_color = "maroon" )
    BusNo_label.place(relx = 0.3, rely = 0.69, anchor = "e" )
    BusNo_db = CTkLabel(master=VID_app, text= busno,font= ("courier new", 17), text_color = "maroon" )
    BusNo_db.place(relx = 0.5, rely = 0.79, anchor = "center" )

    Route_label = CTkLabel(master=VID_app, text= " Route : ",font= ("courier new", 17), text_color = "maroon" )
    Route_label.place(relx = 0.3, rely = 0.76, anchor = "e" )
    BusId_db = CTkLabel(master=VID_app, text= busroute,font= ("courier new", 17), text_color = "maroon" )
    BusId_db.place(relx = 0.5, rely = 0.76, anchor = "center" )

    VID_app.mainloop()

def register():
    reg_app = CTk()
    reg_app.title("Register / Pay")
    reg_app.geometry("500x300")
    set_appearance_mode("dark")

    Ttl_label = CTkLabel(master=reg_app, text= "Register / Payment",font= ("courier new", 30), text_color = "red" )
    Ttl_label.place(relx = 0.5, rely = 0.1, anchor = "center" )

    Route_entry = CTkEntry(master=reg_app, placeholder_text="Enter Route", width = 300, text_color="#FFCC70")
    Route_entry.place(relx = 0.5, rely = 0.3, anchor = "center")

    Rate_entry = CTkEntry(master=reg_app, placeholder_text="Rate..", width = 300, text_color="#FFCC70")
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
                    print("Rate is :" + str(row[2]))

                else:
                    print("Unavailable")
        if flagr==0:
                print("given route doesn't exist")            
        
        
    def pay():
        route=Route_entry.get()
        busdb.execute('select count(*)from student')
        for row in busdb:
            num = row[0]+1
            BUID="B0"+str(num)
        busdb.execute("select * from busdet")
        flagr=0 
        for row in busdb:
            if route ==row[1]:
                flagr=1
                if row[3]>0:
                    print("payment succesfull")
                    print("Your BusID =" + BUID )    
                else:
                    print("seats Unavailable")
        if flagr==0:
                print("given route doesn't exist") 
    

    Check_btn = CTkButton(master=reg_app, text = "Check", corner_radius=25, fg_color="#4158D0", hover_color="#6450c8",
                          border_color="#FFCC70", border_width= 2, command=check)
    Check_btn.place(relx = 0.4, rely = 0.6, anchor = "e")

    Check_btn = CTkButton(master=reg_app, text = "Pay", corner_radius=25, fg_color="#4158D0", hover_color="#6450c8",
                          border_color="#FFCC70", border_width= 2, command=pay)
    Check_btn.place(relx = 0.9, rely = 0.6, anchor = "e")

    reg_app.mainloop()

V_BusID()
register()
