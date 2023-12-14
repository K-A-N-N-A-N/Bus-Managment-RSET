from customtkinter import *
from PIL import Image

def V_BusID():
    VID_app = CTk()
    VID_app.geometry("500x400")
    set_appearance_mode("white")

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

    Uid_label = CTkLabel(master=VID_app, text= "UID : ",font= ("courier new", 15), text_color = "red" )
    Uid_label.place(relx = 0.2, rely = 0.5, anchor = "e" )

    BusId_label = CTkLabel(master=VID_app, text= "Bus ID : ",font= ("courier new", 15), text_color = "red" )
    BusId_label.place(relx = 0.2, rely = 0.6, anchor = "e" )

    BusNo_label = CTkLabel(master=VID_app, text= "Bus No : ",font= ("courier new", 15), text_color = "red" )
    BusNo_label.place(relx = 0.2, rely = 0.7, anchor = "e" )

    Route_label = CTkLabel(master=VID_app, text= "Route : ",font= ("courier new", 15), text_color = "red" )
    Route_label.place(relx = 0.2, rely = 0.8, anchor = "e" )

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
        space = "Y"
        if (space == "Y"):
            print("Space Available")
        else:
            print("No Space aavailable")

    def pay():
        space = "Y"
        if (space == "Y"):
            print("Payment Successful")
        else:
            print("No Seats Available")

    Check_btn = CTkButton(master=Pay_app, text = "Check", corner_radius=25, fg_color="#4158D0", hover_color="#C850C0",
                          border_color="#FFCC70", border_width= 2, command=check)
    Check_btn.place(relx = 0.4, rely = 0.6, anchor = "e")

    Check_btn = CTkButton(master=Pay_app, text = "Pay", corner_radius=25, fg_color="#4158D0", hover_color="#C850C0",
                          border_color="#FFCC70", border_width= 2, command=pay)
    Check_btn.place(relx = 0.9, rely = 0.6, anchor = "e")

    Pay_app.mainloop()

V_BusID()
#Pay()
