import tkinter
import customtkinter
import logingui
import menu
import warnings
import mysql.connector
from customtkinter import *
from PIL import Image, ImageTk

rflag = 0
busn=0

def register():
    conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
    busdb=conn.cursor()
    busdb.execute('select * from current')
    for row in busdb:
        if row[1]==7:
            UId=row[0] 
    reg_app = CTk()
    reg_app.title("Register / Pay")
    reg_app.geometry("600x440")
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    def back():
        reg_app.destroy()
        menu.main()
    warnings.filterwarnings('ignore') 
    bg_img = ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    img_l1 = customtkinter.CTkLabel(master=reg_app,image=bg_img)
    img_l1.pack()


    warnings.filterwarnings('ignore') 
    img2=ImageTk.PhotoImage(Image.open("back33.png"))
    back_btn = CTkButton(master=reg_app,width=50,text="", height=10,image=img2, compound="left", fg_color="#0c9bb3",command = back)
    back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")

    frame = customtkinter.CTkFrame(master=img_l1,width=320, height=340, corner_radius=40)
    frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

    Ttl_label = CTkLabel(master=frame, text= "  Register / Payment",font= ("Century Gothic", 20))
    Ttl_label.place(x = 50, y = 45)
    
    Route_entry = CTkEntry(master=frame,width=220, placeholder_text="Enter Route")
    Route_entry.place(x = 50, y = 110)

    def check():
        global rflag
        global busn
        route=Route_entry.get()
        flag= 0
        rflag = 0
        busdb.execute('select * from bus')
        Note1 = CTkLabel(master=frame,text="",font=('Century Gothic',20))
        Note2 = CTkLabel(master=frame,text="",font=('Century Gothic',20))
        Note3 = CTkLabel(master=frame,text="",font=('Century Gothic',20))
        for row in busdb:
            if row[1]==route:
                flag = 1
                if row[3]>0:
                    rate = row[2]
                    Rate_entry = CTkEntry(master=frame,width=220, placeholder_text=rate)
                    Rate_entry.place(x = 50, y = 145)
                    Note2.destroy()
                    Note3.destroy()
                    rflag = 1
                    busn = row[0]
                    Note1 = CTkLabel(master=frame,text=" Seats Are Available",font=('Century Gothic',20))
                    Note1.place(x = 50, y = 240)
                    
                else:
                    Note1.destroy()
                    Note3.destroy()
                    Note2 = CTkLabel(master=frame,text="Seats Unavailable",font=('Century Gothic',20))
                    Note2.place(x = 50, y = 240)
        if flag==0:
            Note1.destroy()
            Note2.destroy()
            Note3 = CTkLabel(master=frame,text="Route Does Not Exist ",font=('Century Gothic',20))
            Note3.place(x = 50, y = 240)

    def pay():
        if rflag == 1:
            busdb.execute('select count(*) from bstudent')
            for row in busdb:
                num = row[0]+1
                BUID= "B0"+str(num)
            busdb.execute('select * from student')
            rows = busdb.fetchall()

            for row in rows:
                if row[0]==UId:
                    if row[2]==1:
                        Note = CTkLabel(master=frame,text="Already paid",font=('Century Gothic',20))
                        Note.place(x = 50, y = 270)
                    else:
                        busdb.execute('insert into bstudent values (%s,%s,%s)',(BUID,UId,busn))
                        Note = CTkLabel(master=frame,text="Payment Completed",font=('Century Gothic',20))
                        Note.place(x = 50, y = 270)
                        busdb.execute('update student set payment_status = 1 where UID = %s',(UId,))    
                        conn.commit()

    Check_btn = CTkButton(master=frame,width=100, height=20, text = "Check", compound="left", corner_radius=6, fg_color="white", text_color="black", command=check)
    Check_btn.place(x = 50, y = 200)

    pay_btn = CTkButton(master=frame,width=100, height=20, text = "Pay", compound="left", corner_radius=6, fg_color="white", text_color="black", command=pay)
    pay_btn.place(x = 170, y = 200)

    reg_app.mainloop()