import os
import time
import winsound
print("Welcome to Maaz Timer\n")

time.sleep(2)


def whole():
    a = float(input("Enter seconds for timer(only numbers 1,2,3.... : "))

    print("Timer Started!\n")

    while a >= 1:
        print(a, " seconds remaining")
        time.sleep(1)
        a = a-1
        # os.system('cls')
    i = "MaazBinAsif"
    for x in i:
        print("Timer Finished!!\a")
        time.sleep(0.5)
    input("")
    print(again())


def again():
    user = input("Choose: \n\t1) Again\n\t2) Exit\n\tAnswer: ")
    if user == '1':
        whole()
    elif user == '2':
        os.system(exit())
    else:
        again()


print(whole())