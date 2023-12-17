import tkinter
import customtkinter as ctk
import warnings
import logingui
from PIL import ImageTk,Image

def main():
    
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("dark-blue")  


    root = ctk.CTk()  
    root.geometry("600x440")
    root.title('BUS DETAILS')



    def button_function():
        root.destroy()            
        w = ctk.CTk()  
        w.geometry("1280x720")
        w.title('Welcome')
        l1=ctk.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
        l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
        w.mainloop()

    def bus_app_gui():
        bus_app_window = ctk.CTk()
        bus_app_window.title("Bus Application")
        bus_app_window.geometry("300x200")
        bus_app_window.mainloop()

    def fees_payment_gui():
        fees_payment_window = ctk.CTk()
        fees_payment_window.title("Fees Payment")
        fees_payment_window.geometry("300x200")
        fees_payment_window.mainloop()

    def profile_gui():
        profile_window = ctk.CTk()
        profile_window.title("Profile")
        profile_window.geometry("300x200")
        profile_window.mainloop()

    def bus_details_gui():
        bus_details_window = ctk.CTk()
        bus_details_window.title("Bus Details")
        bus_details_window.geometry("300x200")
        bus_details_window.mainloop()

    warnings.filterwarnings('ignore') 
    img1=ImageTk.PhotoImage(Image.open("C:\\Users\\MY PC\\OneDrive\\Desktop\\Example\\rsetlogo2.png"))
    l1=ctk.CTkLabel(master=root,image=img1)
    l1.pack()


    frame=ctk.CTkFrame(master=l1, width=320, height=360, corner_radius=40)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="MENU",font=('Century Gothic',20))
    l2.place(x=50, y=45)

    button2 = ctk.CTkButton(master=frame, width=220, text="Virtual ID", command=profile_gui, corner_radius=30)
    button2.place(x=50, y=110)

    button2 = ctk.CTkButton(master=frame, width=220, text="Application", command=bus_app_gui, corner_radius=30)
    button2.place(x=50, y=150)

    button3 = ctk.CTkButton(master=frame, width=220, text="Fees Payment", command=bus_details_gui, corner_radius=30)
    button3.place(x=50, y=190)


    button4 = ctk.CTkButton(master=frame, width=220, text="Bus Details", command=bus_details_gui, corner_radius=30)
    button4.place(x=50, y=230)
    #,bg_color="transparent",fg_color="transparent",text_color="blue"


    root.mainloop()



if __name__== "__main__":
     my=logingui.login()
     main()
