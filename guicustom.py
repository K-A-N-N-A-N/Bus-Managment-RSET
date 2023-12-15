# Python program to create a basic form 
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk


#connecting to the mysql database
'''import mysql.connector
conn = mysql.connector.connect(host='192.168.249.148',username='user44',password='456ASDcvb###',database='bustrial')
busdb=conn.cursor()'''
# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to 
# the appearance mode of the system
ctk.set_appearance_mode("Dark") 

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue 
ctk.set_default_color_theme(color_string="dark-blue") 

# Dimensions of the window
appWidth, appHeight = 300, 200


# App Class
class App(ctk.CTk):
	# The layout of the window will be written
	# in the init function itself
	def __init__(self):
		super().__init__()

		# Sets the title of the window to "App"
		self.title("RSET BUS MANAGEMENT SYSTEM") 
		# Sets the dimensions of the window to 600x700
		self.geometry(f"{appWidth}x{appHeight}") 

		# Name Label
		self.userLabel = ctk.CTkLabel(self,
								text="UID")
		self.userLabel.grid(row=0, column=0,
							sticky="ew")

		# Name Entry Field
		self.userEntry = ctk.CTkEntry(self,
						placeholder_text="e.g Jefrin John")
		self.userEntry.grid(row=0, column=1,
							columnspan=3, sticky="ew")

		# Age Label
		self.passwLabel = ctk.CTkLabel(self, text="PASSWORD")
		self.passwLabel.grid(row=1, column=0,
						sticky="ew")

		# Age Entry Field
		self.passwEntry = ctk.CTkEntry(self,
							placeholder_text="e.g bhfur34")
		self.passwEntry.grid(row=1, column=1,
						columnspan=3, padx=20,
						pady=20, sticky="ew")
        
		# Generate Button
		self.generateResultsButton = ctk.CTkButton(self,
										text="Login",
										command=self.printf)
		self.generateResultsButton.grid(row=5, column=1,
										columnspan=2, padx=20, 
										pady=20, sticky="ew")

	def printf(self):
		flag=0
		#busdb.execute("select * from student")
		busdb=(("u2101","pass"))
		user = self.userEntry.get()
		passw = self.passwEntry.get()
		for row in busdb:
			if row[0]==user and row[1]==passw:
					self.destroy()
					print("hello")
			else:
				self.userEntry.delete(0, ctk.END)
				self.passwEntry.delete(0, ctk.END)
				self.wrloginLabel = ctk.CTkLabel(self, text="wrong login credentials",text_color="blue")
				self.wrloginLabel.grid(row=7, column=1,columnspan=2, padx=20, sticky="ew")
		
		
	

if __name__ == "__main__":
	app = App()
	# Used to run the application
	app.mainloop()	 
