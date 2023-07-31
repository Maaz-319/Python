import time, getpass, os

secret_key = "Maaz"
password = getpass.getpass(prompt='Password: ', stream=None)
if password != secret_key:
    print("\n\tWrong password!!!!")
    time.sleep(2)
    exit()


os.system('cls')
print("\n\t\t\tWelcom to Bank Management System.\n")
print("********************************************************************************")

acc_found = False

def crt_acc():
    global name, money, pin
    from test2_data import acc_name
    from test2_data import acc_pass
    from test2_data import acc_money
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
    file = open("test2_data.py", 'w')
    file.write('acc_name = ' + str(acc_name) + '\n')
    file.write('acc_pass = ' + str(acc_pass) + '\n')
    file.write('acc_money = ' + str(acc_money) + '\n')
    file.close()
    from test2_data import acc_name
    from test2_data import acc_pass
    from test2_data import acc_money
    print("\n\tNew Account Info:\n")
    print("\n\t\tYour account name is : ", acc_name[a])
    print("\n\t\tYou have " ,acc_money[a],"Rs in your account.")
    time.sleep(3)
    choice()


def del_acc():
    from test2_data import acc_name
    from test2_data import acc_pass
    from test2_data import acc_money
    global acc_found

    name = str(input("\nEnter account name you want to delete: "))

    if name not in acc_name:
        print("No account found!")
        del_acc()
    if name in acc_name:
        pin = getpass.getpass("Enter account pin: ")
        a = acc_name.index(name)
        pass1 = acc_pass[a]
        money = acc_money[a]
        if pin == acc_pass[a]:
            acc_name.remove(name)
            acc_pass.remove(pass1)
            acc_money.remove(money)
            print("\nAccount was deleted!")
            file = open("test2_data.py", 'w')
            file.write('acc_name = ' + str(acc_name) + '\n')
            file.write('acc_pass = ' + str(acc_pass) + '\n')
            file.write('acc_money = ' + str(acc_money) + '\n')
            file.close()
        else:
            print("Wrong password!")
            del_acc()
    
    choice()



def withd_money():
    from test2_data import acc_name
    from test2_data import acc_pass
    from test2_data import acc_money
    global acc_found
    name = str(input("\nEnter account name to withdraw money: "))

    if name in acc_name:
        global passo
        acc_found = True
        pin = getpass.getpass("Enter account pin: ")
        a = acc_name.index(name)
        if pin == acc_pass[a]:
            money = int(input("Enter amount of money you want to withdraw: "))
        elif pin != acc_pass[a]:
            print("wrong Password!")
            time.sleep(3)
            withd_money()
        
        if money < 0:
            print("\nIncorrect amount!")
            time.sleep(2)
            choice()
        if money < acc_money[a]:
            file = open("test2_data.py", 'w')
            acc_money[a] = acc_money[a] - money
            print("\n\tThere are ", acc_money[a], "Rs left in your account.")
            file.write('acc_name = ' + str(acc_name) + '\n')
            file.write('acc_pass = ' + str(acc_pass) + '\n')
            file.write('acc_money = ' + str(acc_money) + '\n')
            file.close()
        else:
            print("\n\tNot enough money in account :(!")
            time.sleep(2)
            choice()
    
    if not(acc_found):
        print("No account found! Try again!")
        withd_money()
    time.sleep(3)
    choice()
        
def deposit_money():
    from test2_data import acc_name
    from test2_data import acc_pass
    from test2_data import acc_money
    global acc_found
    global name
    name = str(input("\nEnter account name to deposit money: "))

    if name in acc_name:
         
        acc_found = True
        a = acc_name.index(name)
        pin = getpass.getpass("Enter your account pin: ")
        if pin == acc_pass[a]:    
            money = int(input("Enter amount of money you want to deposit: "))
            acc_money[a] = acc_money[a] + money
            print("\n\tThere are ", acc_money[a], "Rs in your account.")
            file = open("test2_data.py", 'w')
            file.write('acc_name = ' + str(acc_name) + '\n')
            file.write('acc_pass = ' + str(acc_pass) + '\n')
            file.write('acc_money = ' + str(acc_money) + '\n')
            file.close()
        else:
            print("Wrong account pin!")
            time.sleep(2)
            os.system('cls')
            deposit_money()

    if acc_found == False:
        print("No account found! Try again!")
        deposit_money()
    time.sleep(3)
    choice()

def all_acc_hold_list():
    from test2_data import acc_name
    print("\n")
    print(str(acc_name))
    time.sleep(3)
    choice()

def choice():
    try:
        #user_choice = int(input("\n\tChoose option:\n\t\t1) Create Account\n\t\t2) Delete Account\n\t\t3) Withdraw\n\t\t4) Deposit\n\tChoice: "))
        user_choice = int(input("\n\tChoose option:\n\n\t\t1) Create Account\n\t\t2) Withdraw\n\t\t3) Deposit\n\t\t4) Delete account\n\t\t5) See all account holders\n\t\t6) Exit\n\n\tchoice: "))
    except ValueError:
        print("Enter Correct Input :(")
        #user_choice = int(input("\n\tChoose option:\n\t\t1) Create Account\n\t\t2) Delete Account\n\t\t3) Withdraw\n\t\t4) Deposit\n\tChoice: "))
        user_choice = user_choice = int(input("\n\tChoose option:\n\n\t\t1) Create Account\n\t\t2) Withdraw\n\t\t3) Deposit\n\t\t4) Delete account\n\t\t5) See all account holders\n\t\t6) Exit\n\n\tchoice: "))
    if user_choice == 1:
        crt_acc()
    elif user_choice == 2:
        withd_money()
    elif user_choice == 3:
        deposit_money()
    elif user_choice == 4:
        del_acc()
    elif user_choice == 5:
        all_acc_hold_list()
    elif user_choice == 6:
        exit()
    else:
        print("Wrong Input!!")
        choice()

choice()
input()
