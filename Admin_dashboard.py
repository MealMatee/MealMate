from customtkinter import *
import tkinter as tk
from PIL import Image,ImageTk

root=CTk()
root.geometry("1500x750")
root.iconbitmap("pictures//32432hotbeverage_98916.ico")
root.title("Admin_Dashboard")
root._set_appearance_mode("light")


# the main frame
main_frame6=CTkFrame(root,fg_color="Black")
main_frame6.place(relheight=1,relwidth=1,relx=0,rely=0)


def on_hover(enter):
    '''to change the text colour and image of button on entering the widget'''
    admin_db_btn2.configure(image=a_db_img5ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

def off_hover(leave):
    '''to change the text colour and image of button on enxiting the widget'''
    admin_db_btn2.configure(image=a_db_img1ctk,text_color="#DD2323",fg_color="#D9D9D9")


def on_hover2(enter):
    '''to change the text colour and image of button on entering the widget'''
    admin_db_btn3.configure(text_color="#33303C",fg_color="#F38686",hover_color="#F38686")
    admin_db_btn3_lbl.configure(image=a_db_img6ctk,fg_color="#F38686",bg_color="#F38686")

def off_hover2(leave):
    '''to change the text colour and image of button on enxiting the widget'''
    admin_db_btn3.configure(text_color="#DD2323",fg_color="#D9D9D9")
    admin_db_btn3_lbl.configure(image=a_db_img2ctk,fg_color="#D9D9D9",bg_color="#D9D9D9")


def on_hover3(enter):
    #to change the text colour and image of button on entering the widget
    admin_db_btn4.configure(image=a_db_img7ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

def off_hover3(leave):
    #to change the text colour and image of button on enxiting the widget
    admin_db_btn4.configure(image=a_db_img3ctk,text_color="#DD2323",fg_color="#D9D9D9")


def on_hover4(enter):
    #to change the text colour and image of button on entering the widget
    admin_db_btn5.configure(image=a_db_img8ctk,text_color="#33303C",fg_color="#F38686",hover_color="#F38686")

def off_hover4(leave):
    #to change the text colour and image of button on enxiting the widget
    admin_db_btn5.configure(image=a_db_img4ctk,text_color="#DD2323",fg_color="#D9D9D9")

def go_to_dash():
    admin_logout=tk.messagebox.askyesno("Logout?","Are you sure you want to log out?")
    if admin_logout==1:
        main_frame6.place_forget()
        tk.messagebox.showinfo("Success Message","LogOut Successful!!!")
        main()

def a_db_exit():
    response = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response==1:
        root.destroy()



def dashboard_frame_ad():
    global s_f_frame,admin_db_frame3,admin_db_customer_frame
    #dashboard frame
    admin_db_frame3=tk.Frame(main_frame6,bg="White")
    
    #items frame
    s_f_frame=tk.Frame(main_frame6)

    #Customers frame
    admin_db_customer_frame=tk.Frame(main_frame6,bg="Black")

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
    global photo_a_db_bg
    a_db_bg=Image.open("pictures/5883 1bg_adb.png")
    a_db_bg=a_db_bg.resize((1250,683))
    photo_a_db_bg=ImageTk.PhotoImage(a_db_bg)
    a_db_lbl2 = tk.Label(admin_db_frame3, image=photo_a_db_bg)
    a_db_lbl2.place(x=0, y=0, w=1250, h=683)

    #welcome label
    a_db_lbl6=tk.Label(admin_db_frame3,text="Welcome,",font=("Inter",60,"bold"),bg="White")
    a_db_lbl6.place(relx=0.26,rely=0.78)

#admin name label after welcome label
    a_db_lbl7=tk.Label(admin_db_frame3,text="Dristi",font=("Inter",60,"bold"),bg="White",fg="#DD2323")
    a_db_lbl7.place(relx=0.55,rely=0.78)
    


    pass


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
    u_db_btn4=CTkButton(u_db_button1,text="EDIT",font=("Inter",18,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_btn5=CTkButton(u_db_button2,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_btn6=CTkButton(u_db_button3,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button4.grid(row=0,column=3,pady=0)
    u_db_btn7=CTkButton(u_db_button4,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button5.grid(row=1,column=0,padx=20,pady=0)
    u_db_btn8=CTkButton(u_db_button5,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button6.grid(row=1,column=1,padx=0,pady=0)
    u_db_btn9=CTkButton(u_db_button6,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button7.grid(row=1,column=2,padx=0,pady=0)
    u_db_btn10=CTkButton(u_db_button7,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button8.grid(row=1,column=3,padx=0,pady=0)
    u_db_btn11=CTkButton(u_db_button8,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button9.grid(row=2,column=0,padx=20,pady=20)
    u_db_btn12=CTkButton(u_db_button9,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button10.grid(row=2,column=1,padx=0,pady=20)
    u_db_btn13=CTkButton(u_db_button10,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button11.grid(row=2,column=2,padx=20,pady=20)
    u_db_btn14=CTkButton(u_db_button11,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button12.grid(row=2,column=3,padx=0,pady=20)
    u_db_btn15=CTkButton(u_db_button12,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button13.grid(row=3,column=0,padx=20,pady=0)
    u_db_btn16=CTkButton(u_db_button13,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button14.grid(row=3,column=1,padx=0,pady=0)
    u_db_btn17=CTkButton(u_db_button14,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
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
    u_db_button15.grid(row=3,column=2,padx=20,pady=0)
    u_db_btn18=CTkButton(u_db_button15,text="EDIT",font=("Inter",20,"bold"),text_color="white",fg_color="#C8302B",corner_radius=10,hover_color="#ED8937")
    u_db_btn18.place(rely=0.8,relx=0.15,relheight=0.15)
#image and label for button 15 
    u_db_img17=Image.open("pictures/pngegg (4) 2Biryani.png")
    u_db_img17=u_db_img17.resize((235,180))
    photo_u_db_img17tk=ImageTk.PhotoImage(u_db_img17)
    u_db_img17_lbl = tk.Label(u_db_button15, image=photo_u_db_img17tk,bg="#D9D9D9")
    u_db_img17_lbl.place(x=10, y=5, w=235, h=180)
    u_db_label15=tk.Label(u_db_button15,text="Name: Chicken Biryani\n   Price: Rs.250",font=("Inter",15),bg="#D9D9D9")
    u_db_label15.place(relx=0.1,rely=0.6)

    pass






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
    
    pass







#top frame that coontains logo,item name entrybox and other widgets
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
a_db_btn8=CTkButton(admin_db_frame4,text="          Dristi",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
a_db_btn8.place(relx=0.4,rely=0.1,relwidth=0.18)
a_db_lbl4=tk.Label(a_db_btn8,text="Name:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
a_db_lbl4.place(relx=0.15,rely=0.05)

#Button used as a container to display label 
a_db_btn9=CTkButton(admin_db_frame4,text="             Dashboard",text_color="#DD2323",fg_color="#D9D9D9",hover=0,font=("Regular",15),corner_radius=14)
a_db_btn9.place(relx=0.7,rely=0.1,relwidth=0.2)
a_db_lbl5=tk.Label(a_db_btn9,text="Page:",fg="#33303C",font=("Regular",15),bg="#D9D9D9")
a_db_lbl5.place(relx=0.12,rely=0.05)

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




root.mainloop()