from tkinter import * 

root2=Tk()
root2.geometry("600x600")
bg1 = PhotoImage(file = "white.png")
canvas2 = Canvas( root2, width = 900, 
                height = 900 ) 
canvas2.pack(fill = "both", expand = True) 
canvas2.create_image( 0, 0, image = bg1, 
                    anchor = "nw")
canvas2.create_text( 50, 10, text = "Welcome",fill="maroon",font=("Franklin Gothic Medium", "12"),anchor="n")
profile=root2.Label( text=" PROFILE  ", width=50, height=10 ,master=root2  )
''',fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n"'''
profile.pack()
button1_canvas2 = canvas2.create_window(  100,70,
                                anchor = "nw",
                                height=30,
                                width=100, 
                                window = profile) 

'''label=root2.Label( 50, 70, text=" PROFILE  ",fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n") 
label2=canvas2.create_text( 50, 130, text="APPLICATION",fill="maroon",font=("Franklin Gothic Medium", "10"),anchor="n")
label.pack()
label2.pack()
label.bind("<Buttton-1>",gui3)'''
