import speech_recognition as maaz
import pyttsx3
import datetime
import wikipedia
import pyjokes
import requests
from datetime import date
import webbrowser
import pyautogui
import os
import ctypes
from ecapture import ecapture as ec
import python_weather
import asyncio
import time

listener = maaz.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voice_of_jarvis = "Not Changed"
engine. setProperty("rate", 170)
online = False


async def getweather():
    
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # fetch a weather forecast from a city
    weather = await client.get("Lahore")
    global type_of_weather, temperature, humidity
    # returns the current day's forecast temperature (int)
    type_of_weather = weather.current.description
    temperature = int((int(weather.current.temperature) - 32) * (5/9))
    humidity = weather.current.humidity

    # get the weather forecast for a few days
"""    for forecast in weather.forecasts:
      #print(forecast.date, forecast.astronomy)
        for hourly in forecast.hourly:
            print(f' --> {hourly!r}')"""



def talk(text):
    engine.say(text)
    engine.runAndWait()

def startup():
    global online
    print("Initializing Jarvis.....")
    time.sleep(0.5)
    print("Done.👍")
    talk("Initializing Jarvis")
    print("Starting all systems applications.....")
    time.sleep(0.5)
    print("Done.👍")
    talk("Starting systems applications")
    print("Installing and checking all drivers.....")
    time.sleep(0.5)
    print("Done.👍")
    talk("checking all drivers")
    print("Caliberating and examining all the core processors.....")
    time.sleep(0.5)
    print("Done.👍")
    talk("Caliberating core processors")
    print("Checking the internet connection")
    time.sleep(0.5)
    print("Done.👍")
    talk("Checking internet connection")
    try:
        requests.post(url='https://www.google.com')
        print("You are online 👍")
        talk("Sir! You are online")
    except:
        print("You are offline 👎:-(")
        talk("Sir! You are offline")
        talk("Internet features are not available")
        talk("Enter your command via text input")
        while True:
            global offline_command
            offline_command = str(input("Enter your Query: "))
            run_jarvis()

    print("All drivers are up and running")
    talk("All drivers are up and running")
    print("All systems have been activated")
    talk("All systems have been activated")
    print("Jarvis ready now.")
    talk("Jarvis ready now.")
    online = True
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        talk("Good Morning")
    elif hour>12 and hour<18:
        talk("Good afternoon Maaz!")
    else:
        talk("Good evening Maaz!")
    talk("How may I help you?")
    while True:
        run_jarvis()
def take_command():
    try:
        with maaz.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print("Rocognizing....")
            if 'jarvis'in command:
                command = command.replace('jarvis','')
            elif 'Jarvis'in command:
                command = command.replace('Jarvis','')
    except:
        print("\nSorry! can you say that again.")
        talk("\nSorry! can you say that again.")
        take_command()
    return command

