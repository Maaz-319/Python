try:
    from data import names
    from data import phone
except:
    file = open('data.py', 'w')
    file.write("names = []")
    file.write("\nphone = []")
    file.close()
import os


def search():
    from data import names
    from data import phone
    user_name = str(input("Enter name you want to Search: "))
    if user_name in names:
        index = names.index(user_name)
        print("Your Contact:-")
        print("\n\n\tName: " + str(user_name))
        print("\tPhone# 03" + str(phone[index]))
        input("Enter to continue")
        os.system('cls')
        user_choiice()
    else:
        print("\nNot Found!")
        input("\nEnter to continue")
        os.system('cls')
        user_choiice()



def save():
    from data import names
    from data import phone
    name = str(input("Enter name of contact: "))
    phone_no = str(input("Enter Phone# 03"))
    length = len(phone_no)
    while length < 9:
        os.system('cls')
        phone_no = str(input("Enter Valid Phone Number# 03"))
        length = len(phone_no)
    names.append(name)
    phone.append(phone_no)
    file = open('data.py', 'w')
    file.write("names = " + str(names))
    file.write("\nphone = " + str(phone))
    file.close()
    print("Your Contact is saved succesfully.")
    print("\nName = " + str(name))
    print("Phone# 03" + str(phone_no))
    input("\nPress Enter to continue")
    os.system('cls')
    user_choiice()


def user_choiice():
    try:
        global user_choice
        user_choice = str(input("Enter 's' to search a Number and Enter 'g' to save a Number. Enter 'e' to Exit: "))
    except ValueError:
        os.system('cls')
        user_choiice()
    if user_choice == 'g':
        save()
    elif user_choice == 's':
        search()
    elif user_choice == 'e':
        exit()
    else:
        os.system('cls')
        user_choiice()

user_choiice()
