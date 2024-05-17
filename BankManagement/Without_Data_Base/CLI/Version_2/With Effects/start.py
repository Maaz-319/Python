import getpass, os, time, sys

current_login = ""


# secret_key = "Maaz"
# password = getpass.getpass(prompt='Password: ', stream=None)
# if password != secret_key:
#     print("\n\tWrong password!!!!")
#     input("\n\tPress Enter...")
#     exit()


def move_cursor_to_line_and_column(line, column):
    sys.stdout.write(f'\x1b[{line};{column}H')
    sys.stdout.flush()


def print_text_slowly(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)  # Use 'end' to avoid newline after each character
        time.sleep(delay)  # Add a delay between characters
    print()


os.system('cls')
print_text_slowly("\n\t\t\tWelcom to Bank Management System.\n")
print_text_slowly("*"*80)
input("\n\t\t\tPress Enter to Start...")
acc_found = False




def start():
    os.system('cls')
    print_text_slowly("\n\tChoose:\n\t\t1) Login\n\t\t2) Create Account\n\t\t3) Exit\n\tchoice: \b")
    move_cursor_to_line_and_column(6, 18)
    initial_event = int(input("\b"))
    if initial_event == 1:
        login()
    elif initial_event == 2:
        crt_acc()
    elif initial_event == 3:
        exit()
    else:
        start()

def crt_acc():
    global name, money, pin
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    name = str(input("\nEnter account name: "))
    money = int(input("Enter initial amount of money: "))
    pin = getpass.getpass(prompt='Enter pin for your account(4-digit): ', stream=None)
    length = len(pin)
    while length != 4:
        pin = getpass.getpass(prompt='Please enter atleast 4digit pin: ', stream=None)
        length = len(pin)
    acc_name.append(name)
    acc_money.append(money)
    acc_pass.append(pin)
    a = acc_name.index(name)
    file = open("data22.py", 'w')
    file.write('acc_name = ' + str(acc_name) + '\n')
    file.write('acc_pass = ' + str(acc_pass) + '\n')
    file.write('acc_money = ' + str(acc_money) + '\n')
    file.close()
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    print_text_slowly("\n\tNew Account Info:\n")
    print_text_slowly("\n\t\tYour account name is : " + acc_name[a])
    print_text_slowly("\n\t\tYou have " + str(acc_money[a]) + "Rs in your account.")
    input("\n\tPress Enter...")
    start()

def login():
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    global acc_found, current_login
    name = str(input("\nEnter account name: "))
    if name in acc_name:
        global passo
        acc_found = True
        pin = getpass.getpass("Enter account pin: ")
        a = acc_name.index(name)
        if pin != acc_pass[a]:
            print_text_slowly("wrong Password!")
            input("\n\tPress Enter...")
            login()
        elif pin == acc_pass[a]:
            current_login = name
            logged_in()
    else:
        input("\n\tAccount Not Found!!\n\n\tPress Enter...")
        start()


def del_acc():
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    global acc_found

    name = current_login

    if name not in acc_name:
        print_text_slowly("No account found!")
        del_acc()
    if name in acc_name:
        pin = getpass.getpass("Enter account pin: ")
        a = acc_name.index(name)
        pass1 = acc_pass[a]
        money = acc_money[a]
        if pin == acc_pass[a]:
            temp = input("Type CONFIRM in caps: ")
            if temp == "CONFIRM":
                acc_name.remove(name)
                acc_pass.remove(pass1)
                acc_money.remove(money)
                file = open("data22.py", 'w')
                file.write('acc_name = ' + str(acc_name) + '\n')
                file.write('acc_pass = ' + str(acc_pass) + '\n')
                file.write('acc_money = ' + str(acc_money) + '\n')
                file.close()
                print_text_slowly("\nAccount was deleted!")
                input()
            else:
                logged_in()
        else:
            print_text_slowly("Wrong password!")
            del_acc()
    
    start()



def withd_money():
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    global acc_found, current_login
    name = current_login

    if name in acc_name:
        global passo
        acc_found = True
        pin = getpass.getpass("Enter account pin: ")
        a = acc_name.index(name)
        if pin == acc_pass[a]:
            money = int(input("Enter amount of money you want to withdraw: "))
        elif pin != acc_pass[a]:
            print_text_slowly("wrong Password!")
            input("\n\tPress Enter...")
            withd_money()
        
        if money < 0:
            print_text_slowly("\nIncorrect amount!")
            input("\n\tPress Enter...")
            logged_in()
        if money < acc_money[a]:
            file = open("data22.py", 'w')
            acc_money[a] = acc_money[a] - money
            file.write('acc_name = ' + str(acc_name) + '\n')
            file.write('acc_pass = ' + str(acc_pass) + '\n')
            file.write('acc_money = ' + str(acc_money) + '\n')
            file.close()
            print("\n\tThere are " + str(acc_money[a]) + "Rs left in your account.")
            input("\n\tPress Enter...")
        else:
            print_text_slowly("\n\tNot enough money in account :(!")
            input("\n\tPress Enter...")
            logged_in()
    logged_in()
        
