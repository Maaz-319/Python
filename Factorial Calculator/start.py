import math
import os


def whole():
    try:
        user = int(input("Enter NUM: "))
        print("\n\n\tAnswer: ", math.factorial(user), "\n")
        again()
    except ValueError:
        print("Please enter a number")
        whole()
    except OverflowError:
        print("Enter a lower number")
        whole()


def again():
    user = input("Choose: \n\t1) Again\n\t2) Exit\n\tAnswer: ")
    if user == '1':
        whole()
    elif user == '2':
        os.system(exit())
    else:
        again()


print(whole())
