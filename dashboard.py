from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk
import sqlite3
from tkinter import ttk

root=CTk()

#making the root fit in the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

#title
root.title("Mealmate")
#icon
root.iconbitmap("pictures/32432hotbeverage_98916.ico")







#-------------------------------------------i_buttons for main dashboard--------------------------------------------------#






def i_button1():
    '''function to show message when i button is clicked''' 
    tk.messagebox.showinfo("User Login","Click here for Signing in to User Account .")

def i_button2():
    '''function to show message when i button is clicked''' 
    tk.messagebox.showinfo("Admin Login","Click here for Signing in to Admin Account .")

def i_button3():
    '''function to show message when i button is clicked''' 
    tk.messagebox.showinfo("User Signup","Click here for Creating a new User Account .")

def i_button4():
    '''function to show message when i button is clicked''' 
    tk.messagebox.showinfo("Admin Signup","Click here for Creating a new Admin Account .")
   





#----------------------------------------------------button about MealMate--------------------------------------------------------#
def mealmate():
    pass






#----------------------------------------------User Login--------------------------------------------------------------------------#
def user_login():
    '''this functions contain a frame which consists of the login page'''
    #the main frame
    main_ulogin_frame2=CTkFrame(root)
    main_ulogin_frame2.place(relwidth=1,relheight=1,x=0,y=0)



    def reset_successful():
        '''function to check if the conditions are meet and then resets the password''' 
        #----------------------------------------------database------------------------------------------#
        if ulogin_etr0.get() == '' or ulogin_etr1.get() == '' or ulogin_etr2.get() == '' : 
            tk.messagebox.showerror("Error","All fields must be filled out.")
        elif ulogin_e1.get() != ulogin_etr0.get():
            tk.messagebox.showerror("Error","Incorrect email.")
        elif ulogin_etr2.get()!= ulogin_etr1.get():
            tk.messagebox.showerror("Error","Incorrect password.")
        elif len(ulogin_etr1.get()) < 8 :
            tk.messagebox.showerror("Error","Password must be at least 8 characters long.")
        else:
            #update password to user database table
            conn=sqlite3.connect('mealmate.db')
            c=conn.cursor()
            c.execute("UPDATE user SET password=? WHERE email=?",(ulogin_etr2.get(),ulogin_etr0.get()))
            conn.commit()
            conn.close()
            usign_sec_qsn_frame.place_forget()
            user_login()
            tk.messagebox.showinfo("Reset Successful","Password reset successful.")
        #------------------------------------------------------------------------------------------------#




    def back():
        '''function to open dashboard when back button is clicked '''
        main_ulogin_frame2.destroy()
        main()



    def click_here():
        '''function to open user signup page when click here button is clicked '''
        main_ulogin_frame2.place_forget()
        user_signup()



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
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if ulogin_etr1.cget("show") == "":
            ulogin_etr1.configure(show="*")
        else:
            ulogin_etr1.configure(show="")

    def reset_p2():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if ulogin_etr2.cget("show") == "":
            ulogin_etr2.configure(show="*")
        else:
            ulogin_etr2.configure(show="")
            




    def login():
        """
        this function is made so that a messagebox is shown after clicking 
        the login button and the root window is destroyed . 
        """

        #checking if the entry box are filled
        if ulogin_e1.get() == "" or ulogin_e2.get() == "":
            tk.messagebox.showerror("Error","All fields are required.")
        
        else:
            try:
                conn = sqlite3.connect("mealmate.db")
                c = conn.cursor()


                # Fetch the record with the matching email and password
                c.execute("SELECT * FROM user WHERE email = ? and password = ?", (ulogin_e1.get(), ulogin_e2.get()))
                result = c.fetchone()

                # Check if a result was found
                if result is not None:
                    # Assuming the email is in the 3rd column and the password in the 4th column
                    global u_email, u_password
                    if ulogin_e1.get() == result[2] and ulogin_e2.get() == result[3]:
                        u_email = ulogin_e1.get()
                        u_password = ulogin_e2.get()
                        tk.messagebox.showinfo("Successful Message", "Login Successful!")
                        main_ulogin_frame2.place_forget()
                        user_dashboard()
                    else:
                        tk.messagebox.showerror("Error", "Invalid email or password.")
                else:
                    tk.messagebox.showerror("Error", "Invalid email or password.")

            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                conn.close()
    

            
          
        #----------------------------------------------------------------------------------------------#



    def sec_qsn():
        """This function opens the security questions page when called."""
        main_ulogin_frame2.place_forget()
        main_frame1.place_forget()
        global usign_sec_qsn_frame
        
        usign_sec_qsn_frame=tk.Frame(root)
        usign_sec_qsn_frame.place(relheight=1,relwidth=1,x=0,y=0)
        #the pic in the top label window
        usec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        usec_image_resize=usec_image.resize((961,1080))
        usec_image_tk=ImageTk.PhotoImage(usec_image_resize)
        usec_label1=tk.Label(usign_sec_qsn_frame,image=usec_image_tk)
        usec_label1.image = usec_image_tk  #reference to the picture
        usec_label1.place(relheight=1,relwidth=1,relx=0.2499)

        global usec_entry3, usec_entry2, usec_entry1

    #the main frame of win1 
        usec_frame1=tk.Frame(usign_sec_qsn_frame,bg="#001129")
        usec_frame1.place(relheight=1,relwidth=0.5,x=0,y=0)

    #frame which contains the questions 
        usec_frame2=tk.Frame(usec_frame1,bg="#001129",width=626,height=800,bd=3,relief="groove")
        usec_frame2.place(relx=0.16,rely=0.1)

    #label for security questions heading
        usec_lbl2=tk.Label(usec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        usec_lbl2.place(relx=0.35,rely=0.08)

    #label for 1st question
        usec_lbl3=tk.Label(usec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        usec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        usec_entry1=CTkEntry(usec_frame2,fg_color="#74A9D8",width=380,height=40)
        usec_entry1.place(relx=0.13,rely=0.17)

    #label for 2nd question
        usec_lbl4=tk.Label(usec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        usec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        usec_entry2=CTkEntry(usec_frame2,fg_color="#74A9D8",width=380,height=40)
        usec_entry2.place(relx=0.13,rely=0.39)

    #label for 3rd question
        usec_lbl5=tk.Label(usec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        usec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        usec_entry3=CTkEntry(usec_frame2,fg_color="#74A9D8",width=380,height=40)
        usec_entry3.place(relx=0.13,rely=0.61)

    #the submit button
        usec_button1=CTkButton(usec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=reset_pass)
        usec_button1.place(relx=0.22,rely=0.8,relwidth=0.52,relheight=0.07)
        pass



    ulogin_eye_img=Image.open("pictures//Vectorblack_eye1.png")
    ulogin_eye_imgtk=ImageTk.PhotoImage(ulogin_eye_img)



    #--------------------------------reset password------------------------------------#


    def reset_pass():   
        """this function opens the reset password page when called."""

        #fetch user data from user table
        conn = sqlite3.connect("mealmate.db")
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE email = ?", (ulogin_e1.get(),))
        user_data = c.fetchone()





        #-----------------------------------------------database---------------------------------------------#
        if usec_entry1.get() == '' or usec_entry2.get() == '' or usec_entry3.get() == '':
            tk.messagebox.showerror("Error","All fields are required.")
        elif (usec_entry1.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Entered value must be a number.")
        if usec_entry1.get() == user_data[4] and usec_entry2.get() == user_data[5] and usec_entry3.get() == user_data[6]:
        
            global ulogin_etr1,ulogin_etr2,areset_pass_frame
            usign_sec_qsn_frame.place_forget()

            ureset_pass_main_frame=tk.Frame(root)
            ureset_pass_main_frame.place(relheight=1,relwidth=1,x=0,y=0)

            reset_pass_image=Image.open("pictures/reset passreset_pass2.png")
            reset_pass_image_resize=reset_pass_image.resize((1920,1080))
            reset_pass_image_tk=ImageTk.PhotoImage(reset_pass_image_resize)
            reset_pass_label1=tk.Label(ureset_pass_main_frame,image=reset_pass_image_tk)
            reset_pass_label1.image = reset_pass_image_tk  #reference to the picture
            reset_pass_label1.place(relheight=1,relwidth=1)
            
            ureset_pass_frame=tk.Frame(ureset_pass_main_frame,width=450,height=450,bd=3,relief="groove",bg="#0B1A41")
            ureset_pass_frame.place(relx=0.38,rely=0.36)

            global ulogin_etr1, ulogin_etr2,ulogin_etr0
            #label email 
            ulogin_lbl0=tk.Label(ureset_pass_frame,text="Enter your email:",font=("Regular",13),fg="white",bg="#0B1A41")
            ulogin_lbl0.place(relx=0.05,rely=0.08)
            #enter new pass entry box
            ulogin_etr0=CTkEntry(ureset_pass_frame,font=("Regular",12),corner_radius=8,fg_color="White",border_color="Black",text_color="Black")
            ulogin_etr0.place(relx=0.055,rely=0.17,relwidth=0.9,relheight=0.11)

            #new pass label
            ulogin_lbl1=tk.Label(ureset_pass_frame,text="Enter New Password:",font=("Regular",13),fg="white",bg="#0B1A41")
            ulogin_lbl1.place(relx=0.05,rely=0.33)
            #enter new pass entry box
            ulogin_etr1=CTkEntry(ureset_pass_frame,font=("Regular",12),corner_radius=8,fg_color="White",border_color="Black",show="*",text_color="Black")
            ulogin_etr1.place(relx=0.055,rely=0.41,relwidth=0.9,relheight=0.11)

            #confirm pass label
            ulogin_lbl2=tk.Label(ureset_pass_frame,text="Confirm new Password:",font=("Regular",13),fg="white",bg="#0B1A41")
            ulogin_lbl2.place(relx=0.05,rely=0.54)
            #entrybox for confirm password
            ulogin_etr2=CTkEntry(ureset_pass_frame,font=("Regular",12),corner_radius=8,fg_color="White",border_color="Black",show="*",text_color="Black")
            ulogin_etr2.place(relx=0.055,rely=0.62,relwidth=0.9,relheight=0.11)

            #the submit button
            ulogin_btn1=CTkButton(ureset_pass_frame,text="SUBMIT",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",border_width=2,command=reset_successful)
            ulogin_btn1.place(relx=0.37,rely=0.8,relwidth=0.3,relheight=0.1)

            #eye button in entry box
            ulogin_btn2=tk.Button(ulogin_etr1,image=ulogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p1)
            ulogin_btn2.place(relx=0.9,rely=0.3)
            #eye button in entry box
            ulogin_btn3=tk.Button(ulogin_etr2,image=ulogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p2)
            ulogin_btn3.place(relx=0.9,rely=0.3)
    

        #----------------------------------------------------------------------------------------------------#

#making pictures global so they dont get garbage collected 
    global ulogin_eyetk,ulogin_backtk,photo_ulogin_img1


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
    ulogin_b1=tk.Button(ulogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=sec_qsn)
    ulogin_b1.place(relx=0.713,rely=0.666)


    #login button
    ulogin_b2=CTkButton(ulogin_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
    ulogin_b2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


    #dont have account label
    ulogin_b5=tk.Label(ulogin_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    ulogin_b5.place(relx=0.2,rely=0.9)

    #button for dont have an account
    ulogin_b3=tk.Button(ulogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=click_here)
    ulogin_b3.place(relx=0.56,rely=0.896)


    # eye button
    ulogin_b4=tk.Button(ulogin_f1,image=ulogin_eyetk,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
    ulogin_b4.place(relx=0.8,rely=0.595)

    #the back button
    ulogin_b5=tk.Button(ulogin_f1,image=ulogin_backtk,text=" Back",compound=LEFT,bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    ulogin_b5.place(relx=0.048,rely=0.903)







#------------------------------------------admin login--------------------------------------------------------------#








def admin_login():
    """this function opens the admin login page when called."""
    #the main frame 
    main_frame4 = CTkFrame(root)
    main_frame4.place(relwidth = 1, relheight = 1,x = 0, y = 0)

    def back():
        '''function to get to dashboard page when back button is clicked''' 
        main_frame4.place_forget()
        main()


    def no_account():
        '''function to open admin_signup page when button in dont have an account is clicked'''
        main_frame4.place_forget()
        admin_signup()


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
        this function is made to reset the old password
        '''
        #----------------------------------------------database------------------------------------------#
        if alogin_etr0.get() == '' or alogin_etr1.get() == '' or alogin_etr2.get() == '' : 
            tk.messagebox.showerror("Error","All fields must be filled out.")
        elif alogin_e1.get() != alogin_etr0.get():
            tk.messagebox.showerror("Error","Incorrect email.")
        elif alogin_etr2.get()!= alogin_etr1.get():
            tk.messagebox.showerror("Error","Incorrect password.")
        elif len(alogin_etr1.get()) < 8 :
            tk.messagebox.showerror("Error","Password must be at least 8 characters long.")
        else:
            #update password to user database table
            conn=sqlite3.connect('mealmate.db')
            c=conn.cursor()
            c.execute("UPDATE admin SET password=? WHERE email=?",(alogin_etr2.get(),alogin_etr0.get()))
            conn.commit()
            conn.close()
            areset_pass_main_frame.place_forget()
            asign_sec_qsn_frame.place_forget()
            areset_pass_frame.place_forget()
            admin_login()        
            tk.messagebox.showinfo("Reset Successful","Password reset successful.")
        #------------------------------------------------------------------------------------------------#



        
        

    def login():
        """
        this function is made so that a messagebox is shown after clicking 
        the login button and the root window is destroyed . 
        """
        #checking if the entry box are filled
        if alogin_e1.get() == "" or alogin_e2.get() == "":
            tk.messagebox.showerror("Error","All fields are required.")
        
        else:
            try:
                conn = sqlite3.connect("mealmate.db")
                c = conn.cursor()


                # Fetch the record with the matching email and password
                c.execute("SELECT * FROM admin WHERE email = ? and password = ?", (alogin_e1.get(), alogin_e2.get()))
                result = c.fetchone()
                global a_email, a_password
                # Check if a result was found
                if result is not None:
                    # Assuming the email is in the 3rd column and the password in the 4th column
                    if alogin_e1.get() == result[2] and alogin_e2.get() == result[3]:
                        a_email = alogin_e1.get()
                        a_password = alogin_e2.get()
                        tk.messagebox.showinfo("Successful Message", "Login Successful!")
                        main_frame4.place_forget()
                        admin_dashboard()
                    else:
                        tk.messagebox.showerror("Error", "Invalid email or password.")
                else:
                    tk.messagebox.showerror("Error", "Invalid email or password.")

            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                conn.close()




                
        

    #---------------------------security question page---------------------------------------------#

    def sec_qsn():
        """This function opens the security questions page when called."""
        main_frame4.place_forget()
        main_frame1.place_forget()
        global asign_sec_qsn_frame,asec_entry1,asec_entry2,asec_entry3
        
        asign_sec_qsn_frame=tk.Frame(root)
        asign_sec_qsn_frame.place(relheight=1,relwidth=1,x=0,y=0)
        #the pic in the top label window
        asec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        asec_image_resize=asec_image.resize((961,1080))
        asec_image_tk=ImageTk.PhotoImage(asec_image_resize)
        asec_label1=tk.Label(asign_sec_qsn_frame,image=asec_image_tk)
        asec_label1.image = asec_image_tk  #reference to the picture
        asec_label1.place(relheight=1,relwidth=1,relx=0.2499)


    #the main frame of win1 
        asec_frame1=tk.Frame(asign_sec_qsn_frame,bg="#001129")
        asec_frame1.place(relheight=1,relwidth=0.5,x=0,y=0)

    #frame which contains the questions 
        asec_frame2=tk.Frame(asec_frame1,bg="#001129",width=626,height=800,bd=3,relief="groove")
        asec_frame2.place(relx=0.16,rely=0.1)

    #label for security questions heading
        asec_lbl2=tk.Label(asec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        asec_lbl2.place(relx=0.35,rely=0.08)

    #label for 1st question
        asec_lbl3=tk.Label(asec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        asec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        asec_entry1=CTkEntry(asec_frame2,fg_color="#74A9D8",width=380,height=40)
        asec_entry1.place(relx=0.13,rely=0.17)

    #label for 2nd question
        asec_lbl4=tk.Label(asec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        asec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        asec_entry2=CTkEntry(asec_frame2,fg_color="#74A9D8",width=380,height=40)
        asec_entry2.place(relx=0.13,rely=0.39)

    #label for 3rd question
        asec_lbl5=tk.Label(asec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        asec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        asec_entry3=CTkEntry(asec_frame2,fg_color="#74A9D8",width=380,height=40)
        asec_entry3.place(relx=0.13,rely=0.61)

    #the submit button
        asec_button1=CTkButton(asec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=reset_pass)
        asec_button1.place(relx=0.22,rely=0.8,relwidth=0.52,relheight=0.07)
        pass
    alogin_eye_img=Image.open("pictures//Vectorblack_eye1.png")
    alogin_eye_imgtk=ImageTk.PhotoImage(alogin_eye_img)



    def reset_p1():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if alogin_etr1.cget("show") == "":
            alogin_etr1.configure(show="*")
        else:
            alogin_etr1.configure(show="")

    def reset_p2():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if alogin_etr2.cget("show") == "":
            alogin_etr2.configure(show="*")
        else:
            alogin_etr2.configure(show="")



  #--------------------------------reset password page (admin)---------------------------------------------#


    def reset_pass():
        """this function opens the reset password page when called"""
        #fetch admin data from admin table
        conn = sqlite3.connect("mealmate.db")
        c = conn.cursor()
        c.execute("SELECT * FROM admin WHERE email = ?", (alogin_e1.get(),))
        admin_data = c.fetchone()





        #-----------------------------------------------database---------------------------------------------#
        if asec_entry1.get() == '' or asec_entry2.get() == '' or asec_entry3.get() == '':
            tk.messagebox.showerror("Error","All fields are required.")
        elif (asec_entry1.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Entered value must be a number.")
        if asec_entry1.get() == admin_data[4] and asec_entry2.get() == admin_data[5] and asec_entry3.get() == admin_data[6]:
            global ulogin_etr2,areset_pass_frame,alogin_etr1,alogin_etr2,areset_pass_main_frame
            asign_sec_qsn_frame.place_forget()

            areset_pass_main_frame=tk.Frame(root)
            areset_pass_main_frame.place(relheight=1,relwidth=1,x=0,y=0)

            reset_pass_image=Image.open("pictures/reset passreset_pass2.png")
            reset_pass_image_resize=reset_pass_image.resize((1920,1080))
            reset_pass_image_tk=ImageTk.PhotoImage(reset_pass_image_resize)
            reset_pass_label1=tk.Label(areset_pass_main_frame,image=reset_pass_image_tk)
            reset_pass_label1.image = reset_pass_image_tk  #reference to the picture
            reset_pass_label1.place(relheight=1,relwidth=1)
            
            areset_pass_frame=tk.Frame(areset_pass_main_frame,width=450,height=450,bd=3,relief="groove",bg="#0B1A41")
            areset_pass_frame.place(relx=0.38,rely=0.36)
            
            global alogin_etr1, alogin_etr2,alogin_etr0
            #label email 
            alogin_lbl0=tk.Label(areset_pass_frame,text="Enter your email:",font=("Regular",13),fg="white",bg="#0B1A41")
            alogin_lbl0.place(relx=0.05,rely=0.08)
            #enter new pass entry box
            alogin_etr0=CTkEntry(areset_pass_frame,font=("Regular",12),corner_radius=8,fg_color="White",border_color="Black",text_color="Black")
            alogin_etr0.place(relx=0.055,rely=0.17,relwidth=0.9,relheight=0.11)

            #label
            alogin_lbl1=tk.Label(areset_pass_frame,text="Enter New Password:",font=("Regular",13),fg="white",bg="#0B1A41")
            alogin_lbl1.place(relx=0.05,rely=0.33)
            #enter new pass entry box
            alogin_etr1=CTkEntry(areset_pass_frame,font=("Regular",12),corner_radius=8,fg_color="White",border_color="Black",show="*",text_color="Black")
            alogin_etr1.place(relx=0.055,rely=0.41,relwidth=0.9,relheight=0.11)

            #confirm pass label
            alogin_lbl2=tk.Label(areset_pass_frame,text="Confirm new Password:",font=("Regular",13),fg="white",bg="#0B1A41")
            alogin_lbl2.place(relx=0.05,rely=0.54)
            #entrybox for confirm password
            alogin_etr2=CTkEntry(areset_pass_frame,font=("Regular",12),corner_radius=8,fg_color="White",border_color="Black",show="*",text_color="Black")
            alogin_etr2.place(relx=0.055,rely=0.62,relwidth=0.9,relheight=0.11)

            #the submit button
            alogin_btn1=CTkButton(areset_pass_frame,text="SUBMIT",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",border_width=2,command=security_update)
            alogin_btn1.place(relx=0.35,rely=0.78,relwidth=0.3,relheight=0.11)

            #eye button in entry box
            alogin_btn2=tk.Button(alogin_etr1,image=alogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p1)
            alogin_btn2.place(relx=0.9,rely=0.3)
            #eye button in entry box
            alogin_btn3=tk.Button(alogin_etr2,image=alogin_eye_imgtk,bg="white",activebackground="white",bd=0,command=reset_p2)
            alogin_btn3.place(relx=0.9,rely=0.3)
    


#making pictures global so they dont get garbage collected 
    global alogin_eyetk,alogin_backtk,photo_alogin_logo



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
    alogin_btn1=tk.Button(alogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=sec_qsn)
    alogin_btn1.place(relx=0.713,rely=0.666)


    #login button
    alogin_btn2=CTkButton(alogin_f1,text="LOGIN",text_color="Black",corner_radius=8,fg_color="#543627",hover_color="#543627",font=("Inter",20,"bold"), command = login)
    alogin_btn2.place(relx=0.35,rely=0.77,relwidth=0.3,relheight=0.1)


    #dont have account label
    alogin_lbl5=tk.Label(alogin_f1,text="Dont have an account?",fg="White",bg="#888888",font=("Inter",15,"italic"))
    alogin_lbl5.place(relx=0.28,rely=0.9)

    #button for dont have an account
    alogin_btn3=tk.Button(alogin_f1,text="click here",bg="#888888",fg="#543627",activebackground="#888888",activeforeground="#543627",border=0,font=("Inter",15,"bold italic"),command=no_account)
    alogin_btn3.place(relx=0.64,rely=0.896)


    # eye button
    alogin_btn4=tk.Button(alogin_f1,image=alogin_eyetk,bg="#FAF3DB",activebackground="#FAF3DB",border=0,command=onclick)
    alogin_btn4.place(relx=0.8,rely=0.595)

    #the back button
    alogin_btn5=tk.Button(alogin_f1,image=alogin_backtk,text=" Back",compound=LEFT,bg="#888888",activebackground="#888888",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    alogin_btn5.place(relx=0.048,rely=0.903)


    



#-------------------------------------------------------user signup---------------------------------------------------------------#






def user_signup():
    '''This function opens the user signup page when called.'''


#the main frame
    main_frame3=CTkFrame(root)
    main_frame3.place(relwidth=1,relheight=1,x=0,y=0)



    def usignup_but():
        '''function to open user login page after clicking signup button'''
        #creating the database
        conn = sqlite3.connect("mealmate.db")
        #'cursor()' for executing the queries
        c = conn.cursor()
        #creating user registration table
        c.execute('''CREATE TABLE IF NOT EXISTS user 
                  ( 
                   first_name TEXT, 
                   last_name TEXT, 
                   email TEXT, 
                   password TEXT,
                  sec_ans1,
                  sec_ans2,
                  sec_ans3
                   )''')
    
        #fetching all email data from database of user 
        c.execute("SELECT email FROM user")
        emails = c.fetchall()
        a = []

        for email in emails:
            a.append(email[0])
        #saving the changes made in the database
        conn.commit()
        conn.close()
        
        #checking if the entry boxes are filled and entered the valid credentials

        if usignup_e1.get() == '' or usignup_e2.get() == '' or usignup_e3.get() == '' or usignup_e4.get() == '' or usignup_e5.get() == '' or usignup_e1.get() == 'firstname' or usignup_e2.get() == 'lastname' or usignup_e3.get() == 'example@gmail.com':
            tk.messagebox.showerror("Error", "Please fill all the required fields!")
        
        elif (usignup_e1.get()).isalpha() == False or (usignup_e2.get()).isalpha() == False:
            #show error
            tk.messagebox.showerror("Error", "Please enter valid first and last names!")


        elif '@gmail.com' not in usignup_e3.get() or len(usignup_e3.get()) <= 10 or ' ' in usignup_e3.get():
            #show error
            tk.messagebox.showerror("Error", "Please enter a valid email address!")


        elif usignup_e4.get() != usignup_e5.get():
            #show error
            tk.messagebox.showerror("Error", "Passwords do not match!")

        #check if email already exists in the user database table or not 




        elif len(usignup_e4.get()) < 8 :
            #show error
            tk.messagebox.showerror("Error", "Password should be at least 8 characters long!")  

        else:
            if usignup_e3.get() in a:
                #show error
                tk.messagebox.showerror("Error", "Email already exists!")
            else:
               tk.messagebox.showinfo("Success/Security_info","Signup validated! Now you need to fill the security questions so that you can reset your password in case if you forgot it by filling the questions . ")
               main_frame3.place_forget()
               sec_qsn()





    def back():
       '''function to open dashboard when back  button is clicked '''
       main_frame3.place_forget()
       main()




    def already_acc():
        '''function to open user login page when click here button is clicked in already have an account'''
        main_frame3.place_forget()
        user_login()




    def password():
        '''
        it is made so that we can hide or show password clicking the eye button in password
        '''
        if usignup_e4.cget("show") == "":
            usignup_e4.configure(show="*")
        else:
            usignup_e4.configure(show="")

    def repassword():
        '''
        it is made so that we can hide or show password clicking the eye button in  repassword
        '''
        if usignup_e5.cget("show") == "":
            usignup_e5.configure(show="*")
        else:
            usignup_e5.configure(show="")


    def security_info():
        '''
        this function is made to show a message when user clicks submit on the security question page
        '''



        #----------------------------DATABASE--------------------------#




        #checking if the entry is filled or not
        if usec_entry1.get() == '' or usec_entry2.get() == '' or usec_entry3.get() == '':
            tk.messagebox.showerror("Error", "Please fill all the required fields!")
        elif usec_entry1.get().isdigit() == False:
            tk.messagebox.showerror("Error", "Please enter a number in the first field!")
        else:

           #inserting security answers to the database
            conn = sqlite3.connect("mealmate.db")
            c = conn.cursor()
            
            #updating security questions
            #inserting data into the database
            c.execute('''INSERT INTO user (first_name, last_name, email, password, sec_ans1, sec_ans2, sec_ans3) 
                         VALUES (?,?,?,?,?,?,?)''',
                         ((usignup_e1.get()).capitalize(),(usignup_e2.get()).capitalize(),usignup_e3.get(),usignup_e4.get(),usec_entry1.get(), usec_entry2.get(), usec_entry3.get())
                     )
            conn.commit()
            conn.close()
            usign_sec_qsn_frame.place_forget()  
            user_login()       
            tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")

        


   #-------------------------------------------security questions page-------------------------------------------------#



    def sec_qsn():
        '''This function opens the security questions page when called.'''
        main_frame1.place_forget()
        global usign_sec_qsn_frame,usec_entry1,usec_entry2,usec_entry3
        
        usign_sec_qsn_frame=tk.Frame(root)
        usign_sec_qsn_frame.place(relheight=1,relwidth=1,x=0,y=0)
        #the pic in the top label window
        usec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        usec_image_resize=usec_image.resize((961,1080))
        usec_image_tk=ImageTk.PhotoImage(usec_image_resize)
        usec_label1=tk.Label(usign_sec_qsn_frame,image=usec_image_tk)
        usec_label1.image = usec_image_tk  #reference to the picture
        usec_label1.place(relheight=1,relwidth=1,relx=0.2499)


    #the main frame of win1 
        usec_frame1=tk.Frame(usign_sec_qsn_frame,bg="#001129")
        usec_frame1.place(relheight=1,relwidth=0.5,x=0,y=0)

    #frame which contains the questions 
        usec_frame2=tk.Frame(usec_frame1,bg="#001129",width=626,height=800,bd=3,relief="groove")
        usec_frame2.place(relx=0.16,rely=0.1)

    #label for security questions heading
        usec_lbl2=tk.Label(usec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        usec_lbl2.place(relx=0.35,rely=0.08)

    #label for 1st question
        usec_lbl3=tk.Label(usec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        usec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        usec_entry1=CTkEntry(usec_frame2,fg_color="#74A9D8",width=380,height=40)
        usec_entry1.place(relx=0.13,rely=0.17)

    #label for 2nd question
        usec_lbl4=tk.Label(usec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        usec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        usec_entry2=CTkEntry(usec_frame2,fg_color="#74A9D8",width=380,height=40)
        usec_entry2.place(relx=0.13,rely=0.39)

    #label for 3rd question
        usec_lbl5=tk.Label(usec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        usec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        usec_entry3=CTkEntry(usec_frame2,fg_color="#74A9D8",width=380,height=40)
        usec_entry3.place(relx=0.13,rely=0.61)

    #the submit button
        usec_button1=CTkButton(usec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_info)
        usec_button1.place(relx=0.22,rely=0.8,relwidth=0.52,relheight=0.07)




#making images global
    global tksignup_eye,tkusignup_i,photo_usignup_logo,usignup_backtk,photosignup_image1
    

    #the bg frame
    usignup_frame=tk.Frame(main_frame3,bg="Black")
    usignup_frame.place(relwidth=1,relheight=1)

    #the main bg picture 
    usignup_image1=Image.open("pictures\\f327a69f-4c36-4c1e-8965-c5a71e3d9d99.png")
    usignup_image1=usignup_image1.resize((968,1080))
    photosignup_image1=ImageTk.PhotoImage(usignup_image1)
    usignup_label = tk.Label(main_frame3, image=photosignup_image1)
    usignup_label.place(x=952, y=0, w=968, h=1080)


    #image for eye button in password and repassword
    usignup_eye=Image.open("pictures\\ion_eyeeye.png")
    tksignup_eye=ImageTk.PhotoImage(usignup_eye)


    #image for i button 
    usignup_i=Image.open("pictures\\Vector.png")
    tkusignup_i=ImageTk.PhotoImage(usignup_i)


    #label for mealmate logo
    usignup_logo=Image.open("pictures\\logo-no-2.png")
    usignup_logo=usignup_logo.resize((641,141))
    photo_usignup_logo=ImageTk.PhotoImage(usignup_logo)
    usignup_logo_lbl = tk.Label(main_frame3, image=photo_usignup_logo,bg="#262731")
    usignup_logo_lbl.place(x=138, y=62, w=641, h=141)

    #image for back button
    usignup_back=Image.open("pictures//Vectorarrow.png")
    usignup_backtk=ImageTk.PhotoImage(usignup_back)




    #the main frame
    usignup_f1=CTkFrame(usignup_frame,bg_color="transparent",corner_radius=10,fg_color="#262731",width=681,height=900)
    usignup_f1.place(x=100,y=39,w=681,h=900)
    global usignup_e1,usignup_e2,usignup_e3,usignup_e4,usignup_e5
    #sep frame
    sep_frame=tk.Frame(usignup_f1,bg="Black")
    sep_frame.place(relwidth=1,relheight=0.02,rely=0.2)

    #signup heading label
    usignup_lbl1=tk.Label(usignup_f1,text="User SignUp",font=("Inter",25,"bold"),bg="#262731",fg="white")
    usignup_lbl1.place(relx=0.32,rely=0.23)

    #firstname label
    usignup_lbl2=tk.Label(usignup_f1,text="First Name:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl2.place(relx=0.05,rely=0.3)

    #firstname entry
    usignup_e1=CTkEntry(usignup_f1,placeholder_text="firstname",fg_color="#FAF3DB",width=180,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    usignup_e1.place(relx=0.05,rely=0.33)

    #lastname label
    usignup_lbl3=tk.Label(usignup_f1,text="Last Name:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl3.place(relx=0.53,rely=0.29)

    #lastname entry
    usignup_e2=CTkEntry(usignup_f1,placeholder_text="lastname",fg_color="#FAF3DB",width=190,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    usignup_e2.place(relx=0.53,rely=0.33)

    #email label
    usignup_lbl4=tk.Label(usignup_f1,text="Email:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl4.place(relx=0.05,rely=0.43)

    #email entry
    usignup_e3=CTkEntry(usignup_f1,placeholder_text="example@gmail.com",fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
    usignup_e3.place(relx=0.05,rely=0.46)

    #password label
    usignup_lbl5=tk.Label(usignup_f1,text="Password:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl5.place(relx=0.05,rely=0.56)

    #password entry
    usignup_e4=CTkEntry(usignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
    usignup_e4.place(relx=0.05,rely=0.59)

    #repassword label
    usignup_lbl6=tk.Label(usignup_f1,text="Re-Password:",font=("Regular",15),bg="#262731",fg="White")
    usignup_lbl6.place(relx=0.05,rely=0.69)

    #repassword entry
    usignup_e5=CTkEntry(usignup_f1,fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",corner_radius=8,border_width=0,show="*")
    usignup_e5.place(relx=0.05,rely=0.72)



    #Signup button
    usignup_b2=CTkButton(usignup_f1,text="SIGN UP",fg_color="#FAF3DB",hover=0,height=45,font=("Inter",20,"bold"),text_color="#4D5053",corner_radius=8,command=usignup_but)
    usignup_b2.place(relx=0.35,rely=0.88)

    #eye button in password
    usignup_b3=tk.Button(usignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = password)
    usignup_b3.place(relx=0.8,rely=0.61)

    #eye button in repassword
    usignup_b4=tk.Button(usignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = repassword)
    usignup_b4.place(relx=0.8,rely=0.74)


    #already an account label
    usignup_lbl7=tk.Label(usignup_f1,text="Already have an account?",font=("Inter",12,"italic"),bg="#262731",fg="White")
    usignup_lbl7.place(relx=0.48,rely=0.84)

    # click here button 
    usignup_b5=tk.Button(usignup_f1,text="click here",font=("Inter",12,"bold italic"),bg="#262731",fg="#DD2323",activebackground="#262731",bd=0,command=already_acc)
    usignup_b5.place(relx=0.76,rely=0.84)

    #back button 
    usignup_btn1=tk.Button(usignup_f1,image=usignup_backtk,text=" Back",compound=LEFT,bg="#262731",activebackground="#262731",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    usignup_btn1.place(relx=0.048,rely=0.94)
    






  #-----------------------------------------------------admin signup---------------------------------------------------#





 


def admin_signup():
    '''This function opens the admin signup page when called.'''
    #the main frame
    main_frame5=CTkFrame(root)
    main_frame5.place(relwidth=1,relheight=1,x=0,y=0)


    def asignup_but():
        '''function to open admin login page after signup'''

        #creating the database
        conn = sqlite3.connect("mealmate.db")
        #'cursor()' for executing the queries
        c = conn.cursor()
        #creating admin registration table
        c.execute('''CREATE TABLE IF NOT EXISTS admin 
                  ( 
                   first_name TEXT, 
                   last_name TEXT, 
                   email TEXT, 
                   password TEXT,
                  sec_ans1,
                  sec_ans2,
                  sec_ans3
                   )''')
        global a_emails
        #fetching all email data from database of user 
        c.execute("SELECT email FROM admin")
        a_emails = c.fetchall()
        a_a = []

        for email in a_emails:
            a_a.append(email[0])
            #saving the changes made in the database
        conn.commit()
        conn.close()
        

        #checking if the entry boxes are filled and entered the valid credentials

        if asignup_e1.get() == '' or asignup_e2.get() == '' or asignup_e3.get() == '' or asignup_e4.get() == '' or asignup_e5.get() == '' or asignup_e1.get() == 'firstname' or asignup_e2.get() == 'lastname' or asignup_e3.get() == 'example@admin.gmail.com':
            tk.messagebox.showerror("Error", "Please fill all the required fields!")


        elif (asignup_e1.get()).isalpha() == False or (asignup_e2.get()).isalpha() == False:
            #show error
            tk.messagebox.showerror("Error", "Please enter valid first and last names!")

        elif '@admin.gmail.com' not in asignup_e3.get() or len(asignup_e3.get()) <= 16 or ' ' in asignup_e3.get():
            #show error
            tk.messagebox.showerror("Error", "Please enter a valid email address!")


        elif asignup_e4.get() != asignup_e5.get():
            #show error
            tk.messagebox.showerror("Error", "Passwords do not match!")


        elif len(asignup_e4.get()) < 8 :
            #show error
            tk.messagebox.showerror("Error", "Password should be at least 8 characters long!")
            

        

        else:
         if asignup_e3.get() in a_a:
            #show error
            tk.messagebox.showerror("Error", "User account already registered!")
         else:
            tk.messagebox.showinfo("Success/Security_info","Signup validated! Now you need to fill the security questions so that you can reset your password in case if you forgot it by filling the questions . ")
            main_frame5.place_forget()
            asec_qsn()

         #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#        

    def back():
        '''function to open dashboard when back button is clicked '''
        main_frame5.place_forget()
        main()




    def already_acc():
        '''function for click here ]button in already have an account'''
        main_frame5.place_forget()
        admin_login()




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
        #checking if the entry is filled or not
        if asec_entry1.get() == '' or asec_entry2.get() == '' or asec_entry3.get() == '':
            tk.messagebox.showerror("Error", "Please fill all the required fields!")

        elif asec_entry1.get().isdigit() == False:
            tk.messagebox.showerror("Error", "Please enter a number in the first field!")

        else:

           #inserting security answers to the database (admin)
            conn = sqlite3.connect("mealmate.db")
            c = conn.cursor()
            
            #inserting data into the database (admin)
            c.execute('''INSERT INTO admin (first_name, last_name, email, password, sec_ans1, sec_ans2, sec_ans3) 
                         VALUES (?,?,?,?,?,?,?)''',
                         ((asignup_e1.get()).capitalize(),asignup_e2.get().capitalize(),asignup_e3.get(),asignup_e4.get(),asec_entry1.get(), asec_entry2.get(), asec_entry3.get())
                     )
            
            #for saving the changes made in the database
            conn.commit()
            conn.close()

        asign_sec_qsn_frame.place_forget()
        admin_login()
        tk.messagebox.showinfo("Successful Message ","Security questions Entry Successful !")

    

  #--------------------------------------------security question page(admin)----------------------------------------------------#


    def asec_qsn():
        '''This function opens the security questions page when called.'''
        main_frame5.place_forget()
        main_frame1.place_forget()
        global asign_sec_qsn_frame, asec_entry1,asec_entry2,asec_entry3
        
        asign_sec_qsn_frame=tk.Frame(root)
        asign_sec_qsn_frame.place(relheight=1,relwidth=1,x=0,y=0)
        #the pic in the top label window
        asec_image=Image.open("pictures\\forgot-pass-pic.jpg")
        asec_image_resize=asec_image.resize((961,1080))
        asec_image_tk=ImageTk.PhotoImage(asec_image_resize)
        asec_label1=tk.Label(asign_sec_qsn_frame,image=asec_image_tk)
        asec_label1.image = asec_image_tk  #reference to the picture
        asec_label1.place(relheight=1,relwidth=1,relx=0.2499)


    #the main frame of win1 
        asec_frame1=tk.Frame(asign_sec_qsn_frame,bg="#001129")
        asec_frame1.place(relheight=1,relwidth=0.5,x=0,y=0)

    #frame which contains the questions 
        asec_frame2=tk.Frame(asec_frame1,bg="#001129",width=626,height=800,bd=3,relief="groove")
        asec_frame2.place(relx=0.16,rely=0.1)

    #label for security questions heading
        asec_lbl2=tk.Label(asec_frame1,text="Security Questions",font=("Inter",20,"bold"),fg="White",bg="#001129")
        asec_lbl2.place(relx=0.35,rely=0.08)

    #label for 1st question
        asec_lbl3=tk.Label(asec_frame2,text="Q1.  Which is your favourite number?",fg="White",bg="#001129",font=("Regular",15))
        asec_lbl3.place(relx=0.05,rely=0.1)

    #entry for 1st question
        asec_entry1=CTkEntry(asec_frame2,fg_color="#74A9D8",width=380,height=40)
        asec_entry1.place(relx=0.13,rely=0.17)

    #label for 2nd question
        asec_lbl4=tk.Label(asec_frame2,text="Q2.  Which is your favourite food?",fg="White",bg="#001129",font=("Regular",15))
        asec_lbl4.place(relx=0.05,rely=0.32)

    #entry for 2nd question
        asec_entry2=CTkEntry(asec_frame2,fg_color="#74A9D8",width=380,height=40)
        asec_entry2.place(relx=0.13,rely=0.39)

    #label for 3rd question
        asec_lbl5=tk.Label(asec_frame2,text="Q3.  Which is your favourite color?",fg="White",bg="#001129",font=("Regular",15))
        asec_lbl5.place(relx=0.05,rely=0.54)

    #entry for 3rd question
        asec_entry3=CTkEntry(asec_frame2,fg_color="#74A9D8",width=380,height=40)
        asec_entry3.place(relx=0.13,rely=0.61)

    #the submit button
        asec_button1=CTkButton(asec_frame2,text="SUBMIT",fg_color="#003554",text_color="White",font=("Inter",18,"bold"),command=security_info)
        asec_button1.place(relx=0.22,rely=0.8,relwidth=0.52,relheight=0.07)
        



    global tksignup_eye,tkasignup_i,photo_asignup_logo,asignup_backtk,photosignup_image1,areset_pass_frame
    global asignup_e1, asignup_e2, asignup_e3, asignup_e4, asignup_e5
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
    asignup_lbl1=tk.Label(asignup_f1,text="Admin SignUp",font=("Inter",25,"bold"),bg="#262731",fg="white")
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
    asignup_e3=CTkEntry(asignup_f1,placeholder_text="example@admin.gmail.com ",fg_color="#FAF3DB",width=450,height=50,font=("Regular",15),text_color="#DD2323",placeholder_text_color="#DD2323",corner_radius=8,border_width=0)
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


    #Signup button
    asignup_b2=CTkButton(asignup_f1,text="SIGN UP",fg_color="#FAF3DB",hover=0,height=45,font=("Inter",20,"bold"),text_color="#4D5053",corner_radius=8,command=asignup_but)
    asignup_b2.place(relx=0.35,rely=0.88)

    #eye button in password
    asignup_b3=tk.Button(asignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = password)
    asignup_b3.place(relx=0.8,rely=0.61)

    #eye button in repassword
    asignup_b4=tk.Button(asignup_f1,image=tksignup_eye,bd=0,bg="#FAF3DB",activebackground="#FAF3DB",command = repassword)
    asignup_b4.place(relx=0.8,rely=0.74)



    #already an account label
    asignup_lbl7=tk.Label(asignup_f1,text="Already have an account?",font=("Inter",12,"italic"),bg="#262731",fg="White")
    asignup_lbl7.place(relx=0.48,rely=0.84)

    # click here button 
    asignup_b5=tk.Button(asignup_f1,text="click here",font=("Inter",12,"bold italic"),bg="#262731",fg="#DD2323",activebackground="#262731",bd=0,command=already_acc)
    asignup_b5.place(relx=0.76,rely=0.84)

    #the back button
    asignup_btn1=tk.Button(asignup_f1,image=asignup_backtk,text=" Back",compound=LEFT,bg="#262731",activebackground="#262731",bd=0,font=("Inter",13),fg="White",activeforeground="White",command=back)
    asignup_btn1.place(relx=0.048,rely=0.94)
    


    


#-------------------------------------------------------admin dashboard-------------------------------------------------------------#






def admin_dashboard():
    '''This function opens the admin dashboard page when called.'''
    # the main frame
    main_frame6=CTkFrame(root,fg_color="Black")
    main_frame6.place(relheight=1,relwidth=1,relx=0,rely=0)


    #--------------------------------------------------------database-------------------------------------------------------------#
        #connecting to database
    global admin_data
    conn = sqlite3.connect('mealmate.db')
    c = conn.cursor()
        #fetching data of admin table
    c.execute("SELECT * FROM admin WHERE email = ? and password = ?", (a_email, a_password))
    admin_data = c.fetchall()

        #close connection
    conn.close()
        #-----------------------------------------------------------------------------------------------------------------------------#

    def on_hover(enter):
        '''to change the text colour and image of button on entering the widget'''
        admin_db_btn2.configure(image=a_db_img5ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

    def off_hover(leave):
        '''to change the text colour and image of button on exiting the widget'''
        admin_db_btn2.configure(image=a_db_img1ctk,text_color="#DD2323",fg_color="#D9D9D9")


    def on_hover2(enter):
        '''to change the text colour and image of button on entering the widget'''
        admin_db_btn3.configure(text_color="#33303C",fg_color="#F38686",hover_color="#F38686")
        admin_db_btn3_lbl.configure(image=a_db_img6ctk,fg_color="#F38686",bg_color="#F38686")

    def off_hover2(leave):
        '''to change the text colour and image of button on exiting the widget'''
        admin_db_btn3.configure(text_color="#DD2323",fg_color="#D9D9D9")
        admin_db_btn3_lbl.configure(image=a_db_img2ctk,fg_color="#D9D9D9",bg_color="#D9D9D9")


    def on_hover3(enter):
        '''to change the text colour and image of button on entering the widget'''
        admin_db_btn4.configure(image=a_db_img7ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

    def off_hover3(leave):
        '''to change the text colour and image of button on exiting the widget'''
        admin_db_btn4.configure(image=a_db_img3ctk,text_color="#DD2323",fg_color="#D9D9D9")


    def on_hover4(enter):
        '''to change the text colour and image of button on entering the widget'''
        admin_db_btn5.configure(image=a_db_img8ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

    def off_hover4(leave):
        '''to change the text colour and image of button on exiting the widget'''
        admin_db_btn5.configure(image=a_db_img4ctk,text_color="#DD2323",fg_color="#D9D9D9")
   
    #--------------------------------------------------------update food-------------------------------------------------------------#
    def update_food1():
        if a_db_etrr1.get() == '' or a_db_etrr2.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr2.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr1.get(), a_db_etrr2.get(), 1))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food2():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 2))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food3():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 3))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food4():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 4))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food5():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 5))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food6():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 6))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")



    def update_food7():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 7))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food8():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 8))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food9():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 9))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food10():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 10))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")



    def update_food11():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 11))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")



    def update_food12():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 12))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")



    def update_food13():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 13))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")



    def update_food14():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 14))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")




    def update_food15():
        if a_db_etrr3.get() == '' or a_db_etrr4.get() == '':
            tk.messagebox.showerror("Error","Please enter all fields")
        elif (a_db_etrr4.get()).isdigit() == False:
            tk.messagebox.showerror("Error","Price should be a number")
        else:
            conn = sqlite3.connect('mealmate.db')
            c = conn.cursor()
            c.execute("UPDATE item SET item_name =?, item_price =? where rowid = ?", (a_db_etrr3.get(), a_db_etrr4.get(), 15))
            conn.commit()
            conn.close()
            tk.messagebox.showinfo("Success","Food item updated successfully")

        
    #--------------------------------------------------------------------------------------------------------------------------------#




    def go_to_dash():
        '''this function is made to ask yes no question and if the
        answer is yes then a messagebox would be shown when logout button is clicked and dashboard page is opened'''
        admin_logout=tk.messagebox.askyesno("Logout?","Are you sure you want to log out?")
        if admin_logout==1:
            main_frame6.place_forget()
            main()



    def a_db_exit():
        '''this function is made to ask yes no question to exit the page or not and if answer is yes then a messagebox is 
        shown and the root window is destroyed'''
        response = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if response==1:
            root.destroy()

    def win3_cancel():
        win3.destroy()

    def a_db_edit():

        global win3, a_db_etrr1, a_db_etrr2
        win3=tk.Toplevel()
        win3.title("Edit Items")
        win3.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win3.geometry("500x250")
        win3.resizable(0,0)
        win3_main_frame=tk.Frame(win3,bg="#33303C")
        win3_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl1=tk.Label(win3_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl1.place(relx=0.05,rely=0.08)
        a_db_etrr1=CTkEntry(win3_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Chicken Burger",placeholder_text_color="#33303c")
        a_db_etrr1.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl2=tk.Label(win3_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl2.place(relx=0.05,rely=0.33)
        a_db_etrr2=CTkEntry(win3_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.350",placeholder_text_color="#33303C")
        a_db_etrr2.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn1=CTkButton(win3_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win3_cancel)
        a_db_btnn1.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn2=CTkButton(win3_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food1)
        a_db_btnn2.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win4_cancel():
        win4.destroy()

    def a_db_edit2():
        global win4, a_db_etrr3,a_db_etrr4
        win4=tk.Toplevel()
        win4.title("Edit Items")
        win4.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win4.geometry("500x250")
        win4.resizable(0,0)
        win4_main_frame=tk.Frame(win4,bg="#33303C")
        win4_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win4_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win4_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Espresso",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win4_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win4_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.210",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win4_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win4_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win4_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food2)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win5_cancel():
        win5.destroy() 

    def a_db_edit3():
        global win5, a_db_etrr3, a_db_etrr4
        win5=tk.Toplevel()
        win5.title("Edit Items")
        win5.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win5.geometry("500x250")
        win5.resizable(0,0)
        win5_main_frame=tk.Frame(win5,bg="#33303C")
        win5_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win5_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win5_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Chicken Pizza",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win5_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win5_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.510",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win5_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win5_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win5_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food3)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win6_cancel():
        win6.destroy()

    def a_db_edit4():
        global win6, a_db_etrr3, a_db_etrr4
        win6=tk.Toplevel()
        win6.title("Edit Items")
        win6.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win6.geometry("500x250")
        win6.resizable(0,0)
        win6_main_frame=tk.Frame(win6,bg="#33303C")
        win6_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win6_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win6_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Pepsi",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win6_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win6_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.70",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win6_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win6_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win6_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food4)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win7_cancel():
        win7.destroy()

    def a_db_edit5():
        global win7, a_db_etrr3, a_db_etrr4
        win7=tk.Toplevel()
        win7.title("Edit Items")
        win7.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win7.geometry("500x250")
        win7.resizable(0,0)
        win7_main_frame=tk.Frame(win7,bg="#33303C")
        win7_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win7_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win7_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Drumstick",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win7_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win7_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.110",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win7_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win7_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win7_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food5)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win8_cancel():
        win8.destroy()

    def a_db_edit6():
        global win8, a_db_etrr3, a_db_etrr4
        win8=tk.Toplevel()
        win8.title("Edit Items")
        win8.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win8.geometry("500x250")
        win8.resizable(0,0)
        win8_main_frame=tk.Frame(win8,bg="#33303C")
        win8_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win8_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win8_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Cold Coffee",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win8_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win8_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.280",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win8_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win8_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win8_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food6)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win9_cancel():
        win9.destroy()

    def a_db_edit7():
        global win9, a_db_etrr3, a_db_etrr4
        win9=tk.Toplevel()
        win9.title("Edit Items")
        win9.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win9.geometry("500x250")
        win9.resizable(0,0)
        win9_main_frame=tk.Frame(win9,bg="#33303C")
        win9_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win9_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win9_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="French Fries",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win9_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win9_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.280",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win9_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win9_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win9_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food7)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win10_cancel():
        win10.destroy()

    def a_db_edit8():
        global win10, a_db_etrr3, a_db_etrr4
        win10=tk.Toplevel()
        win10.title("Edit Items")
        win10.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win10.geometry("500x250")
        win10.resizable(0,0)
        win10_main_frame=tk.Frame(win10,bg="#33303C")
        win10_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win10_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win10_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Coca Cola",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win10_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win10_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.70",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win10_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win10_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win10_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food8)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win11_cancel():
        win11.destroy()

    def a_db_edit9():
        global win11, a_db_etrr3, a_db_etrr4
        win11=tk.Toplevel()
        win11.title("Edit Items")
        win11.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win11.geometry("500x250")
        win11.resizable(0,0)
        win11_main_frame=tk.Frame(win11,bg="#33303C")
        win11_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win11_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win11_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Oreo Shake",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win11_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win11_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.450",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win11_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win11_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win11_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food9)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win12_cancel():
        win12.destroy()

    def a_db_edit10():
        global win12, a_db_etrr3, a_db_etrr4
        win12=tk.Toplevel()
        win12.title("Edit Items")
        win12.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win12.geometry("500x250")
        win12.resizable(0,0)
        win12_main_frame=tk.Frame(win12,bg="#33303C")
        win12_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win12_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win12_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Fanta",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win12_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win12_main_frame,font=("Regular",12),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.70",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win12_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win12_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win12_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food10)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win13_cancel():
        win13.destroy()

    def a_db_edit11():
        global win13, a_db_etrr3, a_db_etrr4
        win13=tk.Toplevel()
        win13.title("Edit Items")
        win13.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win13.geometry("500x250")
        win13.resizable(0,0)
        win13_main_frame=tk.Frame(win13,bg="#33303C")
        win13_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win13_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win13_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Cappuccino",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win13_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win13_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.220",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win13_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win13_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win13_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food11)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win14_cancel():
        win14.destroy()

    def a_db_edit12():
        global win14, a_db_etrr3, a_db_etrr4
        win14=tk.Toplevel()
        win14.title("Edit Items")
        win14.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win14.geometry("500x250")
        win14.resizable(0,0)
        win14_main_frame=tk.Frame(win14,bg="#33303C")
        win14_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win14_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win14_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Chicken MoMo",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win14_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win14_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.200",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win14_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win14_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win14_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food12)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)

    def win15_cancel():
        win15.destroy()

    def a_db_edit13():
        global win15, a_db_etrr3, a_db_etrr4
        win15=tk.Toplevel()
        win15.title("Edit Items")
        win15.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win15.geometry("500x250")
        win15.resizable(0,0)
        win15_main_frame=tk.Frame(win15,bg="#33303C")
        win15_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win15_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win15_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Sprite",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win15_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win15_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.70",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win15_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win15_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win15_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food13)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win16_cancel():
        win16.destroy()

    def a_db_edit14():
        global win16, a_db_etrr3, a_db_etrr4
        win16=tk.Toplevel()
        win16.title("Edit Items")
        win16.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win16.geometry("500x250")
        win16.resizable(0,0)
        win16_main_frame=tk.Frame(win16,bg="#33303C")
        win16_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win16_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win16_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Chicken Chowmein",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win16_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win16_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.250",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win16_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win16_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win16_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2,command = update_food14)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)
    
    def win17_cancel():
        win17.destroy()

    def a_db_edit15():
        global win17, a_db_etrr3, a_db_etrr4
        win17=tk.Toplevel()
        win17.title("Edit Items")
        win17.iconbitmap("pictures/32432hotbeverage_98916.ico")
        win17.geometry("500x250")
        win17.resizable(0,0)
        win17_main_frame=tk.Frame(win17,bg="#33303C")
        win17_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        a_db_labl3=tk.Label(win17_main_frame,text="Name:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl3.place(relx=0.05,rely=0.08)
        a_db_etrr3=CTkEntry(win17_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Chicken Biryani",placeholder_text_color="#33303c")
        a_db_etrr3.place(relx=0.055,rely=0.17,relwidth=0.8,relheight=0.13)

        a_db_labl4=tk.Label(win17_main_frame,text="Price:",font=("Regular",13),fg="white",bg="#33303C")
        a_db_labl4.place(relx=0.05,rely=0.33)
        a_db_etrr4=CTkEntry(win17_main_frame,font=("Regular",13),corner_radius=0,fg_color="White",border_color="Black",text_color="#33303C",placeholder_text="Rs.250",placeholder_text_color="#33303C")
        a_db_etrr4.place(relx=0.055,rely=0.43,relwidth=0.8,relheight=0.13)

        a_db_btnn3=CTkButton(win17_main_frame,text="CANCEL",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Red",hover_color="#D9D9D9",border_width=2,command=win17_cancel)
        a_db_btnn3.place(relx=0.1,rely=0.75,relwidth=0.3,relheight=0.15)

        a_db_btnn4=CTkButton(win17_main_frame,text="CONFIRM",font=("Inter",15,"bold"),corner_radius=0,fg_color="White",border_color="Black",text_color="Black",hover_color="#D9D9D9",border_width=2, command = update_food15)
        a_db_btnn4.place(relx=0.6,rely=0.75,relwidth=0.3,relheight=0.15)







    global admin_db_frame3,admin_db_btn2,admin_db_btn3,admin_db_btn4,admin_db_btn3_lbl,photo_a_db_logo,admin_db_btn6,a_db_img9tk





        #----------------------------------------dashboard main frame------------------------------------------------#



    def dashboard_frame_ad():
        '''This function opens the dashboard frame when called.'''
        global s_f_frame,admin_db_frame3,admin_db_customer_frame
        #dashboard frame
        admin_db_frame3=tk.Frame(main_frame6,bg="White")
        
        #items frame
        s_f_frame=tk.Frame(main_frame6)

        #Customers frame
        admin_db_customer_frame=tk.Frame(main_frame6,bg="black")
        

        s_f_frame.place_forget()
        admin_db_customer_frame.place_forget()

        global admin_db_btn3,admin_db_btn3_lbl,admin_db_btn2,admin_db_btn4,admin_db_btn2_dash
        a_db_btn9.configure(text="             Dashboard")
        admin_db_btn2.place_forget()

    #dahboard button
        admin_db_btn2_dash=CTkButton(admin_db_frame2,image=a_db_img5ctk,fg_color="#F38686",text="Dashboard",text_color="#33303C",corner_radius=7,hover=0)
        admin_db_btn2_dash.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

    #Items button
        admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
        admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
        admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
        admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

    #Customers button
        admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
        admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

        #bindings so that that buttons act as intended
        admin_db_btn3.bind("<Enter>", on_hover2)
        admin_db_btn3.bind("<Leave>", off_hover2)
        admin_db_btn4.bind("<Enter>", on_hover3)
        admin_db_btn4.bind("<Leave>", off_hover3)



        #Dashboard Frame
        admin_db_frame3.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)

        
        #the bg image
        global photo_a_db_bg,a_db_lbl2
        a_db_bg=Image.open("pictures/5883 1bg_adb.png")
        a_db_bg=a_db_bg.resize((1250,683))
        photo_a_db_bg=ImageTk.PhotoImage(a_db_bg)
        a_db_lbl2 = tk.Label(admin_db_frame3, image=photo_a_db_bg)
        a_db_lbl2.place(x=0, y=0, w=1250, h=683)

        #welcome label
        a_db_lbl6=tk.Label(admin_db_frame3,text="Welcome,",font=("Inter",60,"bold"),bg="White")
        a_db_lbl6.place(relx=0.26,rely=0.78)

    #admin name label after welcome label
        a_db_lbl7=tk.Label(admin_db_frame3,text=admin_data[0][0],font=("Inter",60,"bold"),bg="White",fg="#DD2323")
        a_db_lbl7.place(relx=0.55,rely=0.78)
        


        

        #-----------------------------------admin_customize_items frame-------------------------------------------------------#






    def items_frame_ad():
        """this function is made to make frame in dashboard swap with the frame in items page and make other buttons hover as usual
        #to configure dashboard label to item label"""

        global photo_u_db_img3tk,photo_u_db_img4tk,photo_u_db_img5tk,photo_u_db_img6tk,photo_u_db_img7tk,photo_u_db_img8tk,photo_u_db_img9tk,photo_u_db_img10tk,photo_u_db_img11tk,photo_u_db_img12tk,photo_u_db_img13tk,photo_u_db_img14tk,photo_u_db_img15tk,photo_u_db_img16tk,photo_u_db_img17tk
        a_db_btn9.configure(text="    Items")
        
        #making the buttons global 
        global admin_db_btn3,admin_db_btn3_lbl,admin_db_btn2,admin_db_btn4

        #forgetting the dashboard frame
        admin_db_frame3.place_forget()
        #forgetting the initial items button to replace it with another button
        admin_db_btn3.place_forget()
        #forgetting the customersframe
        admin_db_customer_frame.place_forget()

        
        #Items button
        admin_db_btn3_items=CTkButton(admin_db_frame2,fg_color="#F38686",text="Items",text_color="#33303C",corner_radius=7,hover=0)
        admin_db_btn3_items.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
        #image in items button
        admin_db_btn3_items_lbl=CTkLabel(admin_db_btn3_items,image=a_db_img6ctk,text="")
        admin_db_btn3_items_lbl.place(relx=0.3,rely=0.1)

        #dashboard button
        admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
        admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

        #customers button
        admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
        admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

        #bindings so that that buttons act as intended
        admin_db_btn2.bind("<Enter>", on_hover)
        admin_db_btn2.bind("<Leave>", off_hover)
        admin_db_btn4.bind("<Enter>", on_hover3)
        admin_db_btn4.bind("<Leave>", off_hover3)


        #Scrollable frame that contains all items
        s_f_frame.place(relwidth=0.6,relheight=0.85,relx=0.32,rely=0.13)
        u_db_sframe=CTkScrollableFrame(s_f_frame,corner_radius=0,fg_color="Black",scrollbar_button_color="white",scrollbar_button_hover_color="#D9D9D9")
        u_db_sframe.place(relwidth=1,relheight=1)

    #button 1 in scrollable frame
        u_db_button1=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button1.grid(row=0,column=0,padx=20,pady=20)
        u_db_btn4=CTkButton(u_db_button1,text="EDIT",font=("Inter",18,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit)
        u_db_btn4.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 1
        u_db_img3=Image.open("pictures/pngegg (2) 1Bargar.png")
        u_db_img3=u_db_img3.resize((230,210))
        photo_u_db_img3tk=ImageTk.PhotoImage(u_db_img3)
        u_db_img3_lbl = tk.Label(u_db_button1, image=photo_u_db_img3tk,bg="#D9D9D9")
        u_db_img3_lbl.place(x=15, y=5, w=230, h=210)
        u_db_label1=tk.Label(u_db_button1,text=f"Name: {items_lst[0][0]}\n  Price: Rs.{price_lst[0][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label1.place(relx=0.1,rely=0.6)

    #button 2 in scrollable frame
        u_db_button2=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button2.grid(row=0,column=2,padx=20,pady=20)
        u_db_btn5=CTkButton(u_db_button2,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit3)
        u_db_btn5.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 2
        u_db_img4=Image.open("pictures/pngegg (6) 1pizza.png")
        u_db_img4=u_db_img4.resize((220,200))
        photo_u_db_img4tk=ImageTk.PhotoImage(u_db_img4)
        u_db_img4_lbl = tk.Label(u_db_button2, image=photo_u_db_img4tk,bg="#D9D9D9")
        u_db_img4_lbl.place(x=15, y=5, w=220, h=200)
        u_db_label2=tk.Label(u_db_button2,text=f"Name: {items_lst[2][0]}\n  Price: Rs.{price_lst[2][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label2.place(relx=0.1,rely=0.6)

    #button 3 in scrollable frame
        u_db_button3=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button3.grid(row=0,column=1,padx=0,pady=0)
        u_db_btn6=CTkButton(u_db_button3,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit2)
        u_db_btn6.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 3
        u_db_img5=Image.open("pictures/pngegg (8) 1cooooofe.png")
        u_db_img5=u_db_img5.resize((210,190))
        photo_u_db_img5tk=ImageTk.PhotoImage(u_db_img5)
        u_db_img5_lbl = tk.Label(u_db_button3, image=photo_u_db_img5tk,bg="#D9D9D9")
        u_db_img5_lbl.place(x=10, y=5, w=210, h=190)
        u_db_label3=tk.Label(u_db_button3,text=f"Name: {items_lst[1][0]}\n   Price: Rs.{price_lst[1][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label3.place(relx=0.17,rely=0.6)

    #button 4 in scrollable frame
        u_db_button4=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button4.grid(row=0,column=3,pady=0)
        u_db_btn7=CTkButton(u_db_button4,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit4)
        u_db_btn7.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 4
        u_db_img6=Image.open("pictures/pngegg (4) 1pepsii.png")
        u_db_img6=u_db_img6.resize((160,160))
        photo_u_db_img6tk=ImageTk.PhotoImage(u_db_img6)
        u_db_img6_lbl = tk.Label(u_db_button4, image=photo_u_db_img6tk,bg="#D9D9D9")
        u_db_img6_lbl.place(x=45, y=15, w=160, h=160)
        u_db_label4=tk.Label(u_db_button4,text=f"   Name:{items_lst[3][0]}\n   Price: Rs.{price_lst[3][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label4.place(relx=0.16,rely=0.6)

    #button 5 in scrollable frame
        u_db_button5=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button5.grid(row=1,column=0,padx=20,pady=0)
        u_db_btn8=CTkButton(u_db_button5,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit5)
        u_db_btn8.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 5
        u_db_img7=Image.open("pictures/pngegg (7) 1fried_chicken.png")
        u_db_img7=u_db_img7.resize((210,190))
        photo_u_db_img7tk=ImageTk.PhotoImage(u_db_img7)
        u_db_img7_lbl = tk.Label(u_db_button5, image=photo_u_db_img7tk,bg="#D9D9D9")
        u_db_img7_lbl.place(x=25, y=4, w=210, h=190)
        u_db_label5=tk.Label(u_db_button5,text=f"Name: {items_lst[4][0]}\n   Price: Rs.{price_lst[4][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label5.place(relx=0.17,rely=0.6)

    #button 6 in scrollable frame
        u_db_button6=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button6.grid(row=1,column=1,padx=0,pady=0)
        u_db_btn9=CTkButton(u_db_button6,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit6)
        u_db_btn9.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 6
        u_db_img8=Image.open("pictures/pngegg (12) 1coffee_shake.png")
        u_db_img8=u_db_img8.resize((190,170))
        photo_u_db_img8tk=ImageTk.PhotoImage(u_db_img8)
        u_db_img8_lbl = tk.Label(u_db_button6, image=photo_u_db_img8tk,bg="#D9D9D9")
        u_db_img8_lbl.place(x=25, y=12, w=190, h=170)
        u_db_label6=tk.Label(u_db_button6,text=f"Name: {items_lst[5][0]}\n   Price: Rs.{price_lst[5][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label6.place(relx=0.15,rely=0.6)

    #button 7 in scrollable frame
        u_db_button7=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button7.grid(row=1,column=2,padx=0,pady=0)
        u_db_btn10=CTkButton(u_db_button7,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit7)
        u_db_btn10.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 7
        u_db_img9=Image.open("pictures/pngegg (3) 1french_fries.png")
        u_db_img9=u_db_img9.resize((210,200))
        photo_u_db_img9tk=ImageTk.PhotoImage(u_db_img9)
        u_db_img9_lbl = tk.Label(u_db_button7, image=photo_u_db_img9tk,bg="#D9D9D9")
        u_db_img9_lbl.place(x=15, y=5, w=210, h=200)
        u_db_label7=tk.Label(u_db_button7,text=f"Name: {items_lst[6][0]}\n   Price: Rs.{price_lst[6][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label7.place(relx=0.15,rely=0.6)

    #button 8 in scrollable frame
        u_db_button8=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button8.grid(row=1,column=3,padx=0,pady=0)
        u_db_btn11=CTkButton(u_db_button8,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit8)
        u_db_btn11.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 8
        u_db_img10=Image.open("pictures/pngegg (14) 1coke.png")
        u_db_img10=u_db_img10.resize((160,160))
        photo_u_db_img10tk=ImageTk.PhotoImage(u_db_img10)
        u_db_img10_lbl = tk.Label(u_db_button8, image=photo_u_db_img10tk,bg="#D9D9D9")
        u_db_img10_lbl.place(x=40, y=17, w=160, h=160)
        u_db_label8=tk.Label(u_db_button8,text=f"Name: {items_lst[7][0]}\n   Price: Rs.{price_lst[7][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label8.place(relx=0.18,rely=0.6)

    #button 9 in scrollable frame
        u_db_button9=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button9.grid(row=2,column=0,padx=20,pady=20)
        u_db_btn12=CTkButton(u_db_button9,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit9)
        u_db_btn12.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 9
        u_db_img11=Image.open("pictures/pngegg (13) 1oreo_shake.png")
        u_db_img11=u_db_img11.resize((180,160))
        photo_u_db_img11tk=ImageTk.PhotoImage(u_db_img11)
        u_db_img11_lbl = tk.Label(u_db_button9, image=photo_u_db_img11tk,bg="#D9D9D9")
        u_db_img11_lbl.place(x=40, y=15, w=180, h=160)
        u_db_label9=tk.Label(u_db_button9,text=f"Name: {items_lst[8][0]}\n   Price: Rs.{price_lst[8][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label9.place(relx=0.15,rely=0.6)

    #button 10 in scrollable frame
        u_db_button10=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button10.grid(row=2,column=1,padx=0,pady=20)
        u_db_btn13=CTkButton(u_db_button10,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit11)
        u_db_btn13.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 10
        u_db_img12=Image.open("pictures/pngegg (11) 1cofee.png")
        u_db_img12=u_db_img12.resize((200,200))
        photo_u_db_img12tk=ImageTk.PhotoImage(u_db_img12)
        u_db_img12_lbl = tk.Label(u_db_button10, image=photo_u_db_img12tk,bg="#D9D9D9")
        u_db_img12_lbl.place(x=25, y=5, w=200, h=200)
        u_db_label10=tk.Label(u_db_button10,text=f"Name: {items_lst[9][0]}\n   Price: Rs.{price_lst[9][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label10.place(relx=0.15,rely=0.6)
        
    #button 11 in scrollable frame
        u_db_button11=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button11.grid(row=2,column=2,padx=20,pady=20)
        u_db_btn14=CTkButton(u_db_button11,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit12)
        u_db_btn14.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 11
        u_db_img15=Image.open("pictures/pngegg (2) 2momo.png")
        u_db_img15=u_db_img15.resize((190,190))
        photo_u_db_img15tk=ImageTk.PhotoImage(u_db_img15)
        u_db_img15_lbl = tk.Label(u_db_button11, image=photo_u_db_img15tk,bg="#D9D9D9")
        u_db_img15_lbl.place(x=30, y=8, w=190, h=190)
        u_db_label11=tk.Label(u_db_button11,text=f"Name: {items_lst[10][0]}\n   Price: Rs.{price_lst[10][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label11.place(relx=0.1,rely=0.6)

    #button 12 in scrollable frame
        u_db_button12=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button12.grid(row=2,column=3,padx=0,pady=20)
        u_db_btn15=CTkButton(u_db_button12,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit13)
        u_db_btn15.place(rely=0.8,relx=0.15,relheight=0.15)
        u_db_label12=tk.Label(u_db_button12,text=f"    Name: {items_lst[11][0]}\n   Price: Rs.{price_lst[11][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label12.place(relx=0.15,rely=0.6)

    #image and label for button 12
        u_db_img13=Image.open("pictures/pngegg (15) 1sprite.png")
        u_db_img13=u_db_img13.resize((140,160))
        photo_u_db_img13tk=ImageTk.PhotoImage(u_db_img13)
        u_db_img13_lbl = tk.Label(u_db_button12, image=photo_u_db_img13tk,bg="#D9D9D9")
        u_db_img13_lbl.place(x=55, y=20, w=140, h=160)

    #button 13 in scrollable frame
        u_db_button13=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button13.grid(row=3,column=0,padx=20,pady=0)
        u_db_btn16=CTkButton(u_db_button13,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit10)
        u_db_btn16.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 13
        u_db_img14=Image.open("pictures/pngegg (16) 1fanta.png")
        u_db_img14=u_db_img14.resize((160,160))
        photo_u_db_img14tk=ImageTk.PhotoImage(u_db_img14)
        u_db_img14_lbl = tk.Label(u_db_button13, image=photo_u_db_img14tk,bg="#D9D9D9")
        u_db_img14_lbl.place(x=45, y=15, w=160, h=160)
        u_db_label13=tk.Label(u_db_button13,text=f"   Name: {items_lst[12][0]}\n   Price: Rs.{price_lst[12][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label13.place(relx=0.15,rely=0.6)

    #button 14 in scrollable frame
        u_db_button14=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button14.grid(row=3,column=1,padx=0,pady=0)
        u_db_btn17=CTkButton(u_db_button14,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit14)
        u_db_btn17.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 14
        u_db_img16=Image.open("pictures/pngegg (3) 2chowmein.png")
        u_db_img16=u_db_img16.resize((200,200))
        photo_u_db_img16tk=ImageTk.PhotoImage(u_db_img16)
        u_db_img16_lbl = tk.Label(u_db_button14, image=photo_u_db_img16tk,bg="#D9D9D9")
        u_db_img16_lbl.place(x=25, y=5, w=200, h=200)
        u_db_label14=tk.Label(u_db_button14,text=f"Name: {items_lst[13][0]}\n   Price: Rs.{price_lst[0][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label14.place(relx=0.04,rely=0.6)

    #button 15 in scrollable frame
        u_db_button15=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button15.grid(row=3,column=2,padx=20,pady=0)
        u_db_btn18=CTkButton(u_db_button15,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=a_db_edit15)
        u_db_btn18.place(rely=0.8,relx=0.15,relheight=0.15)
    #image and label for button 15 
        u_db_img17=Image.open("pictures/pngegg (4) 2Biryani.png")
        u_db_img17=u_db_img17.resize((235,180))
        photo_u_db_img17tk=ImageTk.PhotoImage(u_db_img17)
        u_db_img17_lbl = tk.Label(u_db_button15, image=photo_u_db_img17tk,bg="#D9D9D9")
        u_db_img17_lbl.place(x=10, y=5, w=235, h=180)
        u_db_label15=tk.Label(u_db_button15,text=f"Name: {items_lst[14][0]}\n   Price: Rs.{price_lst[14][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label15.place(relx=0.1,rely=0.6)

        




        #-----------------------------------------------customize_customers frame---------------------------------------------------#






    def customers_frame_ad():
        '''this function is made to make frame in dashboard swap with the frame in customers page and make other buttons hover as usual'''
        
        global s_f_frame,admin_db_customer_frame
        #customers frame
        admin_db_customer_frame.place(relx=0.302,rely=0.12,relwidth=0.7,relheight=0.9)

        #forgetting items frame
        s_f_frame.place_forget()
        #forgetting dashboard frame
        admin_db_frame3.place_forget()

        #this is to configure dashboard labels text to customers
        a_db_btn9.configure(text="             Customers")

    #making image global
        global admin_db_btn3,admin_db_btn3_lbl,admin_db_btn2,admin_db_btn4
        #forgetting the original customers button to replace it with new button 
        admin_db_btn4.place_forget()

    #customers button
        admin_db_btn4_customer=CTkButton(admin_db_frame2,fg_color="#F38686",text="Customers",text_color="#33303C",image=a_db_img7ctk,corner_radius=7 ,hover=0, command = customers_frame_ad)
        admin_db_btn4_customer.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

    #dashboard button
        admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
        admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

    #Item button
        admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
        admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
        admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
        admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

        #Customer Frame

        #bindings so that that buttons act as intended
        admin_db_btn2.bind("<Enter>", on_hover)
        admin_db_btn2.bind("<Leave>", off_hover)

        admin_db_btn3.bind("<Enter>", on_hover2)
        admin_db_btn3.bind("<Leave>", off_hover2)
    

       #--------------end of frames-------------------#
        def load_users():
            cursor = conn.cursor()
            cursor.execute("SELECT first_name, last_name, email, password FROM user")
            users = cursor.fetchall()
            tree.delete(*tree.get_children())
            for user in users:
                tree.insert("", tk.END, values=user)
        
        def search_users(field):
            search_term = globals()[f"{field}_entry"].get()
            cursor = conn.cursor()
            cursor.execute(f"SELECT first_name, last_name, email, password FROM user WHERE {field} LIKE ?", (f"%{search_term}%",))
            users = cursor.fetchall()
            tree.delete(*tree.get_children())
            for user in users:
                tree.insert("", tk.END, values=user)
        
        def clear_search():
            first_name_entry.delete(0, tk.END)
            last_name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            load_users()
        
        def update_user():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("Warning", "Please select a user to update.")
                return
            user = tree.item(selected_item)['values']
            update_window = CTkToplevel(admin_db_customer_frame)
            update_window.title("Update User")
            update_window.geometry("500x400")
            update_window.resizable(0,0)
        
            CTkLabel(update_window, text="First Name:").pack()
            new_first_name = CTkEntry(update_window)
            new_first_name.insert(0, user[0])
            new_first_name.pack()
        
            CTkLabel(update_window, text="Last Name:").pack()
            new_last_name = CTkEntry(update_window)
            new_last_name.insert(0, user[1])
            new_last_name.pack()
        
            CTkLabel(update_window, text="Email:").pack()
            new_email = CTkEntry(update_window)
            new_email.insert(0, user[2])
            new_email.pack()
        
            CTkLabel(update_window, text="Password:").pack()
            new_password = CTkEntry(update_window, show="*")
            new_password.insert(0, user[3])
            new_password.pack()
        
            def save_changes():
                cursor = conn.cursor()
                cursor.execute("UPDATE user SET first_name=?, last_name=?, email=?, password=? WHERE email=?",
                            (new_first_name.get(), new_last_name.get(), new_email.get(), new_password.get(), user[2]))
                conn.commit()
                update_window.destroy()
                load_users()
        
            CTkButton(update_window, text="Save Changes", command=save_changes).pack(pady=10)
        
        def delete_user():
            selected_item = tree.selection()
            if not selected_item:
                tk.messagebox.showwarning("Warning", "Please select a user to delete.")
                return
            user = tree.item(selected_item)['values']
            if tk.messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the user {user[2]}?"):
                cursor = conn.cursor()
                cursor.execute("DELETE FROM user WHERE email=?", (user[2],))
                conn.commit()
                load_users()
        
        def show_all_data():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user")
            users = cursor.fetchall()
            all_data_window = CTkToplevel(admin_db_customer_frame)
            all_data_window.title("All User Data")
            all_data_window.geometry("800x600+0+0")
            all_data_tree = ttk.Treeview(all_data_window)
            all_data_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            # Get column names from the cursor description
            columns = [description[0] for description in cursor.description]
            all_data_tree["columns"] = columns
            all_data_tree["show"] = "headings"
            for col in columns:
                all_data_tree.heading(col, text=col.capitalize())
                all_data_tree.column(col, width=100)
            for user in users:
                all_data_tree.insert("", tk.END, values=user)
        
        global first_name_entry,last_name_entry,email_entry
        # Create main frame
        customize_user_mf = CTkFrame(admin_db_customer_frame,width=850,height=680,fg_color="#33303C")
        customize_user_mf.pack( padx=20,pady=5)
        customize_user_mf.pack_propagate(False)
        
        # Search section
        search_frame = CTkFrame(customize_user_mf,fg_color="#D9D9D9")
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        CTkLabel(search_frame, text="SEARCH BY:-",text_color="black").pack()
        
        # First Name
        first_name_frame = CTkFrame(search_frame,fg_color="#D9D9D9")
        first_name_frame.pack(fill=tk.X, pady=5)
        CTkLabel(first_name_frame, text="FirstName:",text_color="black").pack(side=tk.LEFT)
        first_name_entry = CTkEntry(first_name_frame, placeholder_text="FirstName",fg_color="white",text_color="#33303C",placeholder_text_color="#33303C")
        first_name_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        CTkButton(first_name_frame, text="SEARCH",fg_color="#33303C", command=lambda: search_users("first_name")).pack(side=tk.RIGHT)
        
        # Last Name
        last_name_frame = CTkFrame(search_frame,fg_color="#D9D9D9")
        last_name_frame.pack(fill=tk.X, pady=5)
        CTkLabel(last_name_frame, text="LastName:",text_color="black").pack(side=tk.LEFT)
        last_name_entry = CTkEntry(last_name_frame, placeholder_text="LastName",fg_color="white",text_color="#33303C",placeholder_text_color="#33303C")
        last_name_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        CTkButton(last_name_frame, text="SEARCH",fg_color="#33303C", command=lambda: search_users("last_name")).pack(side=tk.RIGHT)
        
        # Email
        email_frame = CTkFrame(search_frame,fg_color="#D9D9D9")
        email_frame.pack(fill=tk.X, pady=5)
        CTkLabel(email_frame, text="Email:",text_color="black").pack(side=tk.LEFT)
        email_entry = CTkEntry(email_frame, placeholder_text="example@gmail.com",text_color="#33303C",placeholder_text_color="#33303C",width=622,fg_color="white")
        email_entry.pack(side=tk.LEFT, padx=(27, 5))
        CTkButton(email_frame, text="SEARCH",fg_color="#33303C", command=lambda: search_users("email")).pack(side=tk.RIGHT)
        
        # Clear and All Data buttons
        button_frame = CTkFrame(search_frame,fg_color="#D9D9D9")
        button_frame.pack(fill=tk.X, pady=10)
        CTkButton(button_frame, text="CLEAR",fg_color="#33303C",command=clear_search).pack(side=tk.LEFT, expand=True, padx=5)
        CTkButton(button_frame, text="ALL DATA",fg_color="#33303C", command=show_all_data).pack(side=tk.LEFT, expand=True, padx=5)
        
        # Treeview
        tree = ttk.Treeview(customize_user_mf, columns=("FirstName", "LastName", "Email", "Password"), show="headings")
        tree.heading("FirstName", text="First Name")
        tree.heading("LastName", text="Last Name")
        tree.heading("Email", text="Email")
        tree.heading("Password", text="Password")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons frame
        button_frame = CTkFrame(customize_user_mf,fg_color="#33303C")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        CTkButton(button_frame, text="UPDATE",fg_color="#D9D9D9",text_color="#33303C",hover_color="#F38686", command=update_user).pack(side=tk.LEFT, expand=True, padx=5)
        CTkButton(button_frame, text="DELETE",fg_color="#D9D9D9",text_color="#33303C",hover_color="#F38686", command=delete_user).pack(side=tk.LEFT, expand=True, padx=5)
        CTkButton(button_frame, text="EXIT",fg_color="#D9D9D9",text_color="#33303C",hover_color="#F38686", command=root.quit).pack(side=tk.LEFT, expand=True, padx=5)
        
        # Initialize database and load users
        conn = sqlite3.connect("mealmate.db")
        load_users()





    #top frame that contains logo,item name entrybox and other widgets
    admin_db_frame1=tk.Frame(main_frame6,bg="#D9D9D9")
    admin_db_frame1.place(relwidth=1,relheight=0.11,x=0,y=0)


    # the logo
    a_db_logo=Image.open("pictures/Rectangle 41.png")
    a_db_logo=a_db_logo.resize((468,97))
    photo_a_db_logo=ImageTk.PhotoImage(a_db_logo)
    #label that contains image
    a_db_lbl = tk.Label(admin_db_frame1, image=photo_a_db_logo,bg="#D9D9D9")
    a_db_lbl.place(x=20, y=6, w=468, h=97)

    #frame that has menubutton
    admin_db_frame4=CTkFrame(admin_db_frame1,corner_radius=10,fg_color="#33303C")
    admin_db_frame4.place(relx=0.4,rely=0.3,relwidth=0.5,relheight=0.4)

    #Button used as a container to display text
    a_db_btn7=CTkButton(admin_db_frame4,text="          Admin",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
    a_db_btn7.place(relx=0.1,rely=0.1,relwidth=0.17)
    a_db_lbl3=tk.Label(a_db_btn7,text="User:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
    a_db_lbl3.place(relx=0.15,rely=0.05)

    #Button used as a container to display text
    a_db_btn8=CTkButton(admin_db_frame4,text=f"          {admin_data[0][0]}",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
    a_db_btn8.place(relx=0.4,rely=0.1,relwidth=0.18)
    a_db_lbl4=tk.Label(a_db_btn8,text="Name:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
    a_db_lbl4.place(relx=0.15,rely=0.05)

    #Button used as a container to display label 
    a_db_btn9=CTkButton(admin_db_frame4,text="             Dashboard",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
    a_db_btn9.place(relx=0.7,rely=0.1,relwidth=0.2)
    a_db_lbl5=tk.Label(a_db_btn9,text="Page:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
    a_db_lbl5.place(relx=0.12,rely=0.05)

#the frame that consists all the management system heading and dashboard, exit, logout,customers and items button
    admin_db_frame2=CTkFrame(main_frame6,corner_radius=10,fg_color="#33303C")
    admin_db_frame2.place(relheight=0.879,relwidth=0.3,relx=0,rely=0.12)


    #separator frame
    adb_sep_frame=tk.Frame(admin_db_frame2,bg="Black")
    adb_sep_frame.place(relwidth=1,relheight=0.01,relx=0,rely=0.1)

    #managenment system heading
    admin_db_btn=CTkButton(admin_db_frame2,fg_color="#33303C",text="Management System",font=("Regular",23),height=45,hover=0,border_color="#D9D9D9",corner_radius=0,border_width=1)
    admin_db_btn.place(relx=0.21,rely=0.017,relwidth=0.56)


    #images in dashboard button
    a_db_img1=Image.open("pictures/Group 34group_home2.png")
    a_db_img1ctk=CTkImage(a_db_img1)
    a_db_img5=Image.open("pictures/Group 33grouped_home1.png")
    a_db_img5ctk=CTkImage(a_db_img5)

    #images in items button
    a_db_img2=Image.open("pictures/Vectoriconns-1.png")
    a_db_img2ctk=CTkImage(a_db_img2)
    a_db_img6=Image.open("pictures/Vectoriconns-5.png")
    a_db_img6ctk=CTkImage(a_db_img6)

    #images in customers button
    a_db_img3=Image.open("pictures/Vectoriconns.png")
    a_db_img3ctk=CTkImage(a_db_img3)
    a_db_img7=Image.open("pictures/Vectoriconns-4.png")
    a_db_img7ctk=CTkImage(a_db_img7)

    #images in exit button
    a_db_img4=Image.open("pictures/Groupiconns.png")
    a_db_img4ctk=CTkImage(a_db_img4)
    a_db_img8=Image.open("pictures/Groupiconns-1.png")
    a_db_img8ctk=CTkImage(a_db_img8)

    #the arrow pic in back button
    a_db_img9=Image.open("pictures//Vectorarrow.png")
    a_db_img9tk=ImageTk.PhotoImage(a_db_img9)


    #Dashboard Button
    admin_db_btn2=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Dashboard",image=a_db_img1ctk,text_color="#DD2323",corner_radius=7, command = dashboard_frame_ad)
    admin_db_btn2.place(relx=0.21,rely=0.25,relwidth=0.56,relheight=0.06)

    #Items Button
    admin_db_btn3=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Items",text_color="#DD2323",corner_radius=7,command = items_frame_ad)
    admin_db_btn3.place(relx=0.21,rely=0.4,relwidth=0.56,relheight=0.06)
    admin_db_btn3_lbl=CTkLabel(admin_db_btn3,image=a_db_img2ctk,text="")
    admin_db_btn3_lbl.place(relx=0.3,rely=0.1)

    #Customers Button
    admin_db_btn4=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Customers",text_color="#DD2323",image=a_db_img3ctk,corner_radius=7 , command = customers_frame_ad)
    admin_db_btn4.place(relx=0.21,rely=0.55,relwidth=0.56,relheight=0.06)

    #Exit Button Button
    admin_db_btn5=CTkButton(admin_db_frame2,fg_color="#D9D9D9",text="Exit",text_color="#DD2323",image=a_db_img4ctk,corner_radius=7,command=a_db_exit)
    admin_db_btn5.place(relx=0.21,rely=0.7,relwidth=0.56,relheight=0.06)

    admin_db_btn6=tk.Button(admin_db_frame2,text=" Log out",font=("Regular",15),image=a_db_img9tk,compound=LEFT,bg="#33303C",activebackground="#33303C",activeforeground="White",fg="White",bd=0,command=go_to_dash)
    admin_db_btn6.place(relx=0.39,rely=0.85)


    #binding events in buttons
    admin_db_btn2.bind("<Enter>", on_hover)
    admin_db_btn2.bind("<Leave>", off_hover)

    admin_db_btn3.bind("<Enter>", on_hover2)
    admin_db_btn3.bind("<Leave>", off_hover2)

    admin_db_btn4.bind("<Enter>", on_hover3)
    admin_db_btn4.bind("<Leave>", off_hover3)

    admin_db_btn5.bind("<Enter>", on_hover4)
    admin_db_btn5.bind("<Leave>", off_hover4)


    dashboard_frame_ad()







#----------------------------------------------------user items dashboard-------------------------------------------------------#







def user_dashboard():
    '''This function opens the user dashboard page when called.'''

    u_db_mainframe=CTkFrame(root,fg_color="black")
    u_db_mainframe.place(relwidth=1,relheight=1,x=0,y=0)
    global photo_u_db_logo

    #----------------foood menu-------------------#

    def foods():
        """this function is made so that when foods menu in menubutton is clicked,the buttons that dont contain foods are forgotten
        and the buttons that contains foods are displayed in correct order"""

        u_db_menubutton.config(text="Foods  ▼")
        u_db_button3.grid_forget()
        u_db_button4.grid_forget()
        u_db_button6.grid_forget()
        u_db_button8.grid_forget()
        u_db_button9.grid_forget()
        u_db_button10.grid_forget()
        u_db_button12.grid_forget()
        u_db_button13.grid_forget()


        u_db_button1.grid(row=0,column=0,padx=10,pady=10)
        u_db_button2.grid(row=0,column=2,padx=0,pady=0)
        u_db_button5.grid(row=1,column=1,rowspan=1,padx=10,pady=10)
        u_db_button7.grid(row=2,column=0,rowspan=1,padx=0,pady=10)
        u_db_button11.grid(row=0,column=1,rowspan=1,padx=10,pady=10)
        u_db_button14.grid(row=1,column=0,rowspan=1,padx=0,pady=0)
        u_db_button15.grid(row=1,column=2,rowspan=1,padx=10,pady=10)

        

        #-----------------------drinks menu--------------------------#



    def drinks():
        """this function is made so that when drinks menu in menubutton is clicked,the buttons that dont contain drinks are forgotten
        and the buttons that contains drinks are displayed in correct order"""

        u_db_menubutton.config(text="Drinks  ▼")
        u_db_button1.grid_forget()
        u_db_button2.grid_forget()
        u_db_button5.grid_forget()
        u_db_button7.grid_forget()
        u_db_button11.grid_forget()
        u_db_button14.grid_forget()
        u_db_button15.grid_forget()

        u_db_button3.grid(row=0,column=0,padx=10,pady=10)
        u_db_button4.grid(row=0,column=1,padx=0,pady=0)
        u_db_button6.grid(row=0,column=2,padx=10,pady=10)
        u_db_button8.grid(row=1,column=0,padx=0,pady=0)
        u_db_button9.grid(row=1,column=1,padx=10,pady=10)
        u_db_button10.grid(row=1,column=2,padx=0,pady=0)
        u_db_button12.grid(row=2,column=0,padx=10,pady=10)
        u_db_button13.grid(row=2,column=1,padx=0,pady=0)





    def logout_but():
        """this function is made to ask a yesno question when button is clicked and open dashboard page when yes is clicked."""
        user_logout=tk.messagebox.askyesno("Logout?","Are you sure you want to log out?")
        if user_logout==1:
            u_db_mainframe.place_forget()
            main()

    def custom_confirm():
        """this function is created to reopen the admin dashboard"""
        customize_main_frame.place_forget()
            



    def exit_but():
        exit_reply=tk.messagebox.askyesno("Exit?","Are you sure you want to exit ?")
        if exit_reply==1:
            root.destroy()


#----------------------------------------------------------------------------------------------------------------------#
    global total_price,name_lst
    total_price=0
    name_lst=[]
    def user_proceed_1():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[0][0]}                     Rs.{price_lst[0][0]}                       x{count+1}                           Rs.{(price_lst[0][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[0][0]
    def user_proceed_2():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[1][0]}                               Rs.{price_lst[1][0]}                       x{count+1}                           Rs.{(price_lst[1][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[1][0]
    def user_proceed_3():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[2][0]}                        Rs.{price_lst[2][0]}                       x{count+1}                           Rs.{(price_lst[2][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[2][0]
    def user_proceed_4():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[3][0]}                                     Rs.{price_lst[3][0]}                         x{count+1}                           Rs.{(price_lst[3][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[3][0]
    def user_proceed_5():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[4][0]}                              Rs.{price_lst[4][0]}                       x{count+1}                           Rs.{(price_lst[4][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[4][0]
    def user_proceed_6():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[5][0]}                           Rs.{price_lst[5][0]}                        x{count+1}                           Rs.{(price_lst[5][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[5][0]
    def user_proceed_7():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[6][0]}                          Rs.{price_lst[6][0]}                        x{count+1}                           Rs.{(price_lst[6][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[6][0]
    def user_proceed_8():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[7][0]}                               Rs.{price_lst[7][0]}                         x{count+1}                           Rs.{(price_lst[7][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[7][0]
    def user_proceed_9():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[8][0]}                            Rs.{price_lst[8][0]}                       x{count+1}                           Rs.{(price_lst[8][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[8][0]
    def user_proceed_10():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[9][0]}                            Rs.{price_lst[9][0]}                       x{count+1}                           Rs.{(price_lst[9][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[9][0]
    def user_proceed_11():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[10][0]}                       Rs.{price_lst[10][0]}                       x{count+1}                           Rs.{(price_lst[10][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[10][0]
    def user_proceed_12():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[11][0]}                                    Rs.{price_lst[11][0]}                         x{count+1}                           Rs.{(price_lst[11][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[11][0]
    def user_proceed_13():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[12][0]}                                     Rs.{price_lst[12][0]}                         x{count+1}                           Rs.{(price_lst[12][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[12][0]
    def user_proceed_14():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[13][0]}                Rs.{price_lst[13][0]}                       x{count+1}                           Rs.{(price_lst[13][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[13][0]
    def user_proceed_15():
        global total_price
        count = 0
        menu_lbl1 = tk.Label(u_db_frame4,text = f"           {items_lst[14][0]}                     Rs.{price_lst[14][0]}                       x{count+1}                           Rs.{(price_lst[14][0])*(count+1)}", font = ('Inter', 15, 'bold'),bg="#D9D9D9")
        menu_lbl1.pack(anchor = NW,pady=10)
        total_price += price_lst[14][0]


#------------------------------------------------------------------------------------------------------------------------------------#





    #-------------------------------------------user customization profile---------------------------------------------------#





    def customize():
        """this function is made to create a top label window when customize profile button is cliclked """

        global customize_win, user_data

        #-------------------------------------------database----------------------------------------#
        #fetching logged in user data from the mealmate database
        conn = sqlite3.connect('mealmate.db')
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE email =? and password = ?", (u_email,u_password))
        user_data = c.fetchall()
        #-------------------------------------------------------------------------------------------#
        
        global customize_main_frame
        customize_main_frame=tk.Frame(root,bg="white")
        customize_main_frame.place(relheight=1,relwidth=1,relx=0,rely=0)


        global customize_entry1, customize_entry2
    #frame
        customize_frame1=tk.Frame(customize_main_frame,width=712,height=960,bg="white")
        customize_frame1.place(x=0,y=0)
    #frame
        customize_frame3=CTkFrame(customize_frame1,corner_radius=18,fg_color="#D9D9D9")
        customize_frame3.place(relx=0.1,rely=0.15,relwidth=0.9,relheight=0.7)

    #user profile label
        customize_lbl2=tk.Label(customize_frame3,text="USER PROFILE",font=("Inter",26,"bold"),fg="#5B6E80",bg="#D9D9D9")
        customize_lbl2.place(relx=0.31,rely=0.02)

    #firstname label
        customize_lbl3=tk.Label(customize_frame3,text="FirstName:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
        customize_lbl3.place(relx=0.07,rely=0.1)
    #firstname entrybox
        customize_entry1=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text=user_data[0][0],placeholder_text_color="#97D5C9")
        customize_entry1.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.15)
        customize_entry1.configure(state="disabled")

    #lastname label
        customize_lbl4=tk.Label(customize_frame3,text="LastName:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
        customize_lbl4.place(relx=0.07,rely=0.23)
    #lastname entrybox
        customize_entry2=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text=user_data[0][1],placeholder_text_color="#97D5C9")
        customize_entry2.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.28)
        customize_entry2.configure(state="disabled")
    #Email label
        customize_lbl5=tk.Label(customize_frame3,text="Email:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
        customize_lbl5.place(relx=0.07,rely=0.36)
    #Email frame
        customize_email_frame=CTkFrame(customize_frame3,corner_radius=12,border_width=2,border_color="#5B6E80",fg_color="white")
        customize_email_frame.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.41)
        customize_email_label=tk.Label(customize_email_frame,fg="#97D5C9",bg="white",font=("Inter",17),text=user_data[0][2])
        customize_email_label.place(relx=0.03,rely=0.18)

    #eyebutton
        customize_eye_img1=Image.open("pictures/ion_eyegrey_eye.png")
        customize_eye_img1tk=ImageTk.PhotoImage(customize_eye_img1)
        
        #password entry
        customize_lbl6=tk.Label(customize_frame3,text="Password:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
        customize_lbl6.place(relx=0.07,rely=0.49)
        #password frame
        customize_pass_frame=CTkFrame(customize_frame3,corner_radius=12,border_width=2,border_color="#5B6E80",fg_color="white")
        customize_pass_frame.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.54)
        customize_pass_label=tk.Label(customize_pass_frame,fg="#97D5C9",bg="white",font=("Inter",17),text=user_data[0][3])
        customize_pass_label.place(relx=0.03,rely=0.18)


    #confirm button
        customize_button=CTkButton(customize_frame3,text="CONFIRM",font=("Inter",15,"bold"),fg_color="#97D5C9",text_color="#5B6E80",command=custom_confirm)
        customize_button.place(relx=0.35,rely=0.8,relheight=0.08)

    #frame
        customize_frame2=tk.Frame(customize_main_frame,width=700,height=1080,bg="white")
        customize_frame2.place(x=1000,y=0)

    #backgriund pic in admin dashboard
        customize_img=Image.open("pictures/Rectangle 79pic.png")
        customize_img=customize_img.resize((675,970))
        photo_customize_imgtk=ImageTk.PhotoImage(customize_img)
        customize_lbl = tk.Label(customize_frame2, image=photo_customize_imgtk,bg="#D9D9D9")
        customize_lbl.image = photo_customize_imgtk 
        customize_lbl.place(x=0, y=0,w=675,h=970)





    #the top frame 
    u_db_frame1=tk.Frame(u_db_mainframe,bg="#ACACAC")
    u_db_frame1.place(relwidth=1,relheight=0.12,relx=0,rely=0)


    #logo
    u_db_logo=Image.open("pictures\\Rectangle 41.png")
    u_db_logo=u_db_logo.resize((508,105))
    photo_u_db_logo=ImageTk.PhotoImage(u_db_logo)


    #logo
    u_db_lbl1=tk.Label(u_db_frame1,image=photo_u_db_logo,bg="#ACACAC")
    u_db_lbl1.place(relx=0.01,rely=0.04)

    #frame for menubutton
    u_db_menubtn=CTkFrame(u_db_frame1,fg_color="white",border_width=1,border_color="black",corner_radius=8)
    u_db_menubtn.place(relwidth=0.15,relheight=0.45,relx=0.43,rely=0.3)


    # details_menu main frame
    u_db_frame=CTkFrame(u_db_mainframe,corner_radius=7,fg_color="black")
    u_db_frame.place(relwidth=0.45,relheight=0.85,relx=0.5,rely=0.15)



    #exit button
    u_db_btn4=CTkButton(u_db_frame1,text="EXIT",fg_color="Black",text_color="white",hover=0,font=("Inter",12,"bold"),command=exit_but)
    u_db_btn4.place(relwidth=0.05,relheight=0.45,relx=0.92,rely=0.3)


    #customize profile button
    u_db_btn2=CTkButton(u_db_frame1,text="USER DETAILS",fg_color="Black",text_color="white",hover=0,font=("Inter",12,"bold"),command=customize)
    u_db_btn2.place(relwidth=0.1,relheight=0.45,relx=0.74,rely=0.3)

    #logout button
    u_db_btn3=CTkButton(u_db_frame1,text="LOGOUT",fg_color="Black",text_color="white",hover=0,font=("Inter",12,"bold"),command=logout_but)
    u_db_btn3.place(relwidth=0.06,relheight=0.45,relx=0.85,rely=0.3)


    #------------------------------------item's main menu-----------------------------------------#


    def main_menu():
        """this function contains the scrollable frame which contains all the buttons with items and images."""
        u_db_menubutton.config(text="All Items  ▼")
        #making images global 
        global photo_u_db_img3tk,photo_u_db_img4tk,photo_u_db_img5tk,photo_u_db_img6tk,photo_u_db_img7tk,photo_u_db_img8tk,photo_u_db_img9tk,photo_u_db_img10tk,photo_u_db_img11tk,photo_u_db_img12tk,photo_u_db_img13tk,photo_u_db_img14tk,photo_u_db_img15tk,photo_u_db_img16tk,photo_u_db_img17tk
        global u_db_button1,u_db_button2,u_db_button3,u_db_button4,u_db_button5,u_db_button6,u_db_button7,u_db_button8,u_db_button9,u_db_button10,u_db_button11,u_db_button12,u_db_button13,u_db_button14,u_db_button15

        #Scrollable frame that contains all items
        u_db_sframe=CTkScrollableFrame(u_db_mainframe,corner_radius=0,fg_color="Black",scrollbar_button_color="white",scrollbar_button_hover_color="#D9D9D9")
        u_db_sframe.place(relwidth=0.45,relheight=0.85,relx=0.005,rely=0.13)

    #button 1 in scrollable frame
        u_db_button1=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button1.grid(row=0,column=0,padx=20,pady=20)
        u_db_btn4=CTkButton(u_db_button1,text="PROCEED",font=("Inter",18,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_1)
        u_db_btn4.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 1
        u_db_img3=Image.open("pictures/pngegg (2) 1Bargar.png")
        u_db_img3=u_db_img3.resize((230,210))
        photo_u_db_img3tk=ImageTk.PhotoImage(u_db_img3)
        u_db_img3_lbl = tk.Label(u_db_button1, image=photo_u_db_img3tk,bg="#D9D9D9")
        u_db_img3_lbl.place(x=15, y=5, w=230, h=210)
        u_db_label1=tk.Label(u_db_button1,text=f"Name: {items_lst[0][0]}\n  Price: Rs.{price_lst[0][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label1.place(relx=0.1,rely=0.6)

    #button 2 in scrollable frame
        u_db_button2=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button2.grid(row=0,column=2,padx=20,pady=20)
        u_db_btn5=CTkButton(u_db_button2,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_3)
        u_db_btn5.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 2
        u_db_img4=Image.open("pictures/pngegg (6) 1pizza.png")
        u_db_img4=u_db_img4.resize((220,200))
        photo_u_db_img4tk=ImageTk.PhotoImage(u_db_img4)
        u_db_img4_lbl = tk.Label(u_db_button2, image=photo_u_db_img4tk,bg="#D9D9D9")
        u_db_img4_lbl.place(x=15, y=5, w=220, h=200)
        u_db_label2=tk.Label(u_db_button2,text=f"Name: {items_lst[2][0]}\n  Price: {price_lst[2][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label2.place(relx=0.1,rely=0.6)

    #button 3 in scrollable frame
        u_db_button3=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button3.grid(row=0,column=1,padx=0,pady=0)
        u_db_btn6=CTkButton(u_db_button3,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_2)
        u_db_btn6.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 3
        u_db_img5=Image.open("pictures/pngegg (8) 1cooooofe.png")
        u_db_img5=u_db_img5.resize((210,190))
        photo_u_db_img5tk=ImageTk.PhotoImage(u_db_img5)
        u_db_img5_lbl = tk.Label(u_db_button3, image=photo_u_db_img5tk,bg="#D9D9D9")
        u_db_img5_lbl.place(x=10, y=5, w=210, h=190)
        u_db_label3=tk.Label(u_db_button3,text=f"Name: {items_lst[1][0]}\n   Price: Rs.{price_lst[1][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label3.place(relx=0.17,rely=0.6)

    #button 4 in scrollable frame
        u_db_button4=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button4.grid(row=1,column=0,rowspan=1,padx=20,pady=0)
        u_db_btn7=CTkButton(u_db_button4,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_4)
        u_db_btn7.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 4
        u_db_img6=Image.open("pictures/pngegg (4) 1pepsii.png")
        u_db_img6=u_db_img6.resize((160,160))
        photo_u_db_img6tk=ImageTk.PhotoImage(u_db_img6)
        u_db_img6_lbl = tk.Label(u_db_button4, image=photo_u_db_img6tk,bg="#D9D9D9")
        u_db_img6_lbl.place(x=45, y=15, w=160, h=160)
        u_db_label4=tk.Label(u_db_button4,text=f"   Name:{items_lst[3][0]}\n   Price: Rs.{price_lst[3][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label4.place(relx=0.16,rely=0.6)

    #button 5 in scrollable frame
        u_db_button5=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button5.grid(row=1,column=1,rowspan=1,padx=0,pady=0)
        u_db_btn8=CTkButton(u_db_button5,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_5)
        u_db_btn8.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 5
        u_db_img7=Image.open("pictures/pngegg (7) 1fried_chicken.png")
        u_db_img7=u_db_img7.resize((210,190))
        photo_u_db_img7tk=ImageTk.PhotoImage(u_db_img7)
        u_db_img7_lbl = tk.Label(u_db_button5, image=photo_u_db_img7tk,bg="#D9D9D9")
        u_db_img7_lbl.place(x=25, y=4, w=210, h=190)
        u_db_label5=tk.Label(u_db_button5,text=f"Name: {items_lst[4][0]}\n   Price: Rs.{price_lst[4][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label5.place(relx=0.17,rely=0.6)

    #button 6 in scrollable frame
        u_db_button6=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button6.grid(row=1,column=2,rowspan=1,padx=20,pady=0)
        u_db_btn9=CTkButton(u_db_button6,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_6)
        u_db_btn9.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 6
        u_db_img8=Image.open("pictures/pngegg (12) 1coffee_shake.png")
        u_db_img8=u_db_img8.resize((190,170))
        photo_u_db_img8tk=ImageTk.PhotoImage(u_db_img8)
        u_db_img8_lbl = tk.Label(u_db_button6, image=photo_u_db_img8tk,bg="#D9D9D9")
        u_db_img8_lbl.place(x=25, y=12, w=190, h=170)
        u_db_label6=tk.Label(u_db_button6,text=f"Name: {items_lst[5][0]}\n    Price: Rs.{price_lst[5][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label6.place(relx=0.15,rely=0.6)

    #button 7 in scrollable frame
        u_db_button7=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button7.grid(row=2,column=0,rowspan=1,padx=20,pady=20)
        u_db_btn10=CTkButton(u_db_button7,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_7)
        u_db_btn10.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 7
        u_db_img9=Image.open("pictures/pngegg (3) 1french_fries.png")
        u_db_img9=u_db_img9.resize((210,200))
        photo_u_db_img9tk=ImageTk.PhotoImage(u_db_img9)
        u_db_img9_lbl = tk.Label(u_db_button7, image=photo_u_db_img9tk,bg="#D9D9D9")
        u_db_img9_lbl.place(x=15, y=5, w=210, h=200)
        u_db_label7=tk.Label(u_db_button7,text=f"Name: {items_lst[6][0]}\n   Price: Rs.{price_lst[6][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label7.place(relx=0.15,rely=0.6)

    #button 8 in scrollable frame
        u_db_button8=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button8.grid(row=2,column=1,rowspan=1,padx=0,pady=0)
        u_db_btn11=CTkButton(u_db_button8,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_8)
        u_db_btn11.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 8
        u_db_img10=Image.open("pictures/pngegg (14) 1coke.png")
        u_db_img10=u_db_img10.resize((160,160))
        photo_u_db_img10tk=ImageTk.PhotoImage(u_db_img10)
        u_db_img10_lbl = tk.Label(u_db_button8, image=photo_u_db_img10tk,bg="#D9D9D9")
        u_db_img10_lbl.place(x=40, y=17, w=160, h=160)
        u_db_label8=tk.Label(u_db_button8,text=f"Name: {items_lst[7][0]}\n   Price: Rs.{price_lst[7][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label8.place(relx=0.18,rely=0.6)

    #button 9 in scrollable frame
        u_db_button9=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button9.grid(row=2,column=2,rowspan=1,padx=20,pady=20)
        u_db_btn12=CTkButton(u_db_button9,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_9)
        u_db_btn12.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 9
        u_db_img11=Image.open("pictures/pngegg (13) 1oreo_shake.png")
        u_db_img11=u_db_img11.resize((180,160))
        photo_u_db_img11tk=ImageTk.PhotoImage(u_db_img11)
        u_db_img11_lbl = tk.Label(u_db_button9, image=photo_u_db_img11tk,bg="#D9D9D9")
        u_db_img11_lbl.place(x=40, y=15, w=180, h=160)
        u_db_label9=tk.Label(u_db_button9,text=f"Name: {items_lst[8][0]}\n   Price: Rs.{price_lst[8][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label9.place(relx=0.15,rely=0.6)

    #button 10 in scrollable frame
        u_db_button10=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button10.grid(row=3,column=0,rowspan=1,padx=20,pady=0)
        u_db_btn13=CTkButton(u_db_button10,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_10)
        u_db_btn13.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 10
        u_db_img12=Image.open("pictures/pngegg (11) 1cofee.png")
        u_db_img12=u_db_img12.resize((200,200))
        photo_u_db_img12tk=ImageTk.PhotoImage(u_db_img12)
        u_db_img12_lbl = tk.Label(u_db_button10, image=photo_u_db_img12tk,bg="#D9D9D9")
        u_db_img12_lbl.place(x=25, y=5, w=200, h=200)
        u_db_label10=tk.Label(u_db_button10,text=f"Name: {items_lst[9][0]}\n   Price: Rs.{price_lst[9][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label10.place(relx=0.15,rely=0.6)
        
    #button 11 in scrollable frame
        u_db_button11=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button11.grid(row=3,column=1,rowspan=1,padx=0,pady=0)
        u_db_btn14=CTkButton(u_db_button11,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_11)
        u_db_btn14.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 11
        u_db_img15=Image.open("pictures/pngegg (2) 2momo.png")
        u_db_img15=u_db_img15.resize((190,190))
        photo_u_db_img15tk=ImageTk.PhotoImage(u_db_img15)
        u_db_img15_lbl = tk.Label(u_db_button11, image=photo_u_db_img15tk,bg="#D9D9D9")
        u_db_img15_lbl.place(x=30, y=8, w=190, h=190)
        u_db_label11=tk.Label(u_db_button11,text=f"Name: {items_lst[10][0]}\n   Price: Rs.{price_lst[10][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label11.place(relx=0.1,rely=0.6)

    #button 12 in scrollable frame
        u_db_button12=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button12.grid(row=3,column=2,rowspan=1,padx=20,pady=0)
        u_db_btn15=CTkButton(u_db_button12,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_12)
        u_db_btn15.place(rely=0.8,relx=0.15,relheight=0.15)
        u_db_label12=tk.Label(u_db_button12,text=f"    Name: {items_lst[11][0]}\n   Price: Rs.{price_lst[11][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label12.place(relx=0.15,rely=0.6)

    #image and label for button 12
        u_db_img13=Image.open("pictures/pngegg (15) 1sprite.png")
        u_db_img13=u_db_img13.resize((140,160))
        photo_u_db_img13tk=ImageTk.PhotoImage(u_db_img13)
        u_db_img13_lbl = tk.Label(u_db_button12, image=photo_u_db_img13tk,bg="#D9D9D9")
        u_db_img13_lbl.place(x=55, y=20, w=140, h=160)

    #button 13 in scrollable frame
        u_db_button13=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button13.grid(row=4,column=0,rowspan=1,padx=20,pady=20)
        u_db_btn16=CTkButton(u_db_button13,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_13)
        u_db_btn16.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 13
        u_db_img14=Image.open("pictures/pngegg (16) 1fanta.png")
        u_db_img14=u_db_img14.resize((160,160))
        photo_u_db_img14tk=ImageTk.PhotoImage(u_db_img14)
        u_db_img14_lbl = tk.Label(u_db_button13, image=photo_u_db_img14tk,bg="#D9D9D9")
        u_db_img14_lbl.place(x=45, y=15, w=160, h=160)
        u_db_label13=tk.Label(u_db_button13,text=f"   Name: {items_lst[12][0]}\n   Price: Rs.{price_lst[12][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label13.place(relx=0.15,rely=0.6)

    #button 14 in scrollable frame
        u_db_button14=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button14.grid(row=4,column=1,rowspan=1,padx=0,pady=20)
        u_db_btn17=CTkButton(u_db_button14,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_14)
        u_db_btn17.place(rely=0.8,relx=0.15,relheight=0.15)

    #image and label for button 14
        u_db_img16=Image.open("pictures/pngegg (3) 2chowmein.png")
        u_db_img16=u_db_img16.resize((200,200))
        photo_u_db_img16tk=ImageTk.PhotoImage(u_db_img16)
        u_db_img16_lbl = tk.Label(u_db_button14, image=photo_u_db_img16tk,bg="#D9D9D9")
        u_db_img16_lbl.place(x=25, y=5, w=200, h=200)
        u_db_label14=tk.Label(u_db_button14,text=f"Name: {items_lst[13][0]}\n   Price: Rs.{price_lst[13][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label14.place(relx=0.04,rely=0.6)

    #button 15 in scrollable frame
        u_db_button15=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
        u_db_button15.grid(row=4,column=2,rowspan=1,padx=20,pady=20)
        u_db_btn18=CTkButton(u_db_button15,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937",command=user_proceed_15)
        u_db_btn18.place(rely=0.8,relx=0.15,relheight=0.15)
    #image and label for button 15 
        u_db_img17=Image.open("pictures/pngegg (4) 2Biryani.png")
        u_db_img17=u_db_img17.resize((235,180))
        photo_u_db_img17tk=ImageTk.PhotoImage(u_db_img17)
        u_db_img17_lbl = tk.Label(u_db_button15, image=photo_u_db_img17tk,bg="#D9D9D9")
        u_db_img17_lbl.place(x=10, y=5, w=235, h=180)
        u_db_label15=tk.Label(u_db_button15,text=f"Name: {items_lst[14][0]}\n   Price: Rs.{price_lst[14][0]}",font=("Inter",15),bg="#D9D9D9")
        u_db_label15.place(relx=0.1,rely=0.6)

    #menubutton
    u_db_menubutton=tk.Menubutton(u_db_menubtn,text="All items  ▼",bg="white",font=("Regular",13),fg="Red",activebackground="white",activeforeground="red",bd=0)
    u_db_menubutton.place(relx=0.1,rely=0.07,relheight=0.8,relwidth=0.8)

    #menubutton menus
    u_db_menu=tk.Menu(u_db_menubutton,tearoff=0)
    u_db_menubutton["menu"]=u_db_menu
    u_db_menu.add_command(label="All",foreground="red",font=("regular",12),background="white",activebackground="white",activeforeground="red", command = main_menu)
    u_db_menu.add_command(label="Foods",foreground="red",font=("regular",12),background="white",activebackground="white",activeforeground="red",command=foods)
    u_db_menu.add_command(label="Drinks",foreground="red",font=("regular",12),background="white",activebackground="white",activeforeground="red",command=drinks)

    #menu table frame for displaying the name, quantity and price of items
    u_db_frame3=CTkFrame(u_db_mainframe,corner_radius=12,fg_color="#D9D9D9")
    u_db_frame3.place(relwidth=0.45,relheight=0.05,relx=0.5,rely=0.13)

    u_db_frame4=CTkFrame(u_db_mainframe,corner_radius=12,fg_color="#D9D9D9")
    u_db_frame4.place(relwidth=0.45,relheight=0.67,relx=0.5,rely=0.19)

    u_db_framee=CTkFrame(u_db_frame,fg_color="#D9D9D9",corner_radius=10)
    u_db_framee.place(relwidth=1,relheight=0.12, rely = 0.85)
    
    def show_total():
        u_db_ttllbl=tk.Label(u_db_framee,text=f"Total:Rs. {total_price}",font = ("Inter",15),bg="#D9D9D9")
        u_db_ttllbl.place(relx=0.8,rely=0.35)
    
    #the total button
    u_db_ttlbtn=tk.Button(u_db_framee,text="Total", font = ("Inter",15,"bold"),bg="#D9D9D9",command=show_total)
    u_db_ttlbtn.place(relx=0.65,rely=0.28,relwidth=0.13)

    #payment option label
    u_db_ttlbtn=CTkButton(u_db_framee,text="Payment Option: Cash", font = ("Inter",15,"bold"),fg_color="#D9D9D9",border_width=2,border_color="Black",text_color="Black",corner_radius=0,hover=0)
    u_db_ttlbtn.place(relx=0.05,rely=0.25,relwidth=0.26,relheight=0.5)







    #label
    u_db_lbl2=tk.Label(u_db_frame3,text="Product Name",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
    u_db_lbl2.place(relx=0.08,rely=0.17)

    #label
    u_db_lbl3=tk.Label(u_db_frame3,text="Price",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
    u_db_lbl3.place(relx=0.4,rely=0.17)

    #label
    u_db_lbl4=tk.Label(u_db_frame3,text="Quantity",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
    u_db_lbl4.place(relx=0.61,rely=0.17)

    #label
    u_db_lbl5=tk.Label(u_db_frame3,text="Total Price",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
    u_db_lbl5.place(relx=0.82,rely=0.17)


    #separator frame
    u_db_sep_frame1=tk.Frame(u_db_frame3,bg="black")
    u_db_sep_frame1.place(relwidth=0.005,relheight=1,relx=0.3)

    #separator frame 
    u_db_sep_frame2=tk.Frame(u_db_frame3,bg="black")
    u_db_sep_frame2.place(relwidth=0.005,relheight=1,relx=0.55)

    #separator frame 
    u_db_sep_frame3=tk.Frame(u_db_frame3,bg="black")
    u_db_sep_frame3.place(relwidth=0.005,relheight=1,relx=0.76)

    main_menu()








#-------------------------------------------------------Main Dashboard---------------------------------------------------------#









def main():
    """This function opens the main page when called."""




#----------------------------------------------------------------items data table-----------------------------------------------------#
    global items_lst, price_lst
    conn = sqlite3.connect('mealmate.db')
    #fetch items data from mealmate.db
    c = conn.cursor()
    c.execute("SELECT item_name FROM item")
    items_lst = c.fetchall()
    c.execute("SELECT item_price FROM item")
    price_lst = c.fetchall()
    conn.close()
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------------#


    def exit():
        """this function is made to ask a yes-no question to the user when exit button is clicked and if the user clicks yes then the root is destroyed. """
        response = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if response==1:
            root.destroy()

    def about_page():
        global photo_about_page_logo
        c=tk.Toplevel()
        c.iconbitmap("pictures/32432hotbeverage_98916.ico")
        c.title("About Mealmate")
        c.geometry("1000x700")
        c.resizable(0,0)

        main_about_page_frame=tk.Frame(c,bg="white")
        main_about_page_frame.place(relheight=1,relwidth=1,relx=0,rely=0)

        about_page_frame1=tk.Frame(main_about_page_frame,bg="white")
        about_page_frame1.place(relheight=0.15,relwidth=1,relx=0,rely=0)

        about_page_logo=Image.open("pictures/Rectangle 41.png")
        about_page_logo=about_page_logo.resize((468,97))
        photo_about_page_logo=ImageTk.PhotoImage(about_page_logo)
        #label that contains image
        about_page_lbl = tk.Label(main_about_page_frame, image=photo_about_page_logo,bg="white")
        about_page_lbl.place(x=280, y=8, w=468, h=97)

        about_page_frame2=CTkFrame(main_about_page_frame,fg_color="#F7D8D8",corner_radius=15)
        about_page_frame2.place(relwidth=1,relheight=0.9,relx=0,rely=0.16)

        about_page_label1=tk.Label(about_page_frame2,text="Your Everyday Mealtime\n   Companion",font=("Inter",25,"italic"),bg="#F7D8D8",fg="#A1201C")
        about_page_label1.place(relx=0.3,rely=0.1)

        about_page_label2=tk.Label(about_page_frame2,text="Welcome to Mealmate Cafe, where delicious meals, cozy\nvibes, and friendly faces are always on the menu. At\nMealmate, we believe that food is more than just\nsustenance it's about connection, comfort, and creating\nmemories.",font=("Inter",25,"italic"),bg="#F7D8D8",fg="black")
        about_page_label2.place(relx=0.11,rely=0.3)



    global main_frame1
    #the main frame
    main_frame1=tk.Frame(root)
    main_frame1.place(relheight=1,relwidth=1,x=0,y=0)
    #background image
    dashboard_image1=Image.open("pictures\\dashboard_bg.png")
    dashboard_image1=dashboard_image1.resize((1920,990))
    photodashboard_image1=ImageTk.PhotoImage(dashboard_image1)
    #label for image
    dash_label1 = tk.Label(main_frame1, image=photodashboard_image1)
    dash_label1.place(x=0, y=0, w=1920, h=990)


    #image in exit button
    exit_image=ImageTk.PhotoImage(file="pictures/dashicons_exit.png")

    
#image for i button 
    i_image=ImageTk.PhotoImage(file="pictures/Vectori_button(white).png")


#frame
    f=CTkFrame(main_frame1,width=450,height=600,border_width=3,fg_color="White",border_color="BLack")
    f.place(relx=0.35,rely=0.16)

#the image for logo
    image2=Image.open("pictures\\Rectangle 41.png")
    image2=image2.resize((508,105))
    photoimage2=ImageTk.PhotoImage(image2)
#button for logo
    Button1 = tk.Button(f, image=photoimage2,bg="White",activebackground="White",bd=0,command=about_page)
    Button1.place(relx=0.05,rely=0.025)


    f1=tk.Frame(f,width=560,height=10,bg="Black")
    f1.place(rely=0.2)

#the frame containing all buttons
    f2=CTkFrame(f,width=433,height=457,fg_color="White",border_color="Black",border_width=3)
    f2.place(relx=0.0201,rely=0.226)


#user login button
    b1=CTkButton(f2,text="User Login",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#D1D1D1",fg_color="#3A3848",hover=0,command=user_login)
    b1.place(relx=0.204,rely=0.12)
#i button in user login
    ib1=tk.Button(b1,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button1)
    ib1.place(relx=0.87,rely=0.35)

#admin login button
    b2=CTkButton(f2,text="Admin Login",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#D1BC56",fg_color="#3A3848",hover=0,command=admin_login)
    b2.place(relx=0.204,rely=0.33)
#i button in admin login
    ib2=tk.Button(b2,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button2)
    ib2.place(relx=0.89,rely=0.35)

#user signup button
    b3=CTkButton(f2,text="User Signup",width=262,height=55,corner_radius=30,font=("Inter",33),text_color="#E25A00",fg_color="#3A3848",hover=0,command=user_signup)
    b3.place(relx=0.204,rely=0.54)
#i button in user signup
    ib3=tk.Button(b3,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button3)
    ib3.place(relx=0.89,rely=0.35)

#admin signup button
    b4=CTkButton(f2,text="Admin Signup",width=240,height=55,corner_radius=30,font=("Inter",33),text_color="#48A31E",fg_color="#3A3848",hover=0,command=admin_signup)
    b4.place(relx=0.204,rely=0.74)
#i button in admin signup
    ib4=tk.Button(b4,image=i_image,bg="#3A3848",bd=0,activebackground="#3A3848",command=i_button4)
    ib4.place(relx=0.9,rely=0.35)

    back_button=tk.Button(f2,text="Exit",image=exit_image,compound=LEFT,font=("Inter",20),bg="white",activebackground="white",activeforeground="black",bd=0,command=exit)
    back_button.place(relx=0.05,rely=0.9)
    


    root.mainloop()

if __name__ == '__main__':
    main()




#----------------------------------------------------------END----------------------------------------------------------------#