a = None
b = None
def whole():
    global a
    global b
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter last number number: "))
        calc()
    except:
        print("\n\tEnter a valid value\n")
        whole()
    

def calc():
    global a
    global b
    while a < b:
        mod = a % 2
        if mod == 0:
            print("\n", a)
            a += 1
        else:
            a += 1
whole()
input()