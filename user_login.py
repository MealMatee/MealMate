from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk

root=CTk()
root.geometry("1500x750")
root.title("Login")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")

main_ulogin_frame2=CTkFrame(root)
main_ulogin_frame2.place(relwidth=1,relheight=1,x=0,y=0)

def reset_successful():
    win2.destroy()
    tk.messagebox.showinfo("Reset Successful","Password reset successful.")

def no_account():
    root.destroy()
    import user_signup

def back():
    root.destroy()
    import dashboard




def stretch(event):
    '''
    this function is made so that the pictures fits on the screen 
    even when the screen size changes . 
    '''
    global resized_tk

    #for the changing width and height of the window
    width=event.width
    height=event.height

    resized_image=ulogin_bg.resize((width,height))
    resized_tk=ImageTk.PhotoImage(resized_image)
   
    canvas.create_image(0,0,anchor=tk.NW,image=resized_tk)
    


def onclick():
    '''
    it is made so that we can hide or show password clicking the eye button
    '''
    if ulogin_e2.cget("show") == "":
        ulogin_e2.configure(show="*")
    else:
        ulogin_e2.configure(show="")
    
def reset_p1():
    if ulogin_etr1.cget("show") == "":
        ulogin_etr1.configure(show="*")
    else:
        ulogin_etr1.configure(show="")

def reset_p2():
    if ulogin_etr2.cget("show") == "":
        ulogin_etr2.configure(show="*")
    else:
        ulogin_etr2.configure(show="")
        




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
    #the pic in the top label window
    ulogin_sec_image1=Image.open("pictures\\forgot-pass-pic.jpg")
    ulogin_sec_image1_resize=ulogin_sec_image1.resize((626,626))
    ulogin_sec_image1_tk=ImageTk.PhotoImage(ulogin_sec_image1_resize)
    ulogin_label1=tk.Label(win2,image=ulogin_sec_image1_tk)
    ulogin_label1.image = ulogin_sec_image1_tk  #reference to the picture
    ulogin_label1.place(relheight=1,relwidth=1,relx=0.2499)

#the main frame of win1 
    ulogin_frame1=tk.Frame(win2,bg="#001129",width=626,height=626)
    ulogin_frame1.place(x=0,y=0)

#frame which contains the questions 
    ulogin_frame2=tk.Frame(ulogin_frame1,bg="#001129",width=426,height=450,bd=3,relief="groove")
    ulogin_frame2.place(relx=0.16,rely=0.13)

