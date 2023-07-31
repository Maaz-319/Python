# Calculator 2
import os
import keyboard
a = 0
b = 0
c = None 


def check():
    c = input("\n\tChoose:\n\t1) Add\n\t2) Subtract\n\t3) Divide\n\t4) Multiply\n\t5) Modulus\n\t6) Square\n\t7) Cube\n\tAnswer: ")
    if c == "1":
        add()
    elif c == "2":
        subtract()
    elif c == "3":
        divide()
    elif c == "4":
        mult()
    elif c == "5":
        mod()
    elif c == "6":
        square()
    elif c == "7":
        Cube()
    else :
        print("\n\n\tPlease Enter a valid Choice\n\n\t")
        check()



def add():
    global a
    global b
    try:
        a = float(input("\n\n\tEnter first Number: "))
        b = float(input("\n\n\tEnter second Number: "))
        print ("\n\n\tAnswer: ", a + b)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        add()
    again()
    


def subtract():
    global a
    global b
    try:
        a = float(input("\n\n\tEnter first Number: "))
        b = float(input("\n\n\tEnter second Number: "))
        print ("\n\n\tAnswer: ", a - b)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        subtract()
    again()


def divide():
    global a
    global b
    try:
        a = float(input("\n\n\tEnter first Number: "))
        b = float(input("\n\n\tEnter second Number: "))
        print ("\n\n\tAnswer: ", a / b)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        divide()
    again()


def mult():
    global a
    global b
    try:
        a = float(input("\n\n\tEnter first Number: "))
        b = float(input("\n\n\tEnter second Number: "))
        print ("\n\n\tAnswer: ", a * b)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        mult()
    again()


def mod():
    global a
    global b
    try:
        a = float(input("\n\n\tEnter first Number: "))
        b = float(input("\n\n\tEnter second Number: "))
        print ("\n\n\tAnswer: ", a % b)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        mod()
    again()


def square():
    global a
    global b
    try:
        a = float(input("\n\n\tEnter first Number: "))
        print ("\n\n\tAnswer: ", a * a)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        square()
    again()


def Cube():
    try:
        a = float(input("\n\n\tEnter first Number: "))
        result = a * a * a
        print ("\n\n\tAnswer: ", result)
        input("\n\tPress Enter to continue......")
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        square()
    again()


def again():
    user = input("\n\n\tEnter 'a' to run again and Press 'e' to exit: ")
    if user == 'a':
        check()
    elif user == 'e':
        exit()
    else:
        again()
check()