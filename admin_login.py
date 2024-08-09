from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk

root=CTk()
root.geometry("1500x750")
root.title("Admin_Login")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")


main_frame4 = CTkFrame(root)
main_frame4.place(relwidth = 1, relheight = 1,x = 0, y = 0)

def back():
    root.destroy()
    import dashboard


def no_account():
    root.destroy()
    import user_signup


def stretch(event):
    '''
    this function is made so that the pictures fits on the screen 
    even when the screen size changes . 
    '''
    global resized_tk

    #for the changing width and height of the window
    width=event.width
    height=event.height

    resized_image=alogin_bg.resize((width,height))
    resized_tk=ImageTk.PhotoImage(resized_image)
   
    canvas.create_image(0,0,anchor=tk.NW,image=resized_tk)
    


def onclick():
    '''
    it is made so that we can hide or show password clicking the eye button
    '''
    if alogin_e2.cget("show") == "":
        alogin_e2.configure(show="*")
    else:
        alogin_e2.configure(show="")

def security_update():
    '''
    this function is made to show a message when user clicks submit on win1 window
    '''
    win2.destroy()         
    tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")
    pass

def login():
    """
    this function is made so that a messagebox is shown after clicking 
    the login button and the root window is destroyed . 
    """
    tk.messagebox.showinfo("Successful Message ","Login Successful !")
    root.destroy()   
    pass      
    



def new():
    """this function contains a toplevel window which opens when click here button is clicked 
    which is by the side of forgot password .
    """
    global win2

    #the forgot password window
    win2=tk.Toplevel()
    win2.geometry("1252x626")
    win2.resizable(0,0)
    win2.title("Forgot password")
    win2.iconbitmap("pictures//32432hotbeverage_98916.ico")
    #the pic in the top label window
    sec_image=Image.open("pictures\\forgot-pass-pic.jpg")
    sec_image_resize=sec_image.resize((626,626))
    sec_image_tk=ImageTk.PhotoImage(sec_image_resize)
    sec_label1=tk.Label(win2,image=sec_image_tk)
    sec_label1.image = sec_image_tk  #reference to the picture
    sec_label1.place(relheight=1,relwidth=1,relx=0.2499)



#the main frame of win1 
    sec_frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
    sec_frame1.place(x=0,y=0)

#frame which contains the questions 
    sec_frame2=tk.Frame(sec_frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
    sec_frame2.place(relx=0.16,rely=0.13)

#label for security questions heading
    sec_lbl2=tk.Label(sec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
    sec_lbl2.place(relx=0.3,rely=0.1)

#label for 1st question
    sec_lbl3=tk.Label(sec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
    sec_lbl3.place(relx=0.05,rely=0.1)

#entry for 1st question
    sec_entry1=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
    sec_entry1.place(relx=0.17,rely=0.17)

#label for 2nd question
    sec_lbl4=tk.Label(sec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
    sec_lbl4.place(relx=0.05,rely=0.32)

#entry for 2nd question
    sec_entry2=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
    sec_entry2.place(relx=0.17,rely=0.39)

#label for 3rd question
    sec_lbl5=tk.Label(sec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
    sec_lbl5.place(relx=0.05,rely=0.54)

#entry for 3rd question
    sec_entry3=CTkEntry(sec_frame2,fg_color="#74A9D8",width=220)
    sec_entry3.place(relx=0.17,rely=0.61)

#the submit button
    sec_button1=CTkButton(sec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_update)
    sec_button1.place(relx=0.3,rely=0.8)
    pass


    



#eye button pic
alogin_eye=Image.open("pictures\\ion_eyeeye.png")
alogin_eyetk=ImageTk.PhotoImage(alogin_eye)


#bg image
alogin_bg = Image.open("pictures\\coffee.jpg")
alogin_bgtk=ImageTk.PhotoImage(alogin_bg)

alogin_back=Image.open("pictures//Vectorarrow.png")
alogin_backtk=ImageTk.PhotoImage(alogin_back)


#canvas widget which covers the entire screen
canvas=tk.Canvas(main_frame4,bg="black",bd=0,highlightthicknes=0)
canvas.place(relwidth=1,relheight=1)
canvas.bind("<Configure>",stretch)

#The main frame
alogin_f1=CTkFrame(main_frame4,fg_color="#888888",bg_color="White",corner_radius=8)
alogin_f1.place(relx=0.08,rely=0.15,relheight=0.7,relwidth=0.3)


#logo
alogin_logo=Image.open("pictures\\logo-no-1.png")#insert image
alogin_logo=alogin_logo.resize((516,106))#resize
photo_alogin_logo=ImageTk.PhotoImage(alogin_logo)#pil to photo image
alogin_lbl = tk.Label(alogin_f1, image=photo_alogin_logo,bg="#888888")#label
alogin_lbl.place(x=20, y=15, w=516, h=106)



#for spacing between logo and login frame
alogin_sep=tk.Frame(alogin_f1,bg="#F8F9F7")
alogin_sep.place(relwidth=1,relheight=0.018,relx=0,rely=0.2)

#login heading
alogin_lbl1=tk.Label(alogin_f1,text="Admin Login",bg="#888888",font=("Inter",25,"bold"))
alogin_lbl1.place(relx=0.26,rely=0.25,relwidth=0.5,relheight=0.1)

alogin_lbl2=tk.Label(alogin_f1,text="Email:",bg="#888888",font=("Regular",20))
alogin_lbl2.place(relx=0.08,rely=0.34)

#email entrybox
alogin_e1=CTkEntry(alogin_f1,fg_color="#FAF3DB",placeholder_text="example@gmail.com",placeholder_text_color="#DD2323",border_color="#888888",text_color="#DD2323",font=("Regular",15))
alogin_e1.place(relx=0.08,rely=0.40,relwidth=0.8,relheight=0.09)

#password label
alogin_lbl3=tk.Label(alogin_f1,text="Password:",bg="#888888",font=("Regular",20))
alogin_lbl3.place(relx=0.08,rely=0.51)



#password entrybox
alogin_e2=CTkEntry(alogin_f1,fg_color="#FAF3DB",border_color="#888888",text_color="#DD2323",font=("Regular",15),show="*")
alogin_e2.place(relx=0.08,rely=0.57,relwidth=0.8,relheight=0.09)


#forgot pass label
alogin_lbl4=tk.Label(alogin_f1,text="Forgot your password?",fg="White",bg="#888888",font=("Inter",15,"italic"))
alogin_lbl4.place(relx=0.35,rely=0.67)

#click here
alogin_btn1=tk.Button(alogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=new)
alogin_btn1.place(relx=0.713,rely=0.666)


#login button
alogin_btn2=CTkButton(alogin_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
alogin_btn2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


#dont have account label
alogin_lbl5=tk.Label(alogin_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
alogin_lbl5.place(relx=0.28,rely=0.9)

#button for dont have an account
alogin_btn3=tk.Button(alogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"))
alogin_btn3.place(relx=0.64,rely=0.896)


# eye button
alogin_btn4=tk.Button(alogin_f1,image=alogin_eyetk,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
alogin_btn4.place(relx=0.8,rely=0.595)

alogin_btn5=tk.Button(alogin_f1,image=alogin_backtk,text=" Back",compound=LEFT,bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
alogin_btn5.place(relx=0.048,rely=0.903)


root.mainloop()
