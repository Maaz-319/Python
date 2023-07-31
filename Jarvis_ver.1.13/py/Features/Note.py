from talk import talk
from if_online import online
import datetime
from take_command import take_command

talk("What should i write, sir")
if online == True:
    note = take_command()
else:
    note = input("Message: ")
file = open('jarvis.txt', 'w')
talk("Sir, Should i include date and time")
if online == True:
    snfm = take_command()
else:
    print("Should I include date and time?")
    snfm = input("'yes' or 'no'")
if 'yes' in snfm or 'sure' in snfm:
    strTime = datetime.datetime.now().strftime('%I:%M %p')
    file.write(strTime)
    file.write(" :- ")
    file.write(note)
    talk("Message saved")
else:
    file.write(note)
    talk("Message saved")