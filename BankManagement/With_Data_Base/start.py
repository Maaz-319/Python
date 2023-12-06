import getpass, os
import database_handler as db
current_login = ""



os.system('cls')
print("\n\t\t\tWelcom to Bank Management System.\n")
print("********************************************************************************")
name_found = False
password_found = False


def ask_pass():
    secret_key = "Maaz"
    password = getpass.getpass(prompt='Password: ', stream=None)
    if password != secret_key:
        print("\n\tWrong password!!!!")
        input("\n\tPress Enter...")
        exit()


def start():
    os.system('cls')
    initial_event = int(input("\n\tChoose:\n\t\t1) Login\n\t\t2) Sign up\n\t\t3) See all account holders\n\t\t4) Exit\n\tchoice: "))
    if initial_event == 1:
        login()
    elif initial_event == 2:
        crt_acc()
    elif initial_event == 3:
        all_acc_hold_list()
    elif initial_event == 4:
        exit()
    else:
        start()

def crt_acc():
    try:
        all_accounts = db.show_all()[0]
    except IndexError:
        all_accounts = ""
    name = str(input("\nEnter account name: "))
    if name in all_accounts:
        print("\n\n\tName already Used\n\tChoose Something else.")
        crt_acc()
    money = int(input("Enter initial amount of money: "))
    pin = getpass.getpass(prompt='Enter pin for your account(4-digit): ', stream=None)
    length = len(pin)
    while length != 4:
        pin = getpass.getpass(prompt='Please enter atleast 4digit pin: ', stream=None)
        length = len(pin)
    db.add_record(name, pin, money)
    print("\n\tNew Account Info:\n")
    print("\n\t\tYour account name is : ", db.show_one(name)[0][0])
    print("\n\t\tYou have " ,db.show_one(name)[0][2],"Rs in your account.")
    input("\n\tPress Enter...")
    start()

def login():
    global name_found, current_login
    name = str(input("\nEnter account name: "))
    fetch_data = db.show_one(name)
    if fetch_data:
        pin = getpass.getpass("Enter account pin: ")
        if fetch_data[0][1] == pin:
            current_login = name
            logged_in(name, fetch_data)
        else:
            print("wrong Password!")
            input("\n\tPress Enter...")
            login()
    else:
        input("\n\tAccount Not Found!!\n\n\tPress Enter...")
        start()


def del_acc():
    name = str(input("\nEnter account name to DELETE: "))
    fetch_data = db.show_one(name)
    if not fetch_data:
        print("No account found!")
        del_acc()
    else:
        pin = getpass.getpass("Enter account pin: ")
        if pin == fetch_data[0][1]:
            temp = input("Type CONFIRM in caps: ")
            if temp == "CONFIRM":
                db.delete_record(name)
                print("\nAccount was deleted!")
                input()
            else:
                del_acc()
        else:
            print("Wrong password!")
            del_acc()
    start()



def withd_money(name, fetch_data):
    pin = getpass.getpass("Enter account pin: ")
    if pin == fetch_data[0][1]:
        money = int(input("Enter amount of money you want to withdraw: "))
    elif pin != fetch_data[0][1]:
        print("wrong Password!")
        input("\n\tPress Enter...")
        withd_money(name, fetch_data)
    if money < 0:
        print("\nIncorrect amount!")
        input("\n\tPress Enter...")
        withd_money(name, fetch_data)
    if money < fetch_data[0][2]:
        money = fetch_data[0][2] - money
        db.update_record(name, money)
        fetch_data = db.show_one(name)
        print("\n\tThere are ", db.show_one(name)[0][2], "Rs left in your account.")
        input("\n\tPress Enter...")
    else:
        print("\n\tNot enough money in account :(!")
        input("\n\tPress Enter...")
        withd_money(name, fetch_data)
    logged_in(name, fetch_data)
        
def deposit_money(name, fetch_data):
    pin = getpass.getpass("Enter your account pin: ")
    if pin == fetch_data[0][1]:
        money = int(input("Enter amount of money you want to deposit: "))
        if money < 0:
            print("\nIncorrect amount!")
            input("\n\tPress Enter...")
            deposit_money(name, fetch_data)
        else:
            money = fetch_data[0][2] + money           
            db.update_record(name, money)
            fetch_data = db.show_one(name)
            print("\n\tThere are ", fetch_data[0][2], "Rs in your account.")
            input("\n\tPress Enter...")
    else:
        print("Wrong account pin!")
        input("\n\tPress Enter...")
        os.system('cls')
        deposit_money()
    logged_in(name, fetch_data)


def all_acc_hold_list():
    name_list = db.show_all()
    if name_list:
        print("\n\tAll Account Holders Names:")
        for i in name_list:
            print("\t\t-" + i[0])
    else:
        print("\n\tNo Accounts Registered")
    input("\nPress Enter...")
    start()


def logged_in(name, fetch_data):
    os.system('cls')
    print("\n\tLogged IN")
    print("\n\tAccount Name: " + name)
    print("\tBalance: Rs. ", db.show_one(name)[0][2])

    try:
        user_choice = int(input("\n\tChoose option:\n\t\t1) Withdraw\n\t\t2) Deposit\n\t\t3) Delete account\n\t\t4) Logout\n\t\t5) Exit\n\n\tchoice: "))
    except ValueError:
        print("Enter Correct Input :(")
        user_choice = int(input("\n\tChoose option:\n\t\t1) Withdraw\n\t\t2) Deposit\n\t\t3) Delete account\n\t\t4) Logout\n\t\t5) Exit\n\n\tchoice: "))

    if user_choice == 1:
        withd_money(name, fetch_data)
    elif user_choice == 2:
        deposit_money(name, fetch_data)
    elif user_choice == 3:
        del_acc()
    elif user_choice == 4:
        start()
    elif user_choice == 5:
        exit()
    else:
        print("Wrong Input!!")
        logged_in(name, fetch_data)

ask_pass()
start()