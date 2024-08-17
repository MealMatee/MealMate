import tkinter as tk
from PIL import Image,ImageTk
from customtkinter import *

root=tk.Tk()
root.geometry("600x700")
root.resizable(0,0)

#bill main frame
bill_mainframe=tk.Frame(root,bg="white")
bill_mainframe.place(relheight=1,relwidth=1,relx=0,rely=0)

# for logo 
bill_frame_logo=Image.open("pictures/Rectangle 41.png")
bill_frame_logo=bill_frame_logo.resize((430,90))
photo_bill_frame_logo=ImageTk.PhotoImage(bill_frame_logo)
#label that contains image
bill_frame_lbl = tk.Label(bill_mainframe, image=photo_bill_frame_logo,bg="white")
bill_frame_lbl.place(x=70, y=16, w=430, h=90)

#bill no. label
bill_lbl1=tk.Label(bill_mainframe,text="Bill no. :-",font=("Inter",13),bg="white")
bill_lbl1.place(relx=0.08,rely=0.2)
#date no. label
bill_lbl2=tk.Label(bill_mainframe,text="Date :-",font=("Inter",13),bg="white")
bill_lbl2.place(relx=0.65,rely=0.2)
#table that contains S.N,Product etc.
bill_frame1=CTkFrame(bill_mainframe,fg_color="#D9D9D9",border_color="black",corner_radius=0,border_width=1)
bill_frame1.place(relwidth=0.9,relheight=0.7,relx=0.05,rely=0.25)

#S.N label
bill_label1=tk.Label(bill_frame1,text="S.N",font=("Inter",13),bg="#D9D9D9")
bill_label1.place(relx=0.001,rely=0.01)

#Product label
bill_label2=tk.Label(bill_frame1,text="Product",font=("Inter",13),bg="#D9D9D9")
bill_label2.place(relx=0.22,rely=0.01)

#Quantity label
bill_label3=tk.Label(bill_frame1,text="Quantity",font=("Inter",13),bg="#D9D9D9")
bill_label3.place(relx=0.52,rely=0.01)

#Price label
bill_label4=tk.Label(bill_frame1,text="Price",font=("Inter",13),bg="#D9D9D9")
bill_label4.place(relx=0.8,rely=0.01)

#sep frame
bill_sep_frame1=tk.Frame(bill_frame1,bg="black")
bill_sep_frame1.place(relx=0.07,relheight=1,rely=0,relwidth=0.001)
#sep frame
bill_sep_frame2=tk.Frame(bill_frame1,bg="black")
bill_sep_frame2.place(relx=0.48,relheight=1,rely=0,relwidth=0.001)
#sep frame
bill_sep_frame3=tk.Frame(bill_frame1,bg="black")
bill_sep_frame3.place(relx=0.67,relheight=1,rely=0,relwidth=0.001)
#sep frame
bill_sep_frame4=tk.Frame(bill_frame1,bg="black")
bill_sep_frame4.place(relx=0.07,relheight=1,rely=0,relwidth=0.001)

#sep frame
bill_sep_frame5=tk.Frame(bill_frame1,bg="black")
bill_sep_frame5.place(relx=0,relheight=0.001,rely=0.07,relwidth=1)

#sep frame
bill_sep_frame6=tk.Frame(bill_frame1,bg="black")
bill_sep_frame6.place(relx=0.67,relheight=0.001,rely=0.7,relwidth=0.33)

#sep frame
bill_sep_frame7=tk.Frame(bill_frame1,bg="black")
bill_sep_frame7.place(relx=0.67,relheight=0.001,rely=0.85,relwidth=0.33)

#sep frame
bill_sep_frame8=tk.Frame(bill_frame1,bg="black")
bill_sep_frame8.place(relx=0.83,relheight=0.33,rely=0.7,relwidth=0.001)

#Total amount label
bill_label4=tk.Label(bill_frame1,text="Total\nAmount",font=("Inter",13),bg="#D9D9D9")
bill_label4.place(relx=0.7,rely=0.73)

#Payment option label
bill_label4=tk.Label(bill_frame1,text="Payment\nOption",font=("Inter",13),bg="#D9D9D9")
bill_label4.place(relx=0.69,rely=0.87)


root.mainloop()