import tkinter
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk

def register():
    reg_app = CTk()
    reg_app.title("Register / Pay")
    reg_app.geometry("600x440")
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    bg_img = ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    img_l1 = customtkinter.CTkLabel(master=reg_app,image=bg_img)
    img_l1.pack()

    back_btn = CTkButton(master=reg_app,width=50, height=10, text = "<- Back", compound="left", corner_radius=40, fg_color="black")
    back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")

    frame = customtkinter.CTkFrame(master=img_l1,width=320, height=340, corner_radius=40)
    frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

    Ttl_label = CTkLabel(master=frame, text= "  Register / Payment",font= ("Century Gothic", 20))
    Ttl_label.place(x = 50, y = 45)
    
    Route_entry = CTkEntry(master=frame,width=220, placeholder_text="Enter Route")
    Route_entry.place(x = 50, y = 110)

    def check():
        x = "Y" # for checking with dbms
        y = 1500 # for sending rate to the label
        if x == "Y":
            Rate_entry = CTkEntry(master=frame,width=220, placeholder_text=y)
            Rate_entry.place(x = 50, y = 145)

            Note = CTkLabel(master=frame,text="Seats Available",font=('Century Gothic',20))
            Note.place(x = 50, y = 240)
            return 1
        else:
            Note = CTkLabel(master=frame,text="Seats Unavailable",font=('Century Gothic',20))
            Note.place(x = 50, y = 240)
            Note = CTkLabel(master=frame,text="Route Doesnt Exist. Enter valid Route",font=('Century Gothic',20))
            Note.place(x = 50, y = 240)
            return 0

    def pay():
        chk = check()
        if chk == 1:
            Note = CTkLabel(master=frame,text="Payment Completed",font=('Century Gothic',20))
            Note.place(x = 50, y = 240)
    
    Check_btn = CTkButton(master=frame,width=100, height=20, text = "Check", compound="left", corner_radius=6, fg_color="white", text_color="black", command=check)
    Check_btn.place(x = 50, y = 200)

    pay_btn = CTkButton(master=frame,width=100, height=20, text = "Pay", compound="left", corner_radius=6, fg_color="white", text_color="black", command=pay)
    pay_btn.place(x = 170, y = 200)

    ''' 
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
    '''

    #Check_btn = CTkButton(master=reg_app, text = "Check", corner_radius=25, fg_color="#4158D0", hover_color="#6450c8",
                          #border_color="#FFCC70", border_width= 2, command=check)
    #Check_btn.place(relx = 0.4, rely = 0.6, anchor = "e")

    #Check_btn = CTkButton(master=reg_app, text = "Pay", corner_radius=25, fg_color="#4158D0", hover_color="#6450c8",
                          #border_color="#FFCC70", border_width= 2, command=pay)
    #Check_btn.place(relx = 0.9, rely = 0.6, anchor = "e")

    reg_app.mainloop()

#register()