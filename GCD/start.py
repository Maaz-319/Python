import os
def all():
    try:
        num_1 = int(input("\n\tEnter first number: "))
        num_2 = int(input("\n\tEnter second number: "))

        i = 2
        while i <= num_1 and i <= num_2:
            #r_1 = num_1 / i
            #r_2 = num_2 / i
            if num_1 % i == 0 and num_2 % i == 0:
                a = i
            i += 1
        print("\n\n\tGCD of ", num_1, " and ", num_2, "is   '", a, "'.")
        input()
    except:
        print("\n\n\t!Error!")
        input("\n\n\tPress Enter to reboot!")
        os.system('cls')
        all()
all()