def deposit_money():
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    global acc_found, current_login
    global name
    name = current_login

    if name in acc_name:
         
        acc_found = True
        a = acc_name.index(name)
        pin = getpass.getpass("Enter your account pin: ")
        if pin == acc_pass[a]:    
            money = int(input("Enter amount of money you want to deposit: "))
            acc_money[a] = acc_money[a] + money
            file = open("data22.py", 'w')
            file.write('acc_name = ' + str(acc_name) + '\n')
            file.write('acc_pass = ' + str(acc_pass) + '\n')
            file.write('acc_money = ' + str(acc_money) + '\n')
            file.close()
            print_text_slowly("\n\tThere are " + str(acc_money[a]) + "Rs in your account.")
            input("\n\tPress Enter...")
        else:
            print_text_slowly("Wrong account pin!")
            input("\n\tPress Enter...")
            os.system('cls')
            deposit_money()
    logged_in()

def all_acc_hold_list():
    from data22 import acc_name
    print("\n")
    print_text_slowly(str(acc_name))
    input("\n\tPress Enter...")
    logged_in()


# def logged_in():
#     from data22 import acc_name
#     from data22 import acc_pass
#     from data22 import acc_money
#     global acc_found, current_login
#     a = acc_name.index(current_login)
#     os.system('cls')
#     print("\n\tLogged IN")
#     print("\n\tAccount Name: " + acc_name[a])
#     print("\tBalance: Rs. ", acc_money[a])
#     try:
#         #user_choice = int(input("\n\tChoose option:\n\t\t1) Create Account\n\t\t2) Delete Account\n\t\t3) Withdraw\n\t\t4) Deposit\n\tChoice: "))
#         user_choice = int(input("\n\tChoose option:\n\t\t1) Withdraw\n\t\t2) Deposit\n\t\t3) Delete account\n\t\t4) See all account holders\n\t\t5) Go Back\n\t\t6) Exit\n\n\tchoice: "))
#     except ValueError:
#         print("Enter Correct Input :(")
#         #user_choice = int(input("\n\tChoose option:\n\t\t1) Create Account\n\t\t2) Delete Account\n\t\t3) Withdraw\n\t\t4) Deposit\n\tChoice: "))
#         user_choice = user_choice = int(input("\n\tChoose option:\n\n\t\t1) Create Account\n\t\t2) Withdraw\n\t\t3) Deposit\n\t\t4) Delete account\n\t\t5) See all account holders\n\t\t6) Go Back\n\t\t6) Exit\n\n\tchoice: "))
#     if user_choice == 1:
#         withd_money()
#     elif user_choice == 2:
#         deposit_money()
#     elif user_choice == 3:
#         del_acc()
#     elif user_choice == 4:
#         all_acc_hold_list()
#     elif user_choice == 5:
#         start()
#     elif user_choice == 6:
#         file = open("data22.py", 'w')
#         file.write('acc_name = ' + str(acc_name) + '\n')
#         file.write('acc_pass = ' + str(acc_pass) + '\n')
#         file.write('acc_money = ' + str(acc_money) + '\n')
#         file.close()
#         exit()
#     else:
#         print("Wrong Input!!")
#         logged_in()
def logged_in():
    from data22 import acc_name
    from data22 import acc_pass
    from data22 import acc_money
    global acc_found, current_login
    a = acc_name.index(current_login)
    os.system('cls')
    print_text_slowly("\n\tLogged IN")
    print_text_slowly("\n\tAccount Name: " + acc_name[a])
    print_text_slowly("\tBalance: Rs. " + str(acc_money[a]))

    # Save the changes to the file

    file = open("data22.py", 'w')
    file.write('acc_name = ' + str(acc_name) + '\n')
    file.write('acc_pass = ' + str(acc_pass) + '\n')
    file.write('acc_money = ' + str(acc_money) + '\n')
    file.close()

    try:
        print_text_slowly("\n\tChoose option:\n\t\t1) Withdraw\n\t\t2) Deposit\n\t\t3) Close account\n\t\t4) See all account holders\n\t\t5) Go Back\n\t\t6) Exit\n\n\tchoice: ")
        move_cursor_to_line_and_column(15, 18)
        user_choice = int(input())
    except ValueError:
        print("Enter Correct Input :(")
        print_text_slowly("\n\tChoose option:\n\t\t1) Withdraw\n\t\t2) Deposit\n\t\t3) Close account\n\t\t4) See all account holders\n\t\t5) Go Back\n\t\t6) Exit\n\n\tchoice: ")
        move_cursor_to_line_and_column(15, 18)
        user_choice = int(input())

    if user_choice == 1:
        withd_money()
    elif user_choice == 2:
        deposit_money()
    elif user_choice == 3:
        del_acc()
    elif user_choice == 4:
        all_acc_hold_list()
    elif user_choice == 5:
        start()
    elif user_choice == 6:
        exit()
    else:
        print("Wrong Input!!")
        logged_in()

start()