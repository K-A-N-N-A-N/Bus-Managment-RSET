import tkinter
import customtkinter as ctk
import warnings
from PIL import ImageTk,Image

def login():
    li=[]
    try:
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
    except AttributeError:
        print("Invalid command name in customtkinter")

    app = ctk.CTk()  #creating cutstom tkinter window
    app.geometry("600x440")
    app.title('Login')

    def button_function():
        busdb=[("u2101","pass")]
        user = userEntry.get()
        passw = passwEntry.get()
        print(user,passw)
        for row in busdb:
            if row[0]==user and row[1]==passw:
                li.append(user)
                li.append(passw)
                app.destroy()
            else:
                userEntry.delete(0, ctk.END)
                passwEntry.delete(0, ctk.END)
                l3=ctk.CTkLabel(master=frame, text="wrong login credentials",font=('Century Gothic',20))
                l3.place(x=50, y=195)

    warnings.filterwarnings('ignore') 
    img1=ImageTk.PhotoImage(Image.open("C:\\Users\\MY PC\\OneDrive\\Desktop\\Example\\rsetlogo.png"))
    l1=ctk.CTkLabel(master=app,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=360, corner_radius=30)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
    l2.place(x=50, y=45)

    userEntry=ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    userEntry.place(x=50, y=110)

    passwEntry=ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    passwEntry.place(x=50, y=165)

    #Create custom button
    button1 = ctk.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
    button1.place(x=50, y=240)

    app.mainloop()
    return li
