from customtkinter import *
from PIL import Image,ImageTk
import tkinter as tk

root=CTk()
root.geometry("1500x750")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")

def foods():
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

    pass

def drinks():
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


def search_check():
    searched_item_value=u_db_entry.get()
    searched_item_value.lower()

    for i in items_lst: 
        i.lower()
    if searched_item_value in items_lst:
        if searched_item_value==items_lst[1]:
            u_db_button2.place_forget()
            u_db_button3.place_forget()
            u_db_button4.place_forget()
            u_db_button5.place_forget()
            u_db_button6.place_forget()
            u_db_button7.place_forget()
            u_db_button8.place_forget()
            u_db_button9.place_forget()
            u_db_button10.place_forget()
            u_db_button11.place_forget()
            u_db_button12.place_forget()
            u_db_button13.place_forget()
            u_db_button14.place_forget()
            u_db_button15.place_forget()

    pass









def customize():


    def u_db_onclick2():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if customize_entry4.cget("show") == "":
            customize_entry4.configure(show="*")
        else:
            customize_entry4.configure(show="")

    def u_db_onclick3():
        '''
        it is made so that we can hide or show password clicking the eye button
        '''
        if customize_entry5.cget("show") == "":
            customize_entry5.configure(show="*")
        else:
            customize_entry5.configure(show="")

    customize_win=tk.Toplevel()
    customize_win.title("Profile customization Menu")
    customize_win.iconbitmap("pictures//32432hotbeverage_98916.ico")
    customize_win.resizable(0,0)
    customize_win.geometry("1387x970+0+0")

#frame
    customize_frame1=tk.Frame(customize_win,width=712,height=970,bg="white")
    customize_frame1.place(x=0,y=0)
#frame
    customize_frame3=CTkFrame(customize_frame1,corner_radius=18,fg_color="#D9D9D9")
    customize_frame3.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

#user profile label
    customize_lbl2=tk.Label(customize_frame3,text="USER PROFILE",font=("Inter",26,"bold"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl2.place(relx=0.31,rely=0.02)

#firstname label
    customize_lbl3=tk.Label(customize_frame3,text="FirstName:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl3.place(relx=0.07,rely=0.1)
#firstname entrybox
    customize_entry1=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text="Firstname",placeholder_text_color="#97D5C9")
    customize_entry1.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.15)

#lastname label
    customize_lbl4=tk.Label(customize_frame3,text="LastName:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl4.place(relx=0.07,rely=0.23)
#lastname entrybox
    customize_entry2=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text="Lastname",placeholder_text_color="#97D5C9")
    customize_entry2.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.28)

#Email label
    customize_lbl5=tk.Label(customize_frame3,text="Email:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl5.place(relx=0.07,rely=0.36)
#Email entrybox
    customize_entry2=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text="example@gmail.com",placeholder_text_color="#97D5C9")
    customize_entry2.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.41)

#eyebutton
    customize_eye_img1=Image.open("pictures/ion_eyegrey_eye.png")
    customize_eye_img1tk=ImageTk.PhotoImage(customize_eye_img1)
    
    #password entry
    customize_lbl6=tk.Label(customize_frame3,text="Password:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl6.place(relx=0.07,rely=0.49)
    #password entrybox
    customize_entry3=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text="Password",placeholder_text_color="#97D5C9",show="*")
    customize_entry3.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.54)
    customize_entry3.configure(state=DISABLED)

# new password label
    customize_lbl7=tk.Label(customize_frame3,text="NewPassword:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl7.place(relx=0.07,rely=0.62)
# new password entrybox
    customize_entry4=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text="NewPassword",placeholder_text_color="#97D5C9",show="*")
    customize_entry4.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.67)
# new password eyebutton
    customize_entry_btn2=tk.Button(customize_entry4,bg="white",bd=0,activebackground="white",image=customize_eye_img1tk,command=u_db_onclick2)
    customize_entry_btn2.image=customize_eye_img1tk
    customize_entry_btn2.place(relx=0.92,rely=0.28)

