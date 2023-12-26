import tkinter
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
import logingui
import warnings

import mysql.connector


def enroll():
    conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
    busdb=conn.cursor()
    
    enroll_app = CTk()
    enroll_app.title("Enroll")
    enroll_app.geometry("600x440")
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    
    def back():
        enroll_app.destroy()
        logingui.login()
        
	
    bg_img = ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
    image_lab = customtkinter.CTkLabel(master=enroll_app, image=bg_img)
    image_lab.pack()
    
    img2=ImageTk.PhotoImage(Image.open("back33.png"))
    back_btn = CTkButton(master=enroll_app,width=50,text="", height=10,image=img2, compound="left", fg_color="#0c9bb3",command = back)
    back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")
    
    frame = customtkinter.CTkFrame(master=image_lab, width=340,height=340, corner_radius=40)
    frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
    
    name_label = CTkLabel(master=frame,text = "Name : ", font = ("Century Gothic", 20),text_color="#FFCC70")
    name_label.place(x = 20, y = 30)
    name_entry = CTkEntry(master=frame, placeholder_text="Enter Name",width=150,text_color="#FFCC70")
    name_entry.place(x = 140,y = 30)
    
    UID_label = CTkLabel(master=frame,text = "UID : ", font = ("Century Gothic",20),text_color="#FFCC70")
    UID_label.place(x = 20, y = 70)
    UID_entry = CTkEntry(master=frame, placeholder_text="eg: U2110",width=150,text_color="#FFCC70")
    UID_entry.place(x = 140, y = 70)
    
    Pass_label = CTkLabel(master=frame,text = "Password : ", font = ("Century Gothic",20),text_color="#FFCC70")
    Pass_label.place(x = 20,y = 110)
    Pass_entry = CTkEntry(master=frame, placeholder_text="Enter password",width=150,text_color="#FFCC70")
    Pass_entry.place(x = 140, y = 110)
   
    Class_label = CTkLabel(master=frame,text = "Class : ", font = ("Century Gothic",20),text_color="#FFCC70")
    Class_label.place(x = 20, y = 150)
    Class_entry = CTkEntry(master=frame, placeholder_text="Select Class",width=150,text_color="#FFCC70")
    Class_entry.place(x = 140, y = 150)
  
    Year_label5 = CTkLabel(master=frame,text = "Year : ", font = ("Century Gothic",20),text_color="#FFCC70")
    Year_label5.place(x = 20, y = 190)
    Year_entry = CTkEntry(master=frame, placeholder_text="Select Year",width=150,text_color="#FFCC70")
    Year_entry.place(x = 140, y = 190)
   
    Addrs_label = CTkLabel(master=frame,text = "Address : ", font = ("Century Gothic",20),text_color="#FFCC70")
    Addrs_label.place(x = 20, y = 230)
    Addrs_entry = CTkEntry(master=frame, placeholder_text="Enter Address",width=150,text_color="#FFCC70")
    Addrs_entry.place(x = 140, y = 230)

    def store():
        values = {
            "Name": name_entry.get(),
            "UID": UID_entry.get(),
            "Password": Pass_entry.get(),
            "Class": Class_entry.get(),
            "Year": Year_entry.get(),
            "Address": Addrs_entry.get()
        }
        
        msg = CTkLabel(master=frame,text = "Enrollment completed!", font = ("Century Gothic",18),text_color="#FFCC70")
        busdb.execute("insert into student(Name, UID, password,class,Year,address) VALUES (%s,%s,%s,%s,%s,%s)", 
        (name_entry.get(),UID_entry.get(),Pass_entry.get(),Class_entry.get(),Year_entry.get(),Addrs_entry.get()))
        conn.commit()
        msg.place(x = 70, y = 310)

    btn = CTkButton(master=frame,text="Enroll",corner_radius=32,fg_color="#FFCC70",text_color="black",hover_color="#4158D0",command=store)
    btn.place(x = 100, y = 280)
    enroll_app.mainloop() 
    warnings.filterwarnings('ignore') 
