import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data import cashier_login, current_cashier, items_list, order_data
import os

# Global variables
bg_color = "#f0f0f0"
primary_color = "#004d40"
accent_color = "#00bfa5"
text_color = "#333333"
admin_code = 7391
error_color = "#ff5252"


# Function to log in
def login(_=None):
    username = username_entry.get().lower()
    password = password_entry.get().lower()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password")
        return
    elif username not in cashier_login:
        messagebox.showerror("Error", "Username not found")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        return
    elif cashier_login[username] != password:
        messagebox.showerror("Error", "Incorrect password")
        password_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        return

    current_cashier = username
    with open('data.py', 'w') as f:
        f.write(
            f'items_list = {items_list}\norder_data = {order_data}\ncashier_login = {cashier_login}\ncurrent_cashier = "{current_cashier}"\n')
        f.close()
    messagebox.showinfo("Success", "Login Successful")
    window.destroy()
    os.system('program.exe')


def create_signup():
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.geometry("250x250")
    signup_window.resizable(False, False)

    signup_frame = tk.Frame(signup_window, bg=bg_color)

    tk.Label(signup_frame, text="SIGN UP", bg=bg_color, fg=text_color,
             font=("Comic Sans Ms", 15, "bold underline")).pack(
        pady=10)
    signup_frame.pack()

    tk.Label(signup_frame, text="Username", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_username_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_username_entry.pack(pady=5)

    tk.Label(signup_frame, text="Password", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_password_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color, show="*")
    signup_password_entry.pack(pady=5)

    tk.Label(signup_frame, text="Admin Code", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()
    admin_code_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color, show="*")
    admin_code_entry.pack(pady=5)

    signup_button = tk.Button(signup_frame, cursor='hand2', text="Sign Up", bg=primary_color, fg="white", border=0,
                              font=("Comic Sans Ms", 10),
                              command=lambda: signup(signup_username_entry, signup_password_entry, admin_code_entry, signup_window))
    signup_button.pack()


def signup(username, password, admin_pass, window_2):
    username = username.get().lower()
    password = password.get().lower()
    admin_pass = admin_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password")
        return
    elif username in cashier_login:
        messagebox.showerror("Error", "Username already exists")
        return
    elif admin_pass != str(admin_code):
        messagebox.showerror("Error", "Incorrect Admin Code\nPlease contact the administrator")
        return

    cashier_login[username] = password
    current_cashier = None
    with open('data.py', 'w') as f:
        f.write(
            f'items_list = {items_list}\norder_data = {order_data}\ncashier_login = {cashier_login}\ncurrent_cashier = {current_cashier}\n')
        f.close()
    messagebox.showinfo("Success", "Sign Up Successful\nPlease login to continue")
    window.destroy()
    # window_2.destroy()


# Define the Window
window = tk.Tk()
window.configure()
window.title("Welcome to POS Login")
window.geometry("300x300")
window.resizable(False, False)
window.bind("<Return>", login)

# ================== Login Frame ==================
login_frame = tk.Frame(window, bg=bg_color)

tk.Label(login_frame, text="LOGIN", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 15, "bold underline")).pack(
    pady=10)
login_frame.pack()

tk.Label(login_frame, text="Username", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

username_entry = tk.Entry(login_frame, bg=bg_color, fg=text_color)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

password_entry = tk.Entry(login_frame, bg=bg_color, fg=text_color, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, cursor='hand2', text="Login", bg=primary_color, fg="white", border=0, font=("Comic Sans Ms", 10),
                         command=login)
login_button.pack()

signup_button = tk.Button(login_frame, cursor='hand2', text="Sign Up", bg=accent_color, fg="white", border=0,
                          font=("Comic Sans Ms", 10),
                          command=create_signup)
signup_button.pack(pady=10)
# =================================================
window.mainloop()
