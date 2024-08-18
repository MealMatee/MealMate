import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import sqlite3
from tkinter import messagebox

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
        messagebox.showwarning("Warning", "Please select a user to update.")
        return
    
    user = tree.item(selected_item)['values']
    update_window = ctk.CTkToplevel(root)
    update_window.title("Update User")
    update_window.geometry("300x200")

    ctk.CTkLabel(update_window, text="First Name:").pack()
    new_first_name = ctk.CTkEntry(update_window)
    new_first_name.insert(0, user[0])
    new_first_name.pack()

    ctk.CTkLabel(update_window, text="Last Name:").pack()
    new_last_name = ctk.CTkEntry(update_window)
    new_last_name.insert(0, user[1])
    new_last_name.pack()

    ctk.CTkLabel(update_window, text="Email:").pack()
    new_email = ctk.CTkEntry(update_window)
    new_email.insert(0, user[2])
    new_email.pack()

    ctk.CTkLabel(update_window, text="Password:").pack()
    new_password = ctk.CTkEntry(update_window, show="*")
    new_password.insert(0, user[3])
    new_password.pack()

    def save_changes():
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET first_name=?, last_name=?, email=?, password=? WHERE email=?",
                       (new_first_name.get(), new_last_name.get(), new_email.get(), new_password.get(), user[2]))
        conn.commit()
        update_window.destroy()
        load_users()

    ctk.CTkButton(update_window, text="Save Changes", command=save_changes).pack(pady=10)

def delete_user():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a user to delete.")
        return
    
    user = tree.item(selected_item)['values']
    if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the user {user[2]}?"):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE email=?", (user[2],))
        conn.commit()
        load_users()

def show_all_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    
    all_data_window = ctk.CTkToplevel(root)
    all_data_window.title("All User Data")
    all_data_window.geometry("800x600")
    
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

# Create main window
root = ctk.CTk()
root.title("User Management System")
root.geometry("800x600")

# Create main frame
customize_user_mf = ctk.CTkFrame(root)
customize_user_mf.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Search section
search_frame = ctk.CTkFrame(customize_user_mf)
search_frame.pack(fill=tk.X, padx=10, pady=10)

ctk.CTkLabel(search_frame, text="SEARCH BY:-").pack(anchor=tk.W)

# First Name
first_name_frame = ctk.CTkFrame(search_frame)
first_name_frame.pack(fill=tk.X, pady=5)
ctk.CTkLabel(first_name_frame, text="FirstName:").pack(side=tk.LEFT)
first_name_entry = ctk.CTkEntry(first_name_frame, placeholder_text="FirstName")
first_name_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
ctk.CTkButton(first_name_frame, text="SEARCH", command=lambda: search_users("first_name")).pack(side=tk.RIGHT)

# Last Name
last_name_frame = ctk.CTkFrame(search_frame)
last_name_frame.pack(fill=tk.X, pady=5)
ctk.CTkLabel(last_name_frame, text="LastName:").pack(side=tk.LEFT)
last_name_entry = ctk.CTkEntry(last_name_frame, placeholder_text="LastName")
last_name_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
ctk.CTkButton(last_name_frame, text="SEARCH", command=lambda: search_users("last_name")).pack(side=tk.RIGHT)

# Email
email_frame = ctk.CTkFrame(search_frame)
email_frame.pack(fill=tk.X, pady=5)
ctk.CTkLabel(email_frame, text="Email:").pack(side=tk.LEFT)
email_entry = ctk.CTkEntry(email_frame, placeholder_text="example@gmail.com")
email_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
ctk.CTkButton(email_frame, text="SEARCH", command=lambda: search_users("email")).pack(side=tk.RIGHT)

# Clear and All Data buttons
button_frame = ctk.CTkFrame(search_frame)
button_frame.pack(fill=tk.X, pady=10)
ctk.CTkButton(button_frame, text="CLEAR", command=clear_search).pack(side=tk.LEFT, expand=True, padx=5)
ctk.CTkButton(button_frame, text="ALL DATA", command=show_all_data).pack(side=tk.LEFT, expand=True, padx=5)

# Treeview
tree = ttk.Treeview(customize_user_mf, columns=("FirstName", "LastName", "Email", "Password"), show="headings")
tree.heading("FirstName", text="First Name")
tree.heading("LastName", text="Last Name")
tree.heading("Email", text="Email")
tree.heading("Password", text="Password")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Buttons frame
button_frame = ctk.CTkFrame(customize_user_mf)
button_frame.pack(fill=tk.X, padx=10, pady=10)

ctk.CTkButton(button_frame, text="UPDATE", command=update_user).pack(side=tk.LEFT, expand=True, padx=5)
ctk.CTkButton(button_frame, text="DELETE", command=delete_user).pack(side=tk.LEFT, expand=True, padx=5)
ctk.CTkButton(button_frame, text="EXIT", command=root.quit).pack(side=tk.LEFT, expand=True, padx=5)

# Initialize database and load users
conn = sqlite3.connect("mealmate.db")
load_users()

root.mainloop()