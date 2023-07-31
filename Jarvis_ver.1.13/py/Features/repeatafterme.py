from talk import talk
from if_online import online
from take_command import take_command

if online == True:
            talk("Ok speak now.!")
            command = take_command()
            talk("You said.")
            talk(command)
else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
