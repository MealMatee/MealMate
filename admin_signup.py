from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk


root=CTk()
root.geometry("1500x750")
root.title("Admin_signup")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")

main_frame5=CTkFrame(root)
main_frame5.place(relwidth=1,relheight=1,x=0,y=0)


def back():
    root.destroy()
    import dashboard




def already_acc():
    root.destroy()
    import user_login




def password():
    '''
    it is made so that we can hide or show password clicking the eye button in password
    '''
    if asignup_e4.cget("show") == "":
        asignup_e4.configure(show="*")
    else:
        asignup_e4.configure(show="")

def repassword():
    '''
    it is made so that we can hide or show password clicking the eye button in  repassword
    '''
    if asignup_e5.cget("show") == "":
        asignup_e5.configure(show="*")
    else:
        asignup_e5.configure(show="")


def security_info():
    '''
    this function is made to show a message when user clicks submit on win1 window
    '''

    win2.destroy()         
    tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")

    pass




def newwin():
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
    sec_button1=CTkButton(sec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_info)
    sec_button1.place(relx=0.3,rely=0.8)
    pass

def message():
    tk.messagebox.showinfo("Security question message","Security question must be answered. In case if you forgot your password, then this will help you reset your password .")




#the bg frame
asignup_frame=tk.Frame(main_frame5,bg="Black")
asignup_frame.place(relwidth=1,relheight=1)

#the main bg picture 
asignup_image1=Image.open("pictures\\f327a69f-4c36-4c1e-8965-c5a71e3d9d99.png")
asignup_image1=asignup_image1.resize((968,1080))
photosignup_image1=ImageTk.PhotoImage(asignup_image1)
asignup_label = tk.Label(main_frame5, image=photosignup_image1)
asignup_label.place(x=952, y=0, w=968, h=1080)


#image for eye button in password and repassword
asignup_eye=Image.open("pictures\\ion_eyeeye.png")
tksignup_eye=ImageTk.PhotoImage(asignup_eye)


#image for i button 
asignup_i=Image.open("pictures\\Vector.png")
tkasignup_i=ImageTk.PhotoImage(asignup_i)


#label for mealmate logo
asignup_logo=Image.open("pictures\\logo-no-2.png")
asignup_logo=asignup_logo.resize((641,141))
photo_asignup_logo=ImageTk.PhotoImage(asignup_logo)
asignup_logo_lbl = tk.Label(main_frame5, image=photo_asignup_logo,bg="#262731")
asignup_logo_lbl.place(x=138, y=62, w=641, h=141)

asignup_back=Image.open("pictures//Vectorarrow.png")
asignup_backtk=ImageTk.PhotoImage(asignup_back)




#the main frame
asignup_f1=CTkFrame(asignup_frame,corner_radius=10,fg_color="#262731",width=681,height=900)
asignup_f1.place(x=100,y=39,w=681,h=900)

#sep frame
sep_frame=tk.Frame(asignup_f1,bg="Black")
sep_frame.place(relwidth=1,relheight=0.02,rely=0.2)

#signup heading label
asignup_lbl1=tk.Label(asignup_f1,text="User SignUp",font=("Inter",25,"bold"),bg="#262731",fg="white")
asignup_lbl1.place(relx=0.32,rely=0.23)

#firstname label
asignup_lbl2=tk.Label(asignup_f1,text="First Name:",font=("Regular",15),bg="#262731",fg="White")
asignup_lbl2.place(relx=0.05,rely=0.3)

#firstname entry
asignup_e1=CTkEntry(asignup_f1,placeholder_text="firstname",fg_color="#FAF3DB",width=180,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
asignup_e1.place(relx=0.05,rely=0.33)

#lastname label
asignup_lbl3=tk.Label(asignup_f1,text="Last Name:",font=("Regular",15),bg="#262731",fg="White")
asignup_lbl3.place(relx=0.53,rely=0.29)

#lastname entry
asignup_e2=CTkEntry(asignup_f1,placeholder_text="lastname",fg_color="#FAF3DB",width=190,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
asignup_e2.place(relx=0.53,rely=0.33)

#email label
asignup_lbl4=tk.Label(asignup_f1,text="Email:",font=("Regular",15),bg="#262731",fg="White")
asignup_lbl4.place(relx=0.05,rely=0.43)

#email entry
asignup_e3=CTkEntry(asignup_f1,placeholder_text="Your Email Here",fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
asignup_e3.place(relx=0.05,rely=0.46)

#password label
asignup_lbl5=tk.Label(asignup_f1,text="Password:",font=("Regular",15),bg="#262731",fg="White")
asignup_lbl5.place(relx=0.05,rely=0.56)

#password entry
asignup_e4=CTkEntry(asignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
asignup_e4.place(relx=0.05,rely=0.59)

#repassword label
asignup_lbl6=tk.Label(asignup_f1,text="Re-Password:",font=("Regular",15),bg="#262731",fg="White")
asignup_lbl6.place(relx=0.05,rely=0.69)

#repassword entry
asignup_e5=CTkEntry(asignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
asignup_e5.place(relx=0.05,rely=0.72)

#security question label
asignup_b1=CTkButton(asignup_f1,text="Security Questions",text_color="#CF7941",width=300,height=40,fg_color="#FAF3DB",hover=0,font=("Inter",15,"bold"),corner_radius=8,command=newwin)
asignup_b1.place(relx=0.2,rely=0.81)

#Signup button
asignup_b2=CTkButton(asignup_f1,text="SIGN UP",fg_color="#FAF3DB",hover=0,height=45,font=("Inter",20,"bold"),text_color="#4D5053",corner_radius=8)
asignup_b2.place(relx=0.35,rely=0.92)

#eye button in password
asignup_b3=tk.Button(asignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = password)
asignup_b3.place(relx=0.8,rely=0.61)

#eye button in repassword
asignup_b4=tk.Button(asignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = repassword)
asignup_b4.place(relx=0.8,rely=0.74)

#i button in security question
asignup_btn1=tk.Button(asignup_f1,image=tkasignup_i,bg="#FAF3DB",activebackground="#FAF3DB",bd=0,command=message)
asignup_btn1.place(relx=0.68,rely=0.825)

#already an account label
asignup_lbl7=tk.Label(asignup_f1,text="Already have an account?",font=("Inter",12,"italic"),bg="#262731",fg="White")
asignup_lbl7.place(relx=0.48,rely=0.87)

# click here button 
asignup_b5=tk.Button(asignup_f1,text="click here",font=("Inter",12,"bold italic"),bg="#262731",fg="#DD2323",activebackground="#262731",bd=0,command=already_acc)
asignup_b5.place(relx=0.76,rely=0.869)

asignup_btn1=tk.Button(asignup_f1,image=asignup_backtk,text=" Back",compound=LEFT,bg="#262731",activebackground="#262731",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
asignup_btn1.place(relx=0.048,rely=0.94)


root.mainloop()