#label for security questions heading
    ulogin_label2=tk.Label(ulogin_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
    ulogin_label2.place(relx=0.3,rely=0.1)

#label for 1st question
    ulogin_label3=tk.Label(ulogin_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
    ulogin_label3.place(relx=0.05,rely=0.1)

#entry for 1st question
    ulogin_entry1=CTkEntry(ulogin_frame2,fg_color="#74A9D8",width=220)
    ulogin_entry1.place(relx=0.17,rely=0.17)

#label for 2nd question
    ulogin_label4=tk.Label(ulogin_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
    ulogin_label4.place(relx=0.05,rely=0.32)

#entry for 2nd question
    ulogin_entry2=CTkEntry(ulogin_frame2,fg_color="#74A9D8",width=220)
    ulogin_entry2.place(relx=0.17,rely=0.39)

#label for 3rd question
    ulogin_label5=tk.Label(ulogin_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
    ulogin_label5.place(relx=0.05,rely=0.54)

#entry for 3rd question
    ulogin_entry3=CTkEntry(ulogin_frame2,fg_color="#74A9D8",width=220)
    ulogin_entry3.place(relx=0.17,rely=0.61)

#the submit button
    ulogin_button1=CTkButton(ulogin_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=reset_pass)
    ulogin_button1.place(relx=0.3,rely=0.8)
    pass



ulogin_eye_img=Image.open("pictures//Vectorblack_eye1.png")
ulogin_eye_imgtk=ImageTk.PhotoImage(ulogin_eye_img)


def reset_pass():
    global ulogin_etr1
    global ulogin_etr2

    win3=tk.Toplevel()
    win3.title("Reset password")
    win3.geometry("500x250")
    win3.resizable(0,0)

    ulogin_lbl1=tk.Label(win3,text="Enter New Password:",font=("Regular",13))
    ulogin_lbl1.place(relx=0.05,rely=0.08)
    ulogin_etr1=CTkEntry(win3,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",show="*",text_color="Black")
    ulogin_etr1.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

    ulogin_lbl2=tk.Label(win3,text="Confirm new Password:",font=("Regular",13))
    ulogin_lbl2.place(relx=0.05,rely=0.33)
    ulogin_etr2=CTkEntry(win3,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",show="*",text_color="Black")
    ulogin_etr2.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

    ulogin_btn1=CTkButton(win3,text="SUBMIT",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",border_width=2,command=reset_successful)
    ulogin_btn1.place(relx=0.33,rely=0.75,relwidth=0.3,relheight=0.15)

    ulogin_btn2=tk.Button(win3,image=ulogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p1)
    ulogin_btn2.place(relx=0.78,rely=0.2)

    ulogin_btn3=tk.Button(win3,image=ulogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p2)
    ulogin_btn3.place(relx=0.78,rely=0.46)


    



#eye button pic
ulogin_eye=Image.open("pictures\\ion_eyeeye.png")
ulogin_eyetk=ImageTk.PhotoImage(ulogin_eye)





#bg image
ulogin_bg = Image.open("pictures\\coffee.jpg")
ulogin_bgtk=ImageTk.PhotoImage(ulogin_bg)


ulogin_back=Image.open("pictures//Vectorarrow.png")
ulogin_backtk=ImageTk.PhotoImage(ulogin_back)


#canvas widget which covers the entire screen
canvas=tk.Canvas(main_ulogin_frame2,bg="black",bd=0,highlightthicknes=0)
canvas.place(relwidth=1,relheight=1)
canvas.bind("<Configure>",stretch)

#The main frame
ulogin_f1=CTkFrame(main_ulogin_frame2,fg_color="#888888",bg_color="White",corner_radius=8)
ulogin_f1.place(relx=0.08,rely=0.15,relheight=0.7,relwidth=0.3)

#logo
ulogin_img1=Image.open("pictures\\logo-no-1.png")#insert image
ulogin_img1=ulogin_img1.resize((516,106))#resize
photo_ulogin_img1=ImageTk.PhotoImage(ulogin_img1)#pil to photo image
label = tk.Label(ulogin_f1, image=photo_ulogin_img1,bg="#888888")#label
label.place(x=20, y=15, w=516, h=106)
label=ulogin_img1


#for spacing between logo and login frame
ulogin_f2=tk.Frame(ulogin_f1,bg="#F8F9F7")
ulogin_f2.place(relwidth=1,relheight=0.018,relx=0,rely=0.2)

#login heading
ulogin_l1=tk.Label(ulogin_f1,text="User Login",bg="#888888",font=("Inter",25,"bold"))
ulogin_l1.place(relx=0.26,rely=0.25,relwidth=0.5,relheight=0.07)

ulogin_l2=tk.Label(ulogin_f1,text="Email:",bg="#888888",font=("Regular",20))
ulogin_l2.place(relx=0.08,rely=0.34)

#email entrybox
ulogin_e1=CTkEntry(ulogin_f1,fg_color="#FAF3DB",placeholder_text="example@gmail.com",placeholder_text_color="#DD2323",border_color="#888888",text_color="#DD2323",font=("Regular",15))
ulogin_e1.place(relx=0.08,rely=0.40,relwidth=0.8,relheight=0.09)

#password label
ulogin_l3=tk.Label(ulogin_f1,text="Password:",bg="#888888",font=("Regular",20))
ulogin_l3.place(relx=0.08,rely=0.51)



#password entrybox
ulogin_e2=CTkEntry(ulogin_f1,fg_color="#FAF3DB",border_color="#888888",text_color="#DD2323",font=("Regular",15),show="*")
ulogin_e2.place(relx=0.08,rely=0.57,relwidth=0.8,relheight=0.09)


#forgot pass label
ulogin_l4=tk.Label(ulogin_f1,text="Forgot your password?",fg="White",bg="#888888",font=("Inter",15,"italic"))
ulogin_l4.place(relx=0.35,rely=0.67)

#click here
ulogin_b1=tk.Button(ulogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=new)
ulogin_b1.place(relx=0.713,rely=0.666)


#login button
ulogin_b2=CTkButton(ulogin_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
ulogin_b2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


#dont have account label
ulogin_b5=tk.Label(ulogin_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
ulogin_b5.place(relx=0.2,rely=0.9)

#button for dont have an account
ulogin_b3=tk.Button(ulogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"))
ulogin_b3.place(relx=0.56,rely=0.896)


# eye button
ulogin_b4=tk.Button(ulogin_f1,image=ulogin_eyetk,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
ulogin_b4.place(relx=0.8,rely=0.595)

ulogin_b5=tk.Button(ulogin_f1,image=ulogin_backtk,text=" Back",compound=LEFT,bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
ulogin_b5.place(relx=0.048,rely=0.903)


root.mainloop()









