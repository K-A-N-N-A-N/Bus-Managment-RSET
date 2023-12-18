import tkinter
import customtkinter as ctk
import warnings
from PIL import ImageTk,Image
import SignUp
import menu
import mysql.connector


def login():
    conn = mysql.connector.connect(host='localhost',username='root',password='456ASDcvb###',database='RSETbus')
    busdb=conn.cursor()
    try:
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
    except AttributeError:
        print("Invalid command name in customtkinter")

    app = ctk.CTk()  #creating cutstom tkinter window
    app.geometry("600x440")
    app.title('Login')

    def button_function():

        busdb.execute('SELECT * FROM student')
        User = userEntry.get()
        passw = passwEntry.get()
        rows = busdb.fetchall()

        for row in rows:
            if row[0]==User and row[1]==passw:
                busdb.execute('UPDATE current SET ID = %s WHERE i = 7', (User,))
                conn.commit()
                app.destroy()
                menu.main()
            else:
                userEntry.delete(0, ctk.END)
                passwEntry.delete(0, ctk.END)
                l3=ctk.CTkLabel(master=frame, text="wrong login credentials",font=('Century Gothic',20))
                l3.place(x=50, y=195)
               
    def SignBtn_function():
        app.destroy()
        SignUp.enroll()

    warnings.filterwarnings('ignore') 
    img1=ImageTk.PhotoImage(Image.open("rsetlogo.png"))
    l1=ctk.CTkLabel(master=app,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=360,bg_color="transparent",corner_radius=30)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
    l2.place(x=50, y=45)

    userEntry=ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    userEntry.place(x=50, y=110)

    passwEntry=ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    passwEntry.place(x=50, y=165)

    #Create custom button
    loginBtn = ctk.CTkButton(master=frame, width=110, text="Login", command=button_function, corner_radius=6)
    loginBtn.place(x=40, y=240)

    SignBtn = ctk.CTkButton(master=frame, width=110, text="Sign Up", command=SignBtn_function, corner_radius=6)
    SignBtn.place(x=170, y=240)

    app.mainloop()
    conn.commit()

if __name__ == "__main__":
    login()
