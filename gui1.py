# Import module 
from tkinter import *
def printf():
    print(username.get())
    print(password.get())

# Create object 
root = Tk() 

# Adjust size 
root.geometry("400x400") 

# Add image file 
bg = PhotoImage(file = "rset.png")

# Create Canvas 
canvas1 = Canvas( root, width = 900, 
				height = 900 ) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 0, 0, image = bg, 
					anchor = "nw") 

# Add Text 
canvas1.create_text( 200, 230, text = "Welcome",font=("Franklin Gothic Medium", "12"),anchor="n")
canvas1.create_text( 100, 10, text=" USERID:   ",fill="black",font=("Franklin Gothic Medium", "10"),anchor="n") 
canvas1.create_text( 100, 70, text="PASSWORD: ",fill="black",font=("Franklin Gothic Medium", "10"),anchor="n") 

# Create Buttons 
#button1 = Button( root, text = "Exit") 
button3 = Button( root, text = "LOGIN",fg="white",bg="black",command=printf)
#create entry for accepting the inputs from the user
username=Entry(root,width=100,fg="white",bg="black")
password=Entry(root,width=100,fg="white",bg="black")
#button2 = Button( root, text = "Reset") 

# Display Buttons 
button1_canvas = canvas1.create_window(  150,10,
									anchor = "nw",
                                    height=30,
                                    width=100, 
									window = username) 

button2_canvas = canvas1.create_window( 150, 70, 
									anchor = "nw",
                                    height=30,
                                    width=100,
									window = password) 

button3_canvas = canvas1.create_window( 150, 130, anchor = "nw",
                                        height=50,
                                        width=50,  
									window = button3) 

# Execute tkinter 
root.mainloop() 

print(username)
print(password)