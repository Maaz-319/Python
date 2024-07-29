# Imports
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from settings import current_user
import settings_handler as se
import database_handler_user as db_user
from class_user import User
import os

# Global variables
bg_color = "#a8abad"
primary_color = "#004d40"
accent_color = "#00bfa5"
text_color = "#333333"
error_color = "#ff5252"
admin_code = 7391
user_login = db_user.show_all_name() if db_user.show_all_name() else []
new_user = None


# ======================================= Functions ======================================================

# -------------------------------------- Function to log in ---------------------------------------------
def login(_=None):
    global current_user, theme
    username = username_entry.get().lower()
    password = password_entry.get()

    # ------------------- Validation for Input Data ----------------------------
    if username == "" or password == "":  # for empty entries
        messagebox.showerror("Error", "Please enter both username and password")
        return
    elif username not in user_login:  # for unregistered cashier
        messagebox.showerror("Error", "Username not found")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        return
    elif db_user.search(username)[7] != password:  # for wrong password
        messagebox.showerror("Error", "Incorrect password")
        password_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        return
    # ---------------------------------------------------------------------------

    current_user = username
    # write current cashier to file
    se.update_settings(current_user)
    window.destroy()
    os.system('program.pyw')  # run program


# --------------------------------- Function for creating Sign Up Window --------------------------
def create_signup():
    # ---------------- Initialize window------------
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.geometry("300x500")
    signup_window.resizable(False, False)
    # ----------------------------------------------

    signup_frame = tk.Frame(signup_window, bg=bg_color)  # Frame

    tk.Label(signup_frame, text="SIGN UP", bg=bg_color, fg=text_color,
             font=("Comic Sans Ms", 15, "bold underline")).pack(
        pady=10)
    signup_frame.pack()

    tk.Label(signup_frame, text="Name", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_username_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_username_entry.pack(pady=5)

    tk.Label(signup_frame, text="Password", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_password_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color, show="*")
    signup_password_entry.pack(pady=5)

    tk.Label(signup_frame, text="Phone(03xx-xxxxxxx)", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_phone_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_phone_entry.pack(pady=5)

    tk.Label(signup_frame, text="Email", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_email_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_email_entry.pack(pady=5)

    tk.Label(signup_frame, text="Address", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_address_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_address_entry.pack(pady=5)

    tk.Label(signup_frame, text="Account Type", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_account_type_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_account_type_entry.pack(pady=5)

    tk.Label(signup_frame, text="Initial Balance", bg=bg_color, fg=text_color, font=("Comic Sans Ms", 10)).pack()

    signup_balance_entry = tk.Entry(signup_frame, bg=bg_color, fg=text_color)
    signup_balance_entry.pack(pady=5)

    signup_button = tk.Button(signup_frame, cursor='hand2', text="Sign Up", bg=primary_color, fg="white", border=0,
                              font=("Comic Sans Ms", 10),
                              command=lambda: signup(signup_username_entry, signup_password_entry, signup_window, signup_phone_entry, signup_email_entry, signup_address_entry, signup_account_type_entry, signup_balance_entry))
    signup_button.pack()


# -----------------------------------------------------------------------------------------------------

# ======================================== Function to Sign Up =======================================
def signup(username, password, window_2, phone, email, address, account_type, balance):
    global new_user, current_user, window

    username = username.get().lower()
    password = password.get()
    phone = phone.get()
    email = email.get()
    address = address.get()
    account_type = account_type.get()
    try:
        balance = int(balance.get())
        if balance < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid Balance, Atleast Value: Rs.1")
        return

    # ---------- User Input Validation ------------------------------------
    if username == "" or password == "" or email == "" or phone == "" or address == "" or account_type == "" or balance == "":  # for empty fields
        messagebox.showerror("Error", "All Fields are Required")
        return
    elif not phone.isdigit() or len(phone) != 11 or "03" not in phone:  # for invalid phone number
        messagebox.showerror("Error", "Invalid Phone Number")
        return
    elif "@" and "." not in email:  # for invalid email
        messagebox.showerror("Error", "Invalid Email")
        return
    elif username in user_login:  # for already registered User
        messagebox.showerror("Error", "Username already exists")
        return
    # ----------------------------------------------------------------------

    new_user = User(username, phone, email, address, account_type, balance, password)
    new_user.add_user()  # save user to database

    current_user = None
    se.update_settings(current_user)
    messagebox.showinfo("Success", "Sign Up Successful\nPlease login to continue")
    window.destroy()
    window_2.destroy()


# -----------------------------------------------------------------------------------------------------
# =======================================================================================================================


#  ========================================= Define the Window ==========================================
# Main window attributes
window = tk.Tk()
window.configure(bg=bg_color)
window.title("Welcome to BMS Login")
window.geometry("300x300")
window.resizable(False, False)
window.bind("<Return>", login)
tb.Style().theme_use("united")

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
