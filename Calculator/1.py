import os
import keyboard
import time
a = 0
b = 0
c = None 


def getinput():
    global a
    global b
    global c
    try:
        a = float(input("\n\n\tEnter first Number: "))
        c = input("\n\n\tEnter operator +, -, *, /, %(mod): ")
        b = float(input("\n\n\tEnter second Number: "))
    except:
        print("\n\n\tEnter a valid choice\n\n\t")
        RunFunc()


def check():
    global a
    global b
    if c == "+":
        add()
    elif c == "-":
        subtract()
    elif c == "/":
        divide()
    elif c == "*":
        mult()
    elif c == "%":
        mod()
    else :
        print("\n\n\tPlease Enter a valid Choice\n\n\t")
        RunFunc()

# Prints a simple answer.
def add():
    global a
    global b
    print ("\n\n\tAnswer: ", a + b)
    input("\n\tPress Enter to continue......")


# Subtract the given number from the current number.
def subtract():
    global a
    global b
    print ("\n\n\tAnswer: ", a - b)
    input("\n\tPress Enter to continue......")


def divide():
    global a
    global b
    try:
        print ("\n\n\tAnswer: ", a/ b)
        input("\n\tPress Enter to continue......")
    except ZeroDivisionError:
        print("Can't Divide by zero\n\nRestarting program...\n\n")
        time.sleep(3)
        RunFunc()


def mult():
    global a
    global b
    print ("\n\n\tAnswer: ", a * b)
    input("\n\tPress Enter to continue......")


def mod():
    global a
    global b
    print ("\n\n\tAnswer: ", a % b)
    input("\n\tPress Enter to continue......")


def RunFunc():
    getinput()
    check()
    again()


def again():
    print("\n\n\tPress 'a' to run again and Press 'e' to exit\n\tReading key.....: ")
    if keyboard.read_key() == 'a':
        RunFunc()
    elif keyboard.read_key() == 'e':
        exit()
    else:
        again()
RunFunc()
