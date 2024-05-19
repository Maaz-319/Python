# ============ Bank Management System ================

# ================== Imports ==========================
import os
import database_handler as db

# Global Variable to store account object
# new_account = None
new_account_holder = None


# ================== Classes  ================================================================================
class account_holder:
    def __init__(self, holder_name, phone, email, address="", account_object=None):
        self.holder_name = holder_name
        self.phone = phone
        self.email = email
        self.address = address
        self.account_object = account_object

    # -----------------------------------------------------------------

    # This function displays account holder information
    def request_info(self):
        os.system('cls')

        print(" Account Holder Information ".center(50, '='))
        print(f"\nName: '{self.holder_name.title()}'")
        print(f"Phone: '{self.phone}'")
        print(f"Email: '{self.email}'")
        print(f"Address: '{self.address.title()}'")
        print(f"Account Type: {self.account_object.acc_type.title()}")
        print(f"Balance: {self.account_object.balance}")

        input()


# ----------------------------------------------------------------------------------------------

class account:
    def __init__(self, cust_name, acc_type, balance, password):
        self.cust_name = cust_name
        self.acc_type = acc_type
        self.balance = balance
        self.password = password

    # -----------------------------------------------------------------

    # This Function deposits money into account
    def deposit_money(self):
        amount = 0
        os.system('cls')

        print(" Deposit Money ".center(50, '='))

        # ===================Check if amount entered is integer===================
        try:
            amount = int(input("Enter Amount: "))
        except ValueError:
            self.deposit_money()
        # ========================================================================

        # ============amount is only deposited if amount is greater than 0==============
        if amount > 0:
            self.balance += amount
            db.update_record(self.cust_name, self.balance)
            self.logged_in()
        else:
            self.deposit_money()
        # ================================================================================

    # -----------------------------------------------------------------

    # This Function Withdraws money into account
    def withdraw_money(self):
        amount = 0
        os.system('cls')

        print(" Withdraw Money ".center(50, '='))

        # =================Check if amount entered is integer===================
        try:
            amount = int(input("Enter Amount: "))
        except ValueError:
            self.withdraw_money()
        # ========================================================================

        # =========amount is only withdrawn if there is enough money in account===========
        if self.balance >= amount > 0:
            self.balance -= amount
            db.update_record(self.cust_name, self.balance)
            self.logged_in()
        else:
            input(f"\nInsufficient Balance\n\tBalance = {self.balance}\n")
            self.withdraw_money()
        # ================================================================================

    # ----------------------------------------------------------------------------------------------

    # This Functions login the user into account if user exists
    def login(self, name, password):
        if name == self.cust_name and password == self.password:  # Check if user exists and if Password is correct
            self.logged_in()
            return True
        else:
            return False

    # ----------------------------------------------------------------------------------------------\

    # This Function runs when user successfully login
    def logged_in(self):
        user_choice = 0
        os.system('cls')

        print(f"Logged in to '{self.cust_name.title()}'")
        print(f"Type: '{self.acc_type.title()}'")
        print(f"Balance: '{self.balance}'")
        print("\n\n\t1. Deposit\n\t2. Withdraw\n\t3. Logout\n\t4. Request Account Info")

        # ===================Check if amount entered is integer===================
        try:
            user_choice = int(input("\n\tChoice: "))
        except ValueError:
            self.logged_in()
        # ========================================================================

        # ============User Choice to Deposit, Withdraw, Logout or Request Account Info==============
        if user_choice == 1:
            self.deposit_money()
            self.logged_in()
        elif user_choice == 2:
            self.withdraw_money()
            self.logged_in()
        elif user_choice == 3:
            initialize_program()
        elif user_choice == 4:
            new_account_holder.request_info()
            self.logged_in()
        else:
            self.logged_in()
        # ================================================================================


# =========================================================================================================
#                                             Functions
# =========================================================================================================


