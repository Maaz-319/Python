def userinp():
    global user

    try:
        user = str(input("Enter Numbers: "))
    except ValueError:
        userinp()


def Conversion():
    global digits

    digits = {

        "1":"One",
        "2":"Two",
        "3":"Three",
        "4":"Four",
        "5":"Five",
        "6":"Six",
        "7":"Seven",
        "8":"Eight",
        "9":"Nine",
        "0":"Zero"
    }
global output

def ending():
    output = ""
    for ch in user:
        output += digits.get(ch, "Not a number.") + " "
    print(output)



userinp()
Conversion()
ending()
input()