def run_jarvis():
    global source, offline_command, online
    if online == True:
        command = take_command()
    else:
        command = offline_command

    print("You: " + command)

    if 'hello' in command:
        print("\n\nJarvis: Hi! nice to meet you")
        talk("Hi! nice to meet you")
    elif 'thanks' in command or 'thank' in command:
        print("You are welcome!")
        talk("You are welcome!")
    elif 'hi' in command:
        print("\n\nJarvis: Hi! nice to meet you")
        talk("Hi! nice to meet you")
    elif 'who are you' in command:
        print("\n\nJarvis: I am Jarvis\nA voice assistant")
        talk("I am Jarvis\nA voice assistant")
    elif 'how are you' in command:
        talk("I am fine, Thank you Sir.")
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
    elif 'who is ' in command:
        if online == True:
            person = command.replace('who is','')
            result = wikipedia.summary(person, 1)
            print("\n\n" + result)
            talk(result)
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'what is' in command:
        if online == True:    
            thing = command.replace('what is','')
            result = wikipedia.summary(thing, 1)
            print("\n\n" + result)
            talk(result)
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'what is a' in command:
        if online == True:
            thing = command.replace('what is a','')
            result = wikipedia.summary(thing, 1)
            print("\n\n" + result)
            talk(result)
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'joke' in command:
        joke = (pyjokes.get_joke())
        print("\n\n" + joke)
        talk("OK." + joke)
    elif 'bye' in command:
        print("\n\nok! see you later")
        talk("ok! see you later Sir")
        exit()
    elif 'go away' in command:
        print("\n\nok! see you later!")
        talk("ok Sir! Go to hell you idiot.")
        exit()
    elif 'get lost' in command:
        print("\n\nok! see you later!")
        talk("ok Sir! Go to hell you idiot.")
        exit()
    elif 'who made you' in command:
        print("\n\nI was made by the greatest hero! the world has ever seen in the history of mankind. His name is Sir Maaz Bin Asif")
        talk("I was made by the greatest hero! the world has ever seen in the history of mankind. His name is Sir Maaz Bin Asif")
    elif 'who created you' in command:
        print("\n\nI was made by the greatest hero! the world has ever seen in the history of mankind. His name is Sir Maaz Bin Asif")
        talk("I was made by the greatest hero! the world has ever seen in the history of mankind. His name is Sir Maaz Bin Asif")
    elif 'Chrome' in command:
        if online == True:
            print("\n\nOpening Google Chrome")
            talk("Sir! Launching Google Chrome")
            webbrowser.open('https://www.google.com')
        else:
            print("Launching chrome...")
            talk("Launching chrome but Internet is not available.")
            webbrowser.open('https://www.google.com')
    elif 'chrome' in command:
        if online == True:
            print("\n\nOpening Google Chrome")
            talk("Sir! Launching Google Chrome")
            webbrowser.open('https://www.google.com')
        else:
            print("Launching chrome...")
            talk("Launching chrome but Internet is not available.")
            webbrowser.open('https://www.google.com')
    elif 'music' in command:
        print("\n\nThis feature is not available at this moment.")
        talk("This feature is not available at this moment.")
    elif 'repeat after me' in command:
        if online == True:
            talk("Ok speak now.!")
            with maaz.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=1)
                print("listening....")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
            talk("You said.")
            talk(command)
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'youtube' in command:
        if online == True: 
            talk("Opeing youtube")
            webbrowser.open('https://youtube.com/')
        else:
            print("opening youtube...")
            talk("opening youtube but internet is not available")
            webbrowser.open('https"//www.youtube.com/')
    elif 'news' in command:
        if online == True:
            talk("fetching latest headlines. Region! Pakistan")
            webbrowser.open('https://dunyanews.tv/')
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'screenshot' in command:
        print("\n\nTaking Screenshot")
        talk("Taking screenshot")
        img = pyautogui.screenshot()
        img.save(r"C:/Users/Dell/Desktop/Jarvis_capture.png")
        talk("screenshot successfully saved to desktop Sir.")
    elif 'Naat' in command:
        talk("Here you go Sir!")
        music_dir = "D:\\Naat"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[1]))
    elif 'lock' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
        talk("locked")
        input("Enter to continue.")
    elif "camera" in command or "take a photo" in command:
        talk("capturing")
        ec.capture(0, "Jarvis_Capture_3.2 ", "jarvis_capture.png ")
        talk("Done") 
    elif "write a note" in command:
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
    elif "release" in command:
        print("This is jarvis_1.0 released.")
        talk("This is jarvis 1 point o released.")
    elif "weather" in command:
        if online == True:
            global temperature, humidity, type_of_temperature
            if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
                if os.name == "nt":
                    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                asyncio.run(getweather())
            print("Temperature: ", temperature, "\n\nHumidity: ", humidity, "%. ", type_of_weather)
            total_1 = "The forecast is "+ str(temperature)+ "degrees and "+type_of_weather
            total_2 = "! and humidity is "+str(humidity)+ " percent"
            total = str(total_1 + total_2)

            talk(total)
            """talk("The forecast is")
            talk(temperature)
            talk("degrees and")
            talk(type_of_weather)
            talk("! and humidity is")
            talk(humidity)
            talk("percent")"""
        else:
            print("Internet is not available. Try again later.")
            talk("Internet is not available. Try again later.")
    elif 'change your voice' in command:
        global voice_of_jarvis
        if voice_of_jarvis != "Changed":
            engine.setProperty('voice', voices[1].id)
            voice_of_jarvis = "Changed"
            talk("Ok! this will be my new voice.")
        else:
            engine.setProperty('voice', voices[0].id)
            voice_of_jarvis = "Not Changed"
            talk("Ok! this will be my new voice.")
    else:
        print("\n\nSorry! I did not got that. Can you say that again.")
        talk("Sorry! I did not got that. Can you say that again.")

startup()