# This function gets confidential to log in to account
def start_login():
    global new_account_holder

    name = None
    password = None

    os.system('cls')

    print(" Login ".center(50, '='))

    # ==========Getting all the required information to login================
    try:
        name = input("\nEnter Your Name: ").lower()
    except ValueError:
        start_login()

    # ===================Get account and account holder from database===================
    results_account = db.search(name, "Account")  # Get account from database
    results_holder = db.search(name, "Holder")  # Get account holder from database
    # ==================================================================================

    # ===============Check if account exists in database==============
    if not results_account or not results_holder:
        print("\n\tAccount Not Found!")
        input()
        initialize_program()
    else:
        results_account = results_account[0]  # returned data is in list of list, so we get the first list
        results_holder = results_holder[0]  # returned data is in list of list, so we get the first list

        # Validating Password
        try:
            password = input("Enter Password: ")
        except ValueError:
            start_login()
        # ===================

        # ==============================Authorize Login==============================================
        if results_account[0] == name and results_account[3] == password:
            new_account = account(results_account[0], results_account[1], results_account[2],
                                  results_account[3])  # Create account object
            new_account_holder = account_holder(results_holder[0], results_holder[1], results_holder[2],
                                                results_holder[3], new_account)  # Create account_holder object
        else:
            input("Wrong Password")
            start_login()
        if not new_account.login(name, password):
            print("Login failed")
            start_login()
        # ==========================================================================================


# ---------------------------------------------------------------------------------------------------------------------

# This function creates new account
def create_new_account(a):
    global new_account_holder

    name = None
    password = None
    account_type = None
    balance = None
    phone = None
    email = None
    address = None

    os.system('cls')

    # Check if wrong value is entered
    if a:
        print("\nWrong Value Entered, Retry")

    print(" Account Creation ".center(50, '='))

    # ================Getting all the required information to create account================
    try:
        name = input("\nEnter Your Name: ").lower()

        results = db.search(name, "Account")  # Get account from database

        if results:  # Check if account already exists
            for x in results[0]:
                if name == x[0]:
                    print("\n\tAccount Already Exists!")
                    input()
                    initialize_program()

        # ...................................................................
        phone = str(input("Enter Phone Number(03xx-xxxxxxx): ")).lower()
        if len(phone) != 11:
            raise ValueError
        # ...................................................................

        # ...................................................................
        email = input("Enter Email: ").lower()
        if not "@" and "." in email:
            raise ValueError
        # ...................................................................

        address = input("Enter Address: ").lower()
        password = input("Enter Password: ").lower()
        account_type = input("Enter account type or leave empty: ").lower()
        balance = int(input("Enter account initial balance: "))
        # ==================================================================================
    except ValueError:
        create_new_account(True)

    new_account = account(name, account_type if account_type else "Savings", balance, password)  # Create account object

    # Create new account_holder Object
    new_account_holder = account_holder(name, phone, email, address, new_account)

    # Save account to database
    db.add_record(new_account_holder)

    input("\nAccount created Successfully")
    initialize_program()


# ----------------------------------------------------------------------------------------------

# This function asks user to create account or Login
def initialize_program():
    user_choice = 0
    os.system('cls')  # clear screen

    print(" Bank Management System ".center(80, '='))
    print("\n\n\t1. Login\n\t2. Create Account\n\t3. Exit")

    # ===================Check if amount entered is integer===================
    try:
        user_choice = int(input("\n\tChoice: "))
    except ValueError:
        initialize_program()
    # ========================================================================

    # ============User Choice to Create Account, Login or Exit==============
    if user_choice == 1:
        start_login()
    elif user_choice == 2:
        create_new_account(False)
    elif user_choice == 3:
        db.close_database_connection()
        exit()
    else:
        initialize_program()  # If any other choice other than 1,2,3 is entered, function restarts
    # ================================================================================


# =========================================================================================================
#                                            Code by: Maaz Bin Asif
#                                               Date: 17/05/2024
#                                            Email: maazbinaasif@gmail.com
#                                            Github: github.com/maaz-319
# =========================================================================================================

if __name__ == '__main__':
    initialize_program()
# =========================================================================================================
