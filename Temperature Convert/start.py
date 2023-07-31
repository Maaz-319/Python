import time
import webbrowser
print("Welcome to Maaz Temperature Converter\n")
Choice = input("Please select\n1) Fahrenheit to celsius\n2) Celsius to fahrenheit\n3) Celsius to kelvin\n"
               "4) Kelvin to celsius\nEnter Choice Number: ")


def ftoc():
    a = float(input("Enter Number in fahrenheit: "))
    b = (a-32) * 5/9
    print("   Answer: ", b)
    print("\nNow you will be redirected to my website")
    time.sleep(5)
    webbrowser.open('https://donotcheck319.blogspot.com')


def ctof():
    a = float(input("Enter Number in Celsius: "))
    b = (a * 9/5) + 32
    print("   Answer: ", b)
    print("\nNow you will be redirected to my website")
    time.sleep(5)
    webbrowser.open('https://donotcheck319.blogspot.com')


def ktoc():
    a = a = float(input("Enter Number in Kelvin: "))
    b = a - 273.15
    print("Answer: ", b)
    print("\nNow you will be redirected to my website")
    time.sleep(5)
    webbrowser.open('https://donotcheck319.blogspot.com')


def ctok():
    a = a = float(input("Enter Number in Celsius: "))
    b = a + 273.15
    print("Answer: ", b)
    print("\nNow you will be redirected to my website")
    time.sleep(5)
    webbrowser.open('https://donotcheck319.blogspot.com')


if Choice == '1':
    ftoc()
elif Choice == '2':
    ctof()
elif Choice == '3':
    ctok()
elif Choice == '4':
    ktoc()
else:
    input("invalid choice\nNow you will be redirected to my website")
    time.sleep(5)
    webbrowser.open('https://donotcheck319.blogspot.com')
