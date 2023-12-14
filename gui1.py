
# Import module 
from tkinter import *
import customtkinter as CTk


# the appearance mode of the system
ctk.set_appearance_mode("Dark") 

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue 
ctk.set_default_color_theme(color_string="dark-blue") 

d1 = {"u210":"pass"}
def printf():
    user = username.get()
    passw = password.get()
    if user in d1 and (d1[user]==passw):
        print("sucess")
        root.destroy()
        gui2()
    else:
        clearall()
        canvas1.create_text( 100, 330, text = "wrong login credentials",font=("Franklin Gothic Medium", "12"),anchor="n")

    # else the login credientials are wrong try and retry

def gui2():
   
    root2=cTk()
    root2.geometry("600x600")
    bg1 = PhotoImage(file = "white.png")
    canvas2 = Canvas( root2, width = 900, 
                    height = 900 ) 
    canvas2.pack(fill = "both", expand = True) 
    canvas2.create_image( 0, 0, image = bg1, 
                        anchor = "nw")
    canvas2.create_text( 50, 10, text = "Welcome",fill="maroon",font=("Franklin Gothic Medium", "12"),anchor="n")
    canvas2.create_text( 50, 70, text=" PROFILE",fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n") 
    canvas2.create_text( 50, 130, text="APPLICATION ",fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n") 

    button4 = Button( root, text = "PROFILE",fg="BLACK",bg="white")

    button4_canvas = canvas2.create_window( 100, 190, anchor = "nw",
                                        height=50,
                                        width=50,  
									window = button4) 
    root2.mainloop()


def clearall():

 
    # whole content of entry boxes is deleted 
    username.delete(0, END)   
    password.delete(0, END) 
    
    '''  
    # set focus on the principal_field entry box  
    principal_field.focus_set() 
     '''


# Create object 
root = CTk() 

# Adjust size 
root.geometry("400x400") 


# Add image file 
bg = PhotoImage(file = "rset1.png")

# Create Canvas 
canvas1 = Canvas( root, width = 900, 
				height = 900 ) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 0, 0, image = bg,
					anchor="nw") 

# Add Text 
canvas1.create_text( 50, 10, text = "Welcome",fill="maroon",font=("Franklin Gothic Medium", "12"),anchor="n")
canvas1.create_text( 50, 70, text=" USERID:   ",fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n") 
canvas1.create_text( 50, 130, text="PASSWORD: ",fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n") 

# Create Buttons 
#button1 = Button( root, text = "Exit") 
button3 =CTk.CTkButton( root, text = "LOGIN",fg="white",bg="maroon",command=printf)
#create entry for accepting the inputs from the user
username=CTk.CTkEntry(root,width=100,fg="white",bg="maroon")
password=CTk.CTkEntry(root,width=100,fg="white",bg="maroon")
#button2 = Button( root, text = "Reset") 

# Display Buttons 
button1_canvas = canvas1.create_window(  100,70,
									anchor = "nw",
                                    height=30,
                                    width=100, 
									window = username) 

button2_canvas = canvas1.create_window( 100, 130, 
									anchor = "nw",
                                    height=30,
                                    width=100,
									window = password) 

button3_canvas = canvas1.create_window( 100, 190, anchor = "nw",
                                        height=50,
                                        width=50,  
									window = button3) 

root.mainloop() 
