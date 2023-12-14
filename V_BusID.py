from tkinter import *

class GUI:
    def __init__(self):
        self.V_root = Tk()
        self.V_root.geometry("500x400")

        # List of background images
        background_images = [
            PhotoImage(file="background_1.png")
        ]

        # Create a 2x2 grid of canvases
        for i, img in enumerate(background_images):
            canvas = Canvas(self.V_root, width=300, height=300)
            canvas.grid(row=i // 2, column=i % 2, sticky="nsew")

            # Resize background image to match the canvas size
            img = img.subsample(3, 3)  # Adjust subsample factor if necessary

            # Display background image on the canvas
            canvas.create_image(0, 0, anchor="nw", image=img)

            # Add Text
            canvas.create_text(200, 200, text="Welcome", fill="maroon", font=("courier new", "20"), anchor="center")
            canvas.create_text(50, 250, text="UID :", fill="maroon", font=("courier new", "15"), anchor="nw")
            canvas.create_text(50, 270, text="    Bus ID : ", fill="maroon", font=("courier new", "15"), anchor="nw")

        # Configure grid weights to make the canvases expand proportionally
        for i in range(2):
            self.V_root.grid_columnconfigure(i, weight=1)
            self.V_root.grid_rowconfigure(i, weight=1)

        self.V_root.mainloop()

if __name__ == "__main__":
    gui = GUI()

'''
# Import module 
from tkinter import *

def gui():
    V_root = Tk() 
    V_root.geometry("400x400") 

    #bg = PhotoImage(file = "rset1.png")

    V_canvas = Canvas(V_root, width = 900, height = 900 ) 
    V_canvas.pack(fill = "both", expand = True) 

    # Display image 
    V_canvas.create_image( 0, 0,anchor = "nw") 

    # Add Text 
    V_canvas.create_text( 50, 10, text = "Welcome",fill="maroon",font=("courier new", "12"),anchor="n")
    V_canvas.create_text( 50, 70, text=" USERID:   ",fill="maroon",font=("courier new", "12"),anchor="n") 
    V_canvas.create_text( 50, 130, text="PASSWORD: ",fill="maroon",font=("courier new", "12"),anchor="n") 

    V_root.mainloop()

gui()
'''