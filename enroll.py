from customtkinter import *
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
    label4 = CTkLabel(master=enroll_app,text = "Branch", font = ("Courier New",20),text_color="#FFCC70")
    label4.place(relx=0.3,rely=0.5,anchor="e")
    label5 = CTkLabel(master=enroll_app,text = "Division", font = ("Courier New",20),text_color="#FFCC70")
    label5.place(relx=0.3,rely=0.6,anchor="e")
    label6 = CTkLabel(master=enroll_app,text = "Address", font = ("Courier New",20),text_color="#FFCC70")
    label6.place(relx=0.3,rely=0.7,anchor="e")

    entry1 = CTkEntry(master=enroll_app, placeholder_text="Enter Name",width=150,text_color="#FFCC70")
    entry1.place(relx=0.7,rely=0.2,anchor="e")
    entry2 = CTkEntry(master=enroll_app, placeholder_text="eg: U2103135",width=150,text_color="#FFCC70")
    entry2.place(relx=0.7,rely=0.3,anchor="e")
    entry3 = CTkEntry(master=enroll_app, placeholder_text="Enter password",width=150,text_color="#FFCC70")
    entry3.place(relx=0.7,rely=0.4,anchor="e")
    entry4 = CTkEntry(master=enroll_app, placeholder_text="Select branch",width=150,text_color="#FFCC70")
    entry4.place(relx=0.7,rely=0.5,anchor="e")
    entry5 = CTkEntry(master=enroll_app, placeholder_text="Select Division",width=150,text_color="#FFCC70")
    entry5.place(relx=0.7,rely=0.6,anchor="e")
    entry6 = CTkEntry(master=enroll_app, placeholder_text="Enter Address",width=150,text_color="#FFCC70")
    entry6.place(relx=0.7,rely=0.7,anchor="e")

    def store():
        values = {
            "Name": entry1.get(),
            "Branch": entry2.get(),
            "Year": entry3.get(),
            "Division": entry4.get(),
            "UID": entry5.get(),
            "Password": entry6.get()
        }
        msg = CTkLabel(master=enroll_app,text = "Enrollment completed!", font = ("Courier New",18),text_color="#FFCC70")
        msg.place(relx=0.5,rely=0.9,anchor="center")

    btn = CTkButton(master=enroll_app,text="Enroll",corner_radius=32,fg_color="#FFCC70",hover_color="#4158D0",command=store)
    btn.place(relx=0.7,rely=0.8,anchor="e")
    enroll_app.mainloop()
enroll()
