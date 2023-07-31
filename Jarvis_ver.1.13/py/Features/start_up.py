import subprocess
import time
from take_command import *
from talk import talk
from if_online import online
import webbrowser
import os
import datetime
import speech_recognition as maaz
from datetime import date
import pyautogui

name_of_user = ""
age_of_user = ""


def startup():
    global offline_command
    os.system('cls')
    print("Initializing Jarvis.....")
    time.sleep(0.5)
    print("Done.👍")
    talk("Initializing Jarvis")
    print("Starting all systems applications.....")
    time.sleep(0.5)
    print("Caliberating and examining all the core processors.....")
    time.sleep(0.5)
    print("Checking the internet connection")
    time.sleep(0.5)
    talk("Checking internet connection")
    print("Done.👍")
    if online == True:
        print("You are online 👍")
        talk("Sir! You are online")
    else:
        print("You are offline 👎:-(")
        talk("Sir! You are offline")
        talk("Internet features are not available")
        talk("Enter your command via text input")
        while True:
            os.system('cls')
            offline_command = str(input("Enter your Query: "))
            run_jarvis()
    print(
        "--------------------------------------------------------------------------------------------------------------")
    print("                                     Jarvis_ver.1.13")
    print("                                           by Maaz")
    print(
        "--------------------------------------------------------------------------------------------------------------")
    print("Jarvis ready now.")
    talk("Jarvis ready now.")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        talk("Good Morning Maaz!")
    elif hour > 12 and hour < 18:
        talk("Good afternoon Maaz!")
    else:
        talk("Good evening Maaz!")
    talk("How may I help you?")
    while True:
        run_jarvis()


