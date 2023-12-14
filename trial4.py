import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0, sticky="nsew")

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.grid(row=1, column=0, sticky="nsew")

label3 = tk.Label(root, text="Label 3", bg="green")
label3.grid(row=0, column=1, rowspan=2, sticky="nsew")

# Configure row and column weights to make the cells expandable
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