#retype new password label
    customize_lbl8=tk.Label(customize_frame3,text="Re-Type NewPassword:",font=("Inter",20,"italic"),fg="#5B6E80",bg="#D9D9D9")
    customize_lbl8.place(relx=0.07,rely=0.75)
    #retype new password Entrybox
    customize_entry5=CTkEntry(customize_frame3,corner_radius=12,fg_color="white",border_color="#5B6E80",text_color="#97D5C9",font=("Inter",17),placeholder_text="Re-Type NewPassword",placeholder_text_color="#97D5C9",show="*")
    customize_entry5.place(relwidth=0.85,relheight=0.07,relx=0.07,rely=0.80)
    #retype new password eye button
    customize_entry_btn3=tk.Button(customize_entry5,bg="white",bd=0,activebackground="white",image=customize_eye_img1tk,command=u_db_onclick3)
    customize_entry_btn3.image=customize_eye_img1tk
    customize_entry_btn3.place(relx=0.92,rely=0.28)

#confirm button
    customize_button=CTkButton(customize_frame3,text="CONFIRM",font=("Inter",15,"bold"),fg_color="#97D5C9",text_color="#5B6E80")
    customize_button.place(relx=0.35,rely=0.91,relheight=0.06)

#frame
    customize_frame2=tk.Frame(customize_win,width=675,height=970,bg="white")
    customize_frame2.place(x=712,y=0)

#backgriund pic in admin dashboard
    customize_img=Image.open("pictures/Rectangle 79pic.png")
    customize_img=customize_img.resize((675,970))
    photo_customize_imgtk=ImageTk.PhotoImage(customize_img)
    customize_lbl = tk.Label(customize_frame2, image=photo_customize_imgtk,bg="#D9D9D9")
    customize_lbl.image = photo_customize_imgtk 
    customize_lbl.place(x=0, y=0,w=675,h=970)


# global u_db_img2,photo_u_db_logo

u_db_mainframe=CTkFrame(root,fg_color="black")
u_db_mainframe.place(relwidth=1,relheight=1,x=0,y=0)

items_lst=["Chicken Burger","Espresso","Chicken Pizza","Pepsi","Drumstick","Cold Coffee","French Fries", "CocaCola","Oreo Shake","Cappuccino","Chicken MoMo","Sprite","Fanta","Chicken Chowmein","Chicken Biryani"]

#the top frame 
u_db_frame1=tk.Frame(u_db_mainframe,bg="#ACACAC")
u_db_frame1.place(relwidth=1,relheight=0.12,relx=0,rely=0)

#logo
u_db_logo=Image.open("pictures\\Rectangle 41.png")
u_db_logo=u_db_logo.resize((508,105))
photo_u_db_logo=ImageTk.PhotoImage(u_db_logo)

#image in searchbutton
u_db_img2=CTkImage(Image.open("pictures/Vectorsearch.png"))

#logo
u_db_lbl1=tk.Label(u_db_frame1,image=photo_u_db_logo,bg="#ACACAC")
u_db_lbl1.place(relx=0.01,rely=0.04)

#frame for menubutton
u_db_menubtn=CTkFrame(u_db_frame1,fg_color="white",border_width=1,border_color="black",corner_radius=8)
u_db_menubtn.place(relwidth=0.08,relheight=0.45,relx=0.3,rely=0.3)



#search button
u_db_btn1=CTkButton(u_db_frame1,text="       Search",text_color="red",fg_color="white",border_width=1,border_color="black",image=u_db_img2,compound=RIGHT,corner_radius=8,font=("Regular",13),hover_color="#D9D9D9",command=search_check)
u_db_btn1.place(relwidth=0.07,relheight=0.45,relx=0.74,rely=0.3)

#Item name entrybox
u_db_entry=CTkEntry(u_db_frame1,corner_radius=0,fg_color="white",border_width=1,border_color="black",text_color="black",placeholder_text="Item Name",placeholder_text_color="black")
u_db_entry.place(relwidth=0.38,relheight=0.45,relx=0.37,rely=0.3)
# details_menu main frame
u_db_frame=CTkFrame(u_db_mainframe,corner_radius=7,fg_color="black")
u_db_frame.place(relwidth=0.45,relheight=0.85,relx=0.5,rely=0.15)

