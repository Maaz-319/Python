# Imports
import tkinter as tk
from tkinter import messagebox
from data import current_cashier, total_sales
import database_handler_cashier as db_cashier
from class_cashier import Cashier
import os

# Global variables
bg_color = "#f0f0f0"
primary_color = "#004d40"
accent_color = "#00bfa5"
text_color = "#333333"
error_color = "#ff5252"
admin_code = 7391
cashier_login = db_cashier.get_all_items_name() # list of registered Cashiers
new_cashier = None # variable for cashier object

# ======================================= Functions ======================================================

# -------------------------------------- Function to log in ---------------------------------------------
def login(_=None):
    username = username_entry.get().lower()
    password = password_entry.get()

    # ------------------- Validation for Input Data ----------------------------
    if username == "" or password == "": # for empty entries
        messagebox.showerror("Error", "Please enter both username and password")
        return
    elif username not in cashier_login: # for unregistered cashier
        messagebox.showerror("Error", "Username not found")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        return
    elif db_cashier.get_item_by_name(username)[2] != password: # for wrong password
        messagebox.showerror("Error", "Incorrect password")
        password_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        return
    # ---------------------------------------------------------------------------

    current_cashier = username
    # write current cashier to file
    with open('data.py', 'w') as f:
        f.write(
            f'current_cashier = "{current_cashier}"\ntotal_sales = {total_sales}\n')
        f.close()
    messagebox.showinfo("Success", "Login Successful")
    window.destroy()
    os.system('program.pyw') # run program

# --------------------------------- Function for creating Sign Up Window --------------------------
def create_signup():
    # ---------------- Initialize window------------
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.geometry("250x250")
    signup_window.resizable(False, False)
    # ----------------------------------------------

    signup_frame = tk.Frame(signup_window, bg=bg_color) # Frame

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
                              command=lambda: signup(signup_username_entry, signup_password_entry, admin_code_entry,
                                                     signup_window))
    signup_button.pack()
# -----------------------------------------------------------------------------------------------------

# ======================================== Function to Sign Up =======================================
def signup(username, password, admin_pass, window_2):
    global new_cashier

    username = username.get().lower()
    password = password.get()
    admin_pass = admin_pass.get()

    # ---------- User Input Validation ------------------------------------
    if username == "" or password == "": # for empty fields
        messagebox.showerror("Error", "Please enter both username and password")
        return
    elif username in cashier_login: # for already registered cashier
        messagebox.showerror("Error", "Username already exists")
        return
    elif admin_pass != str(admin_code): # for authorization of admin
        messagebox.showerror("Error", "Incorrect Admin Code\nPlease contact the administrator")
        return
    # ----------------------------------------------------------------------

    new_cashier = Cashier(username, password) # create cashier object
    new_cashier.add_cashier() # save cashier to database

    current_cashier = None
    with open('data.py', 'w') as f:
        f.write(
            f'current_cashier = {current_cashier}\ntotal_sales = {total_sales}')
        f.close()
    messagebox.showinfo("Success", "Sign Up Successful\nPlease login to continue")
    window.destroy()
    # window_2.destroy()
# -----------------------------------------------------------------------------------------------------
# =======================================================================================================================


#  ========================================= Define the Window ==========================================
# Main window attributes
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

login_button = tk.Button(login_frame, cursor='hand2', text="Login", bg=primary_color, fg="white", border=0,
                         font=("Comic Sans Ms", 10),
                         command=login)
login_button.pack()

signup_button = tk.Button(login_frame, cursor='hand2', text="Sign Up", bg=accent_color, fg="white", border=0,
                          font=("Comic Sans Ms", 10),
                          command=create_signup)
signup_button.pack(pady=10)
# =================================================
window.mainloop()
# ==================================================================================================================