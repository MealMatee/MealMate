from customtkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3

root = CTk()

#making the root fit in the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
tree_frame = tk.Frame(root)

font1 = ('Inter', 15, 'bold')
tree_frame.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)
# #creating entryboxes and label
# tree_l1 = tk.Label(tree_frame, text = 'first_name', font = font1 )
# tree_l1.place(relx=0.05,rely=0.01,relwidth=0.05)













root.mainloop()