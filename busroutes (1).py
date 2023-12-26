import customtkinter as ctk
import warnings
import tkinter
import busdetails
import menu
from PIL import ImageTk,Image

def buss():
        try:
                ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
                ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, gree     n
        except AttributeError:
                print("Invalid command name in ctk")

        app = ctk.CTk()  #creating cutstom tkinter window
        app.geometry("800x640")
        app.title('BUS DETAILS')

        warnings.filterwarnings('ignore') 
        img1=ImageTk.PhotoImage(Image.open("rsetlogo2.png"))
        l1=ctk.CTkLabel(master=app,image=img1)
        l1.pack()
        def cback():
                app.destroy()
                menu.main()


        warnings.filterwarnings('ignore') 
        img2=ImageTk.PhotoImage(Image.open("back33.png"))
        back_btn = ctk.CTkButton(master=app,width=50,text="", height=10,image=img2, compound="left", fg_color="#0c9bb3",command = cback)
        back_btn.place(relx = 0.1, rely = 0.05, anchor = "e")
        #creating custom frame
        frame=ctk.CTkFrame(master=l1, width=320, height=360,bg_color="transparent",corner_radius=30)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2=ctk.CTkLabel(master=frame, text="BUS ROUTES",font=('Century Gothic',20))
        l2.place(x=50, y=45)
        #combobox_var = ctk.StringVar(value="route")  # set initial value
        
        def combobox_callback(choice):
                print("combobox dropdown clicked:", choice)
                r_no=choice[9]
                app.destroy()
                busdetails.details(r_no)
        
        combobox = ctk.CTkComboBox(master=frame, values=["Route no 1: Aluva - Campus", "Route no 2: Perumbavur - Campus","Route no 3: Vytilla - Campus"
                                        ,"Route no 4: Edappally - Campus","Route no 5: Thripunithura - Campus","Route no 6: Angamaly - Campus",
                                        "Route no 7: Kaloor - Campus","Route no 8: Desom - Campus"]
                                        ,command=combobox_callback,button_color="green",dropdown_fg_color="green",dropdown_hover_color="darkgreen",
                                        dropdown_text_color="white",border_color="green",width=220
                                        #variable=combobox_var
        )
        combobox.place(x=50, y=110)

        app.mainloop()