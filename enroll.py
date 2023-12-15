from customtkinter import *

import mysql.connector
conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='bustrial')
busdb=conn.cursor()

def enroll():
    enroll_app = CTk()
    enroll_app.geometry("500x400")
    set_appearance_mode("dark")

    label1 = CTkLabel(master=enroll_app,text = "Name", font = ("Courier New",20),text_color="#FFCC70")
    label1.place(relx=0.3,rely=0.2,anchor="e")
    label2 = CTkLabel(master=enroll_app,text = "UID", font = ("Courier New",20),text_color="#FFCC70")
    label2.place(relx=0.3,rely=0.3,anchor="e")
    label3 = CTkLabel(master=enroll_app,text = "Password", font = ("Courier New",20),text_color="#FFCC70")
    label3.place(relx=0.3,rely=0.4,anchor="e")
    label4 = CTkLabel(master=enroll_app,text = "Class", font = ("Courier New",20),text_color="#FFCC70")
    label4.place(relx=0.3,rely=0.5,anchor="e")
    label5 = CTkLabel(master=enroll_app,text = "Age", font = ("Courier New",20),text_color="#FFCC70")
    label5.place(relx=0.3,rely=0.6,anchor="e")
    label6 = CTkLabel(master=enroll_app,text = "Address", font = ("Courier New",20),text_color="#FFCC70")
    label6.place(relx=0.3,rely=0.7,anchor="e")

    entry1 = CTkEntry(master=enroll_app, placeholder_text="Enter Name",width=150,text_color="#FFCC70")
    entry1.place(relx=0.7,rely=0.2,anchor="e")
    entry2 = CTkEntry(master=enroll_app, placeholder_text="eg: U2103135",width=150,text_color="#FFCC70")
    entry2.place(relx=0.7,rely=0.3,anchor="e")
    entry3 = CTkEntry(master=enroll_app, placeholder_text="Enter password",width=150,text_color="#FFCC70")
    entry3.place(relx=0.7,rely=0.4,anchor="e")
    entry4 = CTkEntry(master=enroll_app, placeholder_text="Select Class",width=150,text_color="#FFCC70")
    entry4.place(relx=0.7,rely=0.5,anchor="e")
    entry5 = CTkEntry(master=enroll_app, placeholder_text="Select Age",width=150,text_color="#FFCC70")
    entry5.place(relx=0.7,rely=0.6,anchor="e")
    entry6 = CTkEntry(master=enroll_app, placeholder_text="Enter Address",width=150,text_color="#FFCC70")
    entry6.place(relx=0.7,rely=0.7,anchor="e")

    def store():
        values = {
            "Name": entry1.get(),
            "UID": entry2.get(),
            "Password": entry3.get(),
            "Class": entry4.get(),
            "Age": entry5.get(),
            "Address": entry6.get()
        }
        busdb.execute('select count(*)from student')
        for row in busdb:
            num = row[0]+1
            BUID="B0"+str(num)
        msg = CTkLabel(master=enroll_app,text = "Enrollment completed!", font = ("Courier New",18),text_color="#FFCC70")
        busdb.execute("insert into student(Name, UID, password,class,age,address,BusID) VALUES (%s,%s,%s,%s,%s,%s,%s)", (entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),BUID))
        conn.commit()
        msg.place(relx=0.5,rely=0.9,anchor="center")

    btn = CTkButton(master=enroll_app,text="Enroll",corner_radius=32,fg_color="#FFCC70",hover_color="#4158D0",command=store)
    btn.place(relx=0.7,rely=0.8,anchor="e")
    enroll_app.mainloop() 
enroll()