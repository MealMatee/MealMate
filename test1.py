import sqlite3



def create_new_user():
    conn = sqlite3.connect('mealmate.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user 
                  ( 
                   first_name TEXT, 
                   last_name TEXT, 
                   email TEXT, 
                   password TEXT,
                   )''')
    conn.commit()
    conn.close()

def user_data():
    conn = sqlite3.connect('mealmate.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    all_user_data = c.fetchall()
    conn.close()
    return all_user_data

def delete_user(email):
    conn = sqlite3.connect('mealmate.db')
    c = conn.cursor()
    c.execute("DELETE FROM user WHERE email = ?", (email,))
    conn.commit()
    conn.close()

def update_user (new_first_name, new_last_name, new_email, new_password):
    conn = sqlite3.connect('mealmate.db')
    c = conn.cursor()
    c.execute("UPDATE user SET first_name = ?, last_name = ?, email = ?, password = ? WHERE email = ?", (new_first_name, new_last_name, new_email, new_password, email))
    conn.commit()
    conn.close()