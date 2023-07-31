import webbrowser
import math
Choice = input("\nEnter choice Number:\n\n\t1) Square\n\n\t2) Cube\n\n\t3) Square Root\n\n\t4)Cube Root\nChoice:  ")


def square():
    num = float(input("\nEnter the Number: "))
    num = num * num
    print(num)
    input("\nThank you for using Made By Maaz \n")
    webbrowser.open('https://donotcheck319.blogspot.com')


def cube():
    NUM = float(input("\nEnter the Number: "))
    NUM = NUM * NUM * NUM
    print(NUM)
    input("\nThank you for using Made By Maaz \n")
    webbrowser.open('https://donotcheck319.blogspot.com')


def square_root():
    NUM = float(input("\nEnter the Number: "))
    a = math.sqrt(NUM)
    print("\n\n\tAnswer: ", a)
    input('')
    webbrowser.open('https://donotcheck319.blogspot.com')


def cube_root():
    NUM = float(input("\nEnter the Number: "))
    a = NUM**(1./3.)
    print("\n\n\tAnswer: ", a)
    input('')
    webbrowser.open('https://donotcheck319.blogspot.com')


def choice_selector():
    if Choice == '1':
        print(square())
    elif Choice == '2':
        print(cube())
    elif Choice == '3':
        print(square_root())
    elif Choice == '4':
        print(cube_root())
    else:
        print("\nPlease Enter valid Choice\n ")
        choice_selector()


print(choice_selector())
