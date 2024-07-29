import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import ttkbootstrap as tb
from class_user import User
from class_transaction import Transaction
import datetime
from settings import current_user
import settings_handler as se
import database_handler_user as db_user
import database_handler_transaction as db_transaction

user_login = None
new_user = None
new_transaction = None

class BankManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System")
        self.root.state("zoomed")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        tb.Style().theme_use("united")
        tb.Style().configure("Treeview", foreground="black", font=("Arial", 12), rowheight=25, borderwidth=0, selectborderwidth=0)
        tb.Style().configure("Treeview.Heading", font=("Arial", 15, "bold"), foreground="black")

        self.the_cursor = "hand2"
        self.the_font = ("Arial", 10, 'bold')


        # Treeview frame
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(fill=tk.X, padx=10, pady=5, side=tk.TOP)
        self.create_treeview()
        # Form frame
        self.form_frame = ttk.LabelFrame(self.root, text="Actions")
        self.form_frame.pack(fill=tk.BOTH, padx=10, pady=30)

        self.modify_account_frame = ttk.LabelFrame(self.root, text="Modify Account")

        self.create_buttons()

        self.preview()

        self.show_modify_account()


    def create_form(self):
        self.modify_account_frame.pack(fill=tk.X, padx=10, pady=5, side=tk.BOTTOM, expand=True)
        
        tk.Label(self.modify_account_frame, text="Name", font=self.the_font).grid(row=0, column=0, columnspan=2, pady=10)
        self.name_var = tk.Entry(self.modify_account_frame)
        self.name_var.grid(row=0, column=2, columnspan=3, pady=10, padx=10)

        tk.Label(self.modify_account_frame, text="Phone", font=self.the_font).grid(row=1, column=0, columnspan=2, pady=10)
        self.phone_var = tk.Entry(self.modify_account_frame)
        self.phone_var.grid(row=1, column=2, columnspan=3, pady=10, padx=10)

        tk.Label(self.modify_account_frame, text="Email", font=self.the_font).grid(row=2, column=0, columnspan=2, pady=10)
        self.email_var = tk.Entry(self.modify_account_frame)
        self.email_var.grid(row=2, column=2, columnspan=3, pady=10, padx=10)

        tk.Label(self.modify_account_frame, text="Address", font=self.the_font).grid(row=0, column=5, columnspan=2, pady=10)
        self.address_var = tk.Entry(self.modify_account_frame)
        self.address_var.grid(row=0, column=7, pady=10)

        tk.Label(self.modify_account_frame, text="Account Type", font=self.the_font).grid(row=1, column=5, columnspan=2, pady=10)
        self.account_type_var = tk.Entry(self.modify_account_frame)
        self.account_type_var.grid(row=1, column=7, pady=10)

        tk.Button(self.modify_account_frame, text="Modify Account", height=2, cursor=self.the_cursor, command=self.modify_account).grid(row=2, column=5, padx=10, pady=5)

    def create_buttons(self):
        tk.Label(self.form_frame).grid(row=0, column=0, pady=10, padx=120)
        tk.Button(self.form_frame, text="Withdraw\nMoney", command=self.withdraw_money, height=5, cursor=self.the_cursor, width=20).grid(row=0, column=1, padx=20, pady=5, sticky="ew")
        tk.Button(self.form_frame, text="Deposit\nMoney", command=self.deposit_money, height=5, cursor=self.the_cursor, width=20).grid(row=0, column=2, padx=20, pady=5, sticky="ew")
        tk.Button(self.form_frame, text="Download\nInfo", command=self.download_info, height=5, cursor=self.the_cursor, width=20).grid(row=0, column=3, padx=20, pady=5, sticky="ew")
        tk.Button(self.form_frame, text="Transaction\nHistory", command=self.download_transaction_history, height=5, cursor=self.the_cursor, width=20).grid(row=0, column=4, padx=20, pady=5, sticky="ew")
        tk.Button(self.form_frame, text="Close\nAccount", command=self.delete_user, height=5, cursor=self.the_cursor, width=20).grid(row=0, column=5, padx=20, pady=5, sticky="ew")

    def create_treeview(self):
        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Name", "Phone", "Email", "Address", "Account Type", "Balance"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Account Type", text="Account Type")
        self.tree.heading("Balance", text="Balance")

        self.tree.column("ID", width=50)
        self.tree.column("Name", width=100)
        self.tree.column("Phone", width=100)
        self.tree.column("Email", width=150)
        self.tree.column("Address", width=200)
        self.tree.column("Account Type", width=100)
        self.tree.column("Balance", width=100)

        self.tree.pack(fill="both", expand=True)

    def preview(self):
        global new_user, current_user

        results = db_user.search(current_user)

        self.modify_account_frame.pack(fill=tk.BOTH, padx=10, pady=30)
        

        new_user = User(results[1], results[2], results[3], results[4], results[5], results[6], results[7])
        
        self.clear_table()

        self.tree.insert("", "end", values=(results[0], new_user.name.capitalize(), new_user.phone, new_user.email, new_user.address.capitalize(), new_user.account_type.capitalize(), new_user.balance))
    
    def show_modify_account(self):
        global new_user

        self.create_form()
        
        self.clear_form()

        self.name_var.insert(0, new_user.name)
        self.phone_var.insert(0, new_user.phone)
        self.email_var.insert(0, new_user.email)
        self.address_var.insert(0, new_user.address)
        self.account_type_var.insert(0, new_user.account_type)
    
    def modify_account(self):
        global new_user, user_login

        username = self.name_var.get().lower()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get().lower()
        account_type = self.account_type_var.get().lower()

        if username == "" or email == "" or phone == "" or address == "" or account_type == "":  # for empty fields
            messagebox.showerror("Error", "All Fields are Required")
            return
        elif not phone.isdigit() or len(phone) != 11 or "03" not in phone:  # for invalid phone number
            messagebox.showerror("Error", "Invalid Phone Number")
            return
        elif "@" and "." not in email:  # for invalid email
            messagebox.showerror("Error", "Invalid Email")
            return
        elif username != new_user.name:  # for already registered User
            if username in user_login:
                messagebox.showerror("Error", "Username already exists")
                return
        # ----------------------------------------------------------------------

        new_name = username
        if new_name != new_user.name:
            name_updated = True
        new_user.phone = phone
        new_user.email = email
        new_user.address = address
        new_user.account_type = account_type

        new_user.update_user(new_name)
        
        self.preview()

        if name_updated:
            self.on_closing(2)


    def delete_user(self):
        global new_user

        if new_user.balance > 0:
            messagebox.showerror("Error", f"There are Rs.{new_user.balance} in your Account\nPlease Withdraw Money")
            return
        
        if messagebox.askyesno("Delete Account", "Are you sure you want to Close this account?"):
            new_user.delete_user()
            self.on_closing(1)

    def withdraw_money(self):
        global new_user, new_transaction

        if new_user.balance == 0:
            messagebox.showerror("Error", "No Balance\nPlease Deposit Money")
            return

        try:
            withdraw_amount = int(tk.simpledialog.askfloat("Withdraw Money", "Enter Amount"))
            if not withdraw_amount:
                raise ValueError
            if withdraw_amount > new_user.balance:
                messagebox.showerror("Error", "Not Enough Balance")
                return
            if withdraw_amount < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid Amount")
            return
        

        new_user.withdraw_money(withdraw_amount)

        self.preview()

        user_id = db_user.search(new_user.name)[0]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        new_transaction = Transaction(user_id, "Withdraw", withdraw_amount, current_date, current_time)
        new_transaction.save_transaction()
        
        messagebox.showinfo("Success", f"New Balance :{new_user.balance}")


    def deposit_money(self):
        global new_user

        try:
            deposit_amount = int(tk.simpledialog.askfloat("Deposit Money", "Enter Amount"))
            if not deposit_amount:
                raise ValueError
            if deposit_amount < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid Amount")
            return
        
        
        new_user.deposit_money(deposit_amount)
        
        self.preview()

        user_id = db_user.search(new_user.name)[0]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        new_transaction = Transaction(user_id, "Deposit", deposit_amount, current_date, current_time)
        new_transaction.save_transaction()

        messagebox.showinfo("Success", f"New Balance :{new_user.balance}")

        

    def download_info(self):
        global new_user

        messagebox.showinfo("Success", f"File Saved with the name '{new_user.download_info()}'")
    
    def download_transaction_history(self):
        global new_user, new_transaction

        user_id = db_user.search(new_user.name)[0]
        transactions = db_transaction.search(user_id)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%I:%M %p")

        if not transactions:
            messagebox.showerror("Error", "No Transactions Found")
            return

        with open(f"HISTORY {new_user.name}.txt", "w") as file:
            file.write(f"Transaction History of '{new_user.name.capitalize()}' Created on {current_date} at {current_time}\n{'-'*50}\n")
            for transaction in transactions:
                new_transaction = Transaction(transaction[0], transaction[1], transaction[2], transaction[3], transaction[4])
                file.write(str(new_transaction))
                file.write("\n")
                file.write("-"*50 + "\n")
        
        messagebox.showinfo("Success", f"File Saved with the name 'HISTORY {new_user.name}.txt'")

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def clear_form(self):
        self.name_var.delete(0, tk.END)
        self.phone_var.delete(0, tk.END)
        self.email_var.delete(0, tk.END)
        self.address_var.delete(0, tk.END)
        self.account_type_var.delete(0, tk.END)
    
    def on_closing(self, event=None):
        global current_user

        if event == 2:
            messagebox.showinfo("Update", f"Please Login Again\nFrom now on, you will login through '{new_user.name.capitalize()}'")
            self.root.destroy()
            current_user = None
            se.update_settings(current_user)
        elif event:
            self.root.destroy()
            current_user = None
            se.update_settings(current_user)
        else:
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                db_user.close_connection()
                current_user = None
                se.update_settings(current_user)
                self.root.destroy()

def authorize():
    global user_login, new_user
    if not current_user:
        messagebox.showerror("Error", "Please login to continue")
        return
    new_user = None
    user_login = db_user.show_all_name() if db_user.show_all_name() else []
    root = tk.Tk()
    app = BankManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    authorize()
