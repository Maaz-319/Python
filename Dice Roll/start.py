import random
import keyboard
import os
def whole():
    input("Press enter to roll the dice")
    a = random.randint(1, 6)
    print("You number is " , a)
    again()

def again():
    print("\n\n\tPress 'a' to run again and Press 'e' to exit\n\tReading key.....: ")
    if keyboard.read_key() == "a":
        whole()
    elif keyboard.read_key() == "e":
        os.system(exit)
    else:
        again()

def Runfunc():
    whole()
    

Runfunc()