u_db_framee=CTkFrame(u_db_frame,fg_color="#D9D9D9",corner_radius=10)
u_db_framee.place(relwidth=1,relheight=0.14, rely = 0.83)



#customize profile button
u_db_btn2=CTkButton(u_db_frame1,text="CUSTOMIZE PROFILE",fg_color="Black",text_color="white",hover=0,font=("Inter",12,"bold"),command=customize)
u_db_btn2.place(relwidth=0.1,relheight=0.45,relx=0.82,rely=0.3)

#logout button
u_db_btn3=CTkButton(u_db_frame1,text="LOGOUT",fg_color="Black",text_color="white",hover=0,font=("Inter",12,"bold"))
u_db_btn3.place(relwidth=0.06,relheight=0.45,relx=0.93,rely=0.3)





def main_menu():
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
    u_db_btn4=CTkButton(u_db_button1,text="PROCEED",font=("Inter",18,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn4.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 1
    u_db_img3=Image.open("pictures/pngegg (2) 1Bargar.png")
    u_db_img3=u_db_img3.resize((230,210))
    photo_u_db_img3tk=ImageTk.PhotoImage(u_db_img3)
    u_db_img3_lbl = tk.Label(u_db_button1, image=photo_u_db_img3tk,bg="#D9D9D9")
    u_db_img3_lbl.place(x=15, y=5, w=230, h=210)
    u_db_label1=tk.Label(u_db_button1,text="Name: Chicken Burger\n  Price: Rs.350",font=("Inter",15),bg="#D9D9D9")
    u_db_label1.place(relx=0.1,rely=0.6)

#button 2 in scrollable frame
    u_db_button2=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button2.grid(row=0,column=2,padx=20,pady=20)
    u_db_btn5=CTkButton(u_db_button2,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn5.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 2
    u_db_img4=Image.open("pictures/pngegg (6) 1pizza.png")
    u_db_img4=u_db_img4.resize((220,200))
    photo_u_db_img4tk=ImageTk.PhotoImage(u_db_img4)
    u_db_img4_lbl = tk.Label(u_db_button2, image=photo_u_db_img4tk,bg="#D9D9D9")
    u_db_img4_lbl.place(x=15, y=5, w=220, h=200)
    u_db_label2=tk.Label(u_db_button2,text="Name: Chicken Pizza\n  Price: Rs.510",font=("Inter",15),bg="#D9D9D9")
    u_db_label2.place(relx=0.1,rely=0.6)

#button 3 in scrollable frame
    u_db_button3=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button3.grid(row=0,column=1,padx=0,pady=0)
    u_db_btn6=CTkButton(u_db_button3,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn6.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 3
    u_db_img5=Image.open("pictures/pngegg (8) 1cooooofe.png")
    u_db_img5=u_db_img5.resize((210,190))
    photo_u_db_img5tk=ImageTk.PhotoImage(u_db_img5)
    u_db_img5_lbl = tk.Label(u_db_button3, image=photo_u_db_img5tk,bg="#D9D9D9")
    u_db_img5_lbl.place(x=10, y=5, w=210, h=190)
    u_db_label3=tk.Label(u_db_button3,text="Name: Espresso\n   Price: Rs.210",font=("Inter",15),bg="#D9D9D9")
    u_db_label3.place(relx=0.17,rely=0.6)

#button 4 in scrollable frame
    u_db_button4=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button4.grid(row=1,column=0,rowspan=1,padx=20,pady=0)
    u_db_btn7=CTkButton(u_db_button4,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn7.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 4
    u_db_img6=Image.open("pictures/pngegg (4) 1pepsii.png")
    u_db_img6=u_db_img6.resize((160,160))
    photo_u_db_img6tk=ImageTk.PhotoImage(u_db_img6)
    u_db_img6_lbl = tk.Label(u_db_button4, image=photo_u_db_img6tk,bg="#D9D9D9")
    u_db_img6_lbl.place(x=45, y=15, w=160, h=160)
    u_db_label4=tk.Label(u_db_button4,text="   Name:Pepsi\n   Price: Rs.70",font=("Inter",15),bg="#D9D9D9")
    u_db_label4.place(relx=0.16,rely=0.6)

#button 5 in scrollable frame
    u_db_button5=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button5.grid(row=1,column=1,rowspan=1,padx=0,pady=0)
    u_db_btn8=CTkButton(u_db_button5,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn8.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 5
    u_db_img7=Image.open("pictures/pngegg (7) 1fried_chicken.png")
    u_db_img7=u_db_img7.resize((210,190))
    photo_u_db_img7tk=ImageTk.PhotoImage(u_db_img7)
    u_db_img7_lbl = tk.Label(u_db_button5, image=photo_u_db_img7tk,bg="#D9D9D9")
    u_db_img7_lbl.place(x=25, y=4, w=210, h=190)
    u_db_label5=tk.Label(u_db_button5,text="Name: Drumstick\n   Price: Rs.110",font=("Inter",15),bg="#D9D9D9")
    u_db_label5.place(relx=0.17,rely=0.6)

#button 6 in scrollable frame
    u_db_button6=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button6.grid(row=1,column=2,rowspan=1,padx=20,pady=0)
    u_db_btn9=CTkButton(u_db_button6,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn9.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 6
    u_db_img8=Image.open("pictures/pngegg (12) 1coffee_shake.png")
    u_db_img8=u_db_img8.resize((190,170))
    photo_u_db_img8tk=ImageTk.PhotoImage(u_db_img8)
    u_db_img8_lbl = tk.Label(u_db_button6, image=photo_u_db_img8tk,bg="#D9D9D9")
    u_db_img8_lbl.place(x=25, y=12, w=190, h=170)
    u_db_label6=tk.Label(u_db_button6,text="Name: Cold Coffee\n   Price: Rs.280",font=("Inter",15),bg="#D9D9D9")
    u_db_label6.place(relx=0.15,rely=0.6)

#button 7 in scrollable frame
    u_db_button7=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button7.grid(row=2,column=0,rowspan=1,padx=20,pady=20)
    u_db_btn10=CTkButton(u_db_button7,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn10.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 7
    u_db_img9=Image.open("pictures/pngegg (3) 1french_fries.png")
    u_db_img9=u_db_img9.resize((210,200))
    photo_u_db_img9tk=ImageTk.PhotoImage(u_db_img9)
    u_db_img9_lbl = tk.Label(u_db_button7, image=photo_u_db_img9tk,bg="#D9D9D9")
    u_db_img9_lbl.place(x=15, y=5, w=210, h=200)
    u_db_label7=tk.Label(u_db_button7,text="Name: French Fries\n   Price: Rs.280",font=("Inter",15),bg="#D9D9D9")
    u_db_label7.place(relx=0.15,rely=0.6)

#button 8 in scrollable frame
    u_db_button8=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button8.grid(row=2,column=1,rowspan=1,padx=0,pady=0)
    u_db_btn11=CTkButton(u_db_button8,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn11.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 8
    u_db_img10=Image.open("pictures/pngegg (14) 1coke.png")
    u_db_img10=u_db_img10.resize((160,160))
    photo_u_db_img10tk=ImageTk.PhotoImage(u_db_img10)
    u_db_img10_lbl = tk.Label(u_db_button8, image=photo_u_db_img10tk,bg="#D9D9D9")
    u_db_img10_lbl.place(x=40, y=17, w=160, h=160)
    u_db_label8=tk.Label(u_db_button8,text="Name: CocaCola\n   Price: Rs.70",font=("Inter",15),bg="#D9D9D9")
    u_db_label8.place(relx=0.18,rely=0.6)

#button 9 in scrollable frame
    u_db_button9=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button9.grid(row=2,column=2,rowspan=1,padx=20,pady=20)
    u_db_btn12=CTkButton(u_db_button9,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn12.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 9
    u_db_img11=Image.open("pictures/pngegg (13) 1oreo_shake.png")
    u_db_img11=u_db_img11.resize((180,160))
    photo_u_db_img11tk=ImageTk.PhotoImage(u_db_img11)
    u_db_img11_lbl = tk.Label(u_db_button9, image=photo_u_db_img11tk,bg="#D9D9D9")
    u_db_img11_lbl.place(x=40, y=15, w=180, h=160)
    u_db_label9=tk.Label(u_db_button9,text="Name: Oreo Shake\n   Price: Rs.450",font=("Inter",15),bg="#D9D9D9")
    u_db_label9.place(relx=0.15,rely=0.6)

#button 10 in scrollable frame
    u_db_button10=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button10.grid(row=3,column=0,rowspan=1,padx=20,pady=0)
    u_db_btn13=CTkButton(u_db_button10,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn13.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 10
    u_db_img12=Image.open("pictures/pngegg (11) 1cofee.png")
    u_db_img12=u_db_img12.resize((200,200))
    photo_u_db_img12tk=ImageTk.PhotoImage(u_db_img12)
    u_db_img12_lbl = tk.Label(u_db_button10, image=photo_u_db_img12tk,bg="#D9D9D9")
    u_db_img12_lbl.place(x=25, y=5, w=200, h=200)
    u_db_label10=tk.Label(u_db_button10,text="Name: Cappuccino\n   Price: Rs.200",font=("Inter",15),bg="#D9D9D9")
    u_db_label10.place(relx=0.15,rely=0.6)
    
#button 11 in scrollable frame
    u_db_button11=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button11.grid(row=3,column=1,rowspan=1,padx=0,pady=0)
    u_db_btn14=CTkButton(u_db_button11,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn14.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 11
    u_db_img15=Image.open("pictures/pngegg (2) 2momo.png")
    u_db_img15=u_db_img15.resize((190,190))
    photo_u_db_img15tk=ImageTk.PhotoImage(u_db_img15)
    u_db_img15_lbl = tk.Label(u_db_button11, image=photo_u_db_img15tk,bg="#D9D9D9")
    u_db_img15_lbl.place(x=30, y=8, w=190, h=190)
    u_db_label11=tk.Label(u_db_button11,text="Name: Chicken momo\n   Price: Rs.200",font=("Inter",15),bg="#D9D9D9")
    u_db_label11.place(relx=0.1,rely=0.6)

#button 12 in scrollable frame
    u_db_button12=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button12.grid(row=3,column=2,rowspan=1,padx=20,pady=0)
    u_db_btn15=CTkButton(u_db_button12,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn15.place(rely=0.8,relx=0.15,relheight=0.15)
    u_db_label12=tk.Label(u_db_button12,text="    Name: Sprite\n   Price: Rs.70",font=("Inter",15),bg="#D9D9D9")
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
    u_db_btn16=CTkButton(u_db_button13,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn16.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 13
    u_db_img14=Image.open("pictures/pngegg (16) 1fanta.png")
    u_db_img14=u_db_img14.resize((160,160))
    photo_u_db_img14tk=ImageTk.PhotoImage(u_db_img14)
    u_db_img14_lbl = tk.Label(u_db_button13, image=photo_u_db_img14tk,bg="#D9D9D9")
    u_db_img14_lbl.place(x=45, y=15, w=160, h=160)
    u_db_label13=tk.Label(u_db_button13,text="   Name: Fanta\n   Price: Rs.70",font=("Inter",15),bg="#D9D9D9")
    u_db_label13.place(relx=0.15,rely=0.6)

#button 14 in scrollable frame
    u_db_button14=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button14.grid(row=4,column=1,rowspan=1,padx=0,pady=20)
    u_db_btn17=CTkButton(u_db_button14,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn17.place(rely=0.8,relx=0.15,relheight=0.15)

#image and label for button 14
    u_db_img16=Image.open("pictures/pngegg (3) 2chowmein.png")
    u_db_img16=u_db_img16.resize((200,200))
    photo_u_db_img16tk=ImageTk.PhotoImage(u_db_img16)
    u_db_img16_lbl = tk.Label(u_db_button14, image=photo_u_db_img16tk,bg="#D9D9D9")
    u_db_img16_lbl.place(x=25, y=5, w=200, h=200)
    u_db_label14=tk.Label(u_db_button14,text="Name: Chicken Chowmein\n   Price: Rs.250",font=("Inter",15),bg="#D9D9D9")
    u_db_label14.place(relx=0.04,rely=0.6)

#button 15 in scrollable frame
    u_db_button15=CTkButton(u_db_sframe,width=200,height=250,fg_color="#D9D9D9",hover=0,border_width=3,border_color="#ED8937")
    u_db_button15.grid(row=4,column=2,rowspan=1,padx=20,pady=20)
    u_db_btn18=CTkButton(u_db_button15,text="PROCEED",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn18.place(rely=0.8,relx=0.15,relheight=0.15)
#image and label for button 15 
    u_db_img17=Image.open("pictures/pngegg (4) 2Biryani.png")
    u_db_img17=u_db_img17.resize((235,180))
    photo_u_db_img17tk=ImageTk.PhotoImage(u_db_img17)
    u_db_img17_lbl = tk.Label(u_db_button15, image=photo_u_db_img17tk,bg="#D9D9D9")
    u_db_img17_lbl.place(x=10, y=5, w=235, h=180)
    u_db_label15=tk.Label(u_db_button15,text="Name: Chicken Biryani\n   Price: Rs.250",font=("Inter",15),bg="#D9D9D9")
    u_db_label15.place(relx=0.1,rely=0.6)

#menubutton
u_db_menubutton=tk.Menubutton(u_db_menubtn,text="All items  ▼",bg="white",font=("Regular",13),fg="Red",activebackground="white",activeforeground="red",bd=0)
u_db_menubutton.place(relx=0.03,rely=0.07,relheight=0.8,relwidth=1)

#menubutton menus
u_db_menu=tk.Menu(u_db_menubutton,tearoff=0)
u_db_menubutton["menu"]=u_db_menu
u_db_menu.add_command(label="All",foreground="red",font=("regular",12),background="white",activebackground="white",activeforeground="red", command = main_menu)
u_db_menu.add_command(label="Foods",foreground="red",font=("regular",12),background="white",activebackground="white",activeforeground="red",command=foods)
u_db_menu.add_command(label="Drinks",foreground="red",font=("regular",12),background="white",activebackground="white",activeforeground="red",command=drinks)

#menu table frame for displaying the name, quantity and price of items
u_db_frame3=CTkFrame(u_db_mainframe,corner_radius=12,fg_color="#D9D9D9")
u_db_frame3.place(relwidth=0.45,relheight=0.72,relx=0.5,rely=0.13)

#label
u_db_lbl2=tk.Label(u_db_frame3,text="S.N",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
u_db_lbl2.place(relx=0.04,rely=0.03)

#label
u_db_lbl3=tk.Label(u_db_frame3,text="Product Name",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
u_db_lbl3.place(relx=0.26,rely=0.03)

#label
u_db_lbl4=tk.Label(u_db_frame3,text="Quantity",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
u_db_lbl4.place(relx=0.61,rely=0.03)

#label
u_db_lbl5=tk.Label(u_db_frame3,text="Price",font=("Inter",15,"bold"),bg="#D9D9D9",fg="#2D2825")
u_db_lbl5.place(relx=0.85,rely=0.03)


#separator frame
u_db_sep_frame1=tk.Frame(u_db_frame3,bg="black")
u_db_sep_frame1.place(relwidth=0.005,relheight=1,relx=0.12)

#separator frame 
u_db_sep_frame2=tk.Frame(u_db_frame3,bg="black")
u_db_sep_frame2.place(relwidth=0.005,relheight=1,relx=0.55)

#separator frame 
u_db_sep_frame3=tk.Frame(u_db_frame3,bg="black")
u_db_sep_frame3.place(relwidth=0.005,relheight=1,relx=0.76)

#separator frame 
u_db_sep_frame4=tk.Frame(u_db_frame3,bg="black")
u_db_sep_frame4.place(relwidth=1,relheight=0.008,rely=0.1)

main_menu()

root.mainloop()