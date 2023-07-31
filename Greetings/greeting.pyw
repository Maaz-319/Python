"""from actdeact import run
if run == False:
    exit()
elif run == True:
    import pyttsx3, datetime, subprocess
    from talk import talk

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        talk("Good Morning Maaz! Welcome back")
    elif hour > 12 and hour < 18:
        talk("Good afternoon Maaz! Welcome back")
    else:
        talk("Good evening Maaz! Welcome back")

    file = open('tasks.txt', 'r')
    data = file.read()
    if data == '':
        talk('No due tasks')
        exit()
    else:
        talk('There are some tasks that you might want to check. Here!')
        subprocess.Popen(["C:/Windows/System32/notepad.exe", "tasks.txt"])
        talk('Take a look')
    exit()
else:
    exit()"""






import random
import datetime
import subprocess
import pyttsx3
from actdeact import run
from talk import talk
import datetime
from datetime import date

if not run:
    exit()
else:
    temp = date.today()
    hour = datetime.datetime.now().hour
    time = datetime.datetime.now().strftime('%I:%M %p')
    today_date = temp.strftime("%d/%m/%Y")
    file = open("log.txt", "a")
    file.write("\nDate:"+str(today_date)+"\nTime:"+str(time)+"\n")
    file.close()

    if 0 <= hour < 12:
        talk("Good Morning Maaz!")
    elif 12 <= hour < 18:
        talk("Good afternoon Maaz!")
    else:
        talk("Good evening Maaz!")

    greetings = [
        "Welcome back. I hope you have a fantastic day!",
        "Welcome back. I hope you're having a productive day!",
        "Welcome back. I hope you had a great day!",
        "Welcome back. It's good to see you again. Ready to conquer the day?",
        "Welcome back. Wishing you a day full of accomplishments!",
        "Welcome back. I hope your day is off to a great start!",
        "Welcome back. Let's make today even better than yesterday!",
        "Welcome back. Sir, Get ready to make some magic happen!",
        "Welcome back. Ahoy, Sir! Time to continue your amazing journey!",
        "Welcome back. Sir, it's a pleasure to have you here again. Let's make the most out of it."
    ]

    selected_greeting = random.choice(greetings)
    talk(selected_greeting)

    with open('tasks.txt', 'r') as file:
        data = file.read()

    if not data:
        talk('No pending tasks found. Enjoy your free time!')
        exit()
    else:
        talk('Ok first thing first, You have some tasks that you might want to check. Let me open them for you!')
        subprocess.Popen(["C:/Windows/System32/notepad.exe", "tasks.txt"])
        talk('Take a look and tackle those tasks with enthusiasm!')

        quotes = [
        "The only way to do great work is to love what you do.",
        "Believe you can, and you're halfway there.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "In the middle of difficulty lies opportunity.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Don't watch the clock; do what it does. Keep going.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Hardships often prepare ordinary people for an extraordinary destiny.",
        "Every day is a new beginning. Take a deep breath and start again.",
        "The only person you should try to be better than is the person you were yesterday."
        ]

        talk("As someone once said")
        selected_quote = random.choice(quotes)
        talk(selected_quote)
    exit()

