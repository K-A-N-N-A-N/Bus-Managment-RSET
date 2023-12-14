# GUI application using the customtkinter module
from customtkinter import *
import tkinter as tk

def printf():
    user = userEntry.get()
    passw = passwEntry.get()
    print("the uid is",user)
    print("the password is ",passw)





appWidth, appHeight = 300, 200

app=CTk()

app.title("RSET BUS MANAGEMENT SYSTEM") 
# Sets the dimensions of the window to 600x700
app.geometry(f"{appWidth}x{appHeight}") 

# Name Label
userLabel = CTkLabel(app,text="UID")
userLabel.grid(row=0, column=0,
                    sticky="ew")

# Name Entry Field
userEntry = CTkEntry(app,
                placeholder_text="e.g Jefrin John")
userEntry.grid(row=0, column=1,
                    columnspan=3, sticky="ew")

# Age Label
passwLabel = CTkLabel(app,text="UID")                      
passwLabel.grid(row=1, column=0,
                sticky="ew")

# Age Entry Field
passwEntry = CTkEntry(app,placeholder_text="e.g bhfur34")
passwEntry.grid(row=1, column=1,
                columnspan=3, padx=20,
                pady=20, sticky="ew")

# Generate Button
generateResultsButton = CTkButton(app,text="Generate Results",command=printf)
generateResultsButton.grid(row=5, column=1,
                                columnspan=2, padx=20, 
                                pady=20, sticky="ew")