def run_jarvis():
    global source, online, engine, voices, command
    if online == True:
        command = take_command()
    else:
        command = offline_command

    print("You: " + command)

    if "how are you" in command:
        print("\n\nJarvis: Iam good, Thanks for asking")
        talk("Iam good, Thanks for asking")
    elif 'repeat after me' in command or 'speak after me' in command:
        os.system("repeatafterme.py")
    elif 'know' in command and 'my name' in command:
        global name_of_user
        try:
            file = open('data\\Name.txt', 'r')
        except:
            file = open('data\\Name.txt', 'w')
            file.write('')
        name_of_user = file.read()
        file.close()
        if name_of_user == '':
            print('I don\'t know your name yet. Say \'Yes\' if you want to tell me.')
            talk("I don\'t know your name yet. Say Yes, if you want to tell me.")
            if online == True:
                command = take_command()
            else:
                command = offline_command
            if 'yes' in command or 'sure' in command:
                print("What should I call you?")
                talk("What should I call you?")
                if online == True:
                    command = take_command()
                else:
                    command = offline_command
                name_of_user = str(command)
                print("Ok! I will call you " + name_of_user)
                talk("Ok! I will call you " + name_of_user)
                file = open('data\\Name.txt', 'w')
                file.write(name_of_user)
                file.close()
            else:
                pass
        else:
            print("You are " + name_of_user)
            talk("Your name is " + name_of_user)
    elif 'my' in command and 'age' in command:
        global age_of_user
        try:
            file = open('data\\Age.txt', 'r')
        except:
            file = open('data\\Age.txt', 'w')
            file.write('')
        age_of_user = file.read()
        file.close()
        if age_of_user == '':
            print('I don\'t know how old are you. Say \'Yes\' if you want to tell me.')
            talk("I don\'t know how old are you. Say \'Yes\' if you want to tell me.")
            if online == True:
                command = take_command()
            else:
                command = offline_command
            if 'yes' in command or 'sure' in command:
                print("How old are you?")
                talk("How old are you?")
                if online == True:
                    command = take_command()
                else:
                    command = offline_command
                age_of_user = str(command)
                print("Ok! You are " + age_of_user + " Years old.")
                talk("Ok! You are " + age_of_user)
                file = open('data\\Age.txt', 'w')
                file.write(age_of_user)
                file.close()
            else:
                pass
        else:
            print("You are " + age_of_user + " Years old.")
            talk("You are " + age_of_user)
    elif 'hello' in command or 'Hi' in command:
        print("\n\nJarvis: Hi! nice to meet you")
        talk("Hi! nice to meet you")
    elif 'thanks' in command or 'thank' in command:
        print("You are welcome!")
        talk("You are welcome Sir!")
    elif 'change' in command and 'your name' in command:
        print("\n\nJarvis: I am Jarvis, and I like my name.")
        talk("I am Jarvis, and I like my name")
    elif 'who are you' in command or 'your name' in command:
        print("\n\nJarvis: I am Jarvis\nA voice assistant")
        talk("I am Jarvis\nA voice assistant")
    elif 'what is your name' in command:
        talk("I am Jarvis, nice to meet you.")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("\n\nJarvis: " + time)
        talk("It's " + time)
    elif 'date' in command:
        temp = date.today()
        today_date = temp.strftime("%d/%m/%Y")
        print("\n\nJarvis: " + today_date)
        talk("It's " + today_date)
    elif 'search' in command:
        os.system("search_talk.py")
    elif 'joke' in command:
        os.system("tell_joke.py")
    elif 'bye' in command:
        print("\n\nok! see you later")
        talk("ok! see you later Sir")
        exit()
    elif 'exit' in command or 'Exit' in command or 'go away' in command or 'get lost' in command:
        print("\n\nok! see you later")
        talk("ok! see you later Sir")
        exit()
    elif 'who made you' in command or 'who created you' in command:
        print(
            "\n\nI was made by the greatest hero! the world has ever seen in the history of mankind. His name is Sir Maaz Bin Asif")
        talk(
            "I was made by the greatest hero! the world has ever seen in the history of mankind. His name is Sir Maaz Bin Asif")
    elif 'Chrome' in command or 'chrome' in command:
        if online == True:
            print("\n\nOpening Google Chrome")
            talk("Sir! Launching Google Chrome")
            webbrowser.open('https://www.google.com')
        else:
            print("Launching chrome...")
            talk("Launching chrome but Internet is not available.")
            webbrowser.open('https://www.google.com')
    elif 'music' in command:
        talk("Ok Sir! Asking Windows to play Music.")
        print("\n\nPlaying Music.")
        os.system("music.py")
    elif 'open' in command and 'youtube' in command:
        if online == True:
            talk("Opeing youtube")
            webbrowser.open('https://youtube.com/')
        else:
            print("opening youtube...")
            talk("opening youtube but internet is not available")
            webbrowser.open('https:"//www.youtube.com/')
    elif 'news' in command:
        if online == True:
            talk("fetching latest headlines. Region! Pakistan")
            webbrowser.open('https://dunyanews.tv/')
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'screenshot' in command:
        """print("\n\nTaking Screenshot")
        talk("Taking screenshot")
        img = pyautogui.screenshot()
        img.save(r"C:/Users/Dell/Desktop/Jarvis_capture.png")
        talk("screenshot successfully saved to desktop Sir.")"""
        os.system("screenshot.py")
    elif 'Naat' in command:
        """talk("Here you go Sir!")
        music_dir = "D:\\Naat"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[1]))"""
        os.system("Naat.py")
    elif 'lock' in command and 'device' in command:
        """talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
        talk("locked")
        input("Enter to continue.")"""
        os.system("lock_device.py")
    elif "camera" in command or "take a photo" in command:
        """talk("capturing")
        ec.capture(0, "Jarvis_Capture_3.2 ", "jarvis_capture.png ")
        talk("Done") """
        os.system("take_photo.py")
    elif "write a note" in command:
        os.system('Note.py')
    elif "release" in command or 'version' in command:
        print("This is jarvis_1.13 released.")
        talk("This is jarvis 1 point 1 3.")
    elif "weather" in command:
        os.system('weather.py')
    elif 'change your voice' in command:
        global voice_of_jarvis, engine, voices
        if voice_of_jarvis != "Changed":
            engine.setProperty('voice', voices[1].id)
            voice_of_jarvis = "Changed"
            talk("Ok! this will be my new voice.")
        else:
            engine.setProperty('voice', voices[0].id)
            voice_of_jarvis = "Not Changed"
            talk("Ok! this will be my new voice.")
    elif 'wait' in command:
        talk("Press Enter when ever you are ready")
        input()
    elif 'roblox' in command:
        talk('Opening Roblox! now')
        webbrowser.open('https:www.roblox.com/')
        talk('Press Enter to continue Jarvis')
        input()
    elif 'I am going outside' in command or 'I will be right back' in command or 'I\'ll be right back' in command:
        os.system("lock_device.py")
    elif 'shutdown' in command:
        os.system('shutdown /s /t 1')
    elif 'I want to do edit program' in command or 'edit code' in command:
        os.system('edit_code.py')
        input('Press Enter to continue')
    elif 'I want to do programming' in command:
        os.system('do_programming.py')
        input('Press Enter to continue')
    elif 'I want to do some python' in command or 'I want to do some python Programming' in command or 'python programming' in command:
        os.system('do_python_programming.py')
        input('Press Enter to continue')
    elif 'open' in command and 'calculator' in command:
        os.system('open_calc.py')
        input('Press Enter to continue')
    elif ('open' in command and 'Notepad' in command) or ('open' in command and 'editor' in command):
        os.system('open_notepad.py')
        input('Press Enter to continue')
    elif 'I want to watch Doraemon' in command or 'play doraemon' in command or 'play movie' in command or 'play movies' in command:
        os.system('play_movies.py')
        input('Press Enter to continue')
    elif 'tell me the truth' in command:
        talk("Mooseb is very Idiot")
    elif ('open' in command and 'edge' in command) or ('open' in command and 'Edge'):
        os.system('open_edge.py')
    elif 'what' in command and 'you do' in command:
        try:
            file = open('list.txt', 'r')
            talk("all actions that I can perform are saved in a file")
            subprocess.Popen(["C:/Windows/System32/notepad.exe", "list.txt"])
            talk("Here! Take a look at it")
            input('Enter to continue......')
            file.close()
        except:
            print("One moment.....")
            talk("One moment")
            file = open('backup\\command_backup.txt', 'r')
            data = file.read()
            file2 = open('list.txt', 'w')
            file2.write(data)
            file.close()
            file2.close()
            talk("all actions that I can perform are saved in a file")
            subprocess.Popen(["C:/Windows/System32/notepad.exe", "list.txt"])
            talk("Here! Take a look at it")
            input('Enter to continue......')
    elif 'what' in command and 'fox say' in command:
        print("Fra-ca ca-ca ca-ca ca-ca cow")
        talk("Fracacacacacacaca cow")
    elif 'change' in command and 'wallpaper' in command:
        print('Changing Wallpaper......')
        os.system('change_wallpaper.py')
    elif 'locate' in command:
        command = command.replace('locate ', '')
        os.system('locate.py')
    elif 'wallpaper' in command:
        print('If you want me to change wallpaper, say "Change wallpaper"')
        talk('If you want me to change wallpaper, say "Change wallpaper"')
    elif 'volume up' in command or 'unmute' in command:
        pyautogui.press("volumeup")
    elif 'volume down' in command:
        pyautogui.press("volumedown")
    elif 'mute' in command or 'shut up' in command:
        pyautogui.press("volumemute")
        print('Muted !')
    elif 'photoshop' in command or 'edit photo' in command or 'Edit photo' in command:
        os.system('photoshop.py')
    elif 'I am unknown person 1442 598' in command:
        os.system('pass.py')
    elif command == '':
        talk("Can you say that again")
    elif 'what' in command and 'my email' in command:
        file = open('data\\Email.txt', 'r')
        talk(file.read())
        file.close()
    else:
        print("\n\nAnswering this is beyond my capabilities.")
        talk("Sorry! Answering this is beyond my capabilities.")


startup()

"""elif 'change' in command and 'my name' in command:
        print("What should I call you?")
        talk("What should I call you?")
        if online == True:
            with maaz.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=1)
                print("Speak now")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
        else:
            command = str(input("Enter your Name: "))
        name_of_user = str(command)
        print("Ok! I will call you " + name_of_user)
        talk("Ok! I will call you " + name_of_user)"""
