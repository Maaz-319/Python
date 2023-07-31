from talk import talk
from if_online import online
from take_command import take_command
import wikipedia
talk("What do you want to search for?")
print("What do you want to search for?")
command = str(take_command())
if online == True:
            search = command.replace('who is','')
            result = wikipedia.summary(search, 1)
            print("\n\n" + result)
            talk(result)
else:
    print("Internet is not available. Try again later.")
    talk("Internet is not available. Try again later.")
