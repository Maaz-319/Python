import speech_recognition as maaz
from talk import talk
import os

listener = maaz.Recognizer()


def take_command():
    try:
            with maaz.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=1)
                os.system("cls")
                print("listening....")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                if 'jarvis' in command:
                    command = command.replace('jarvis','')
                elif 'Jarvis'in command:
                    command = command.replace('Jarvis','')
    except:
            print("\nSorry! can you say that again.")
            talk("\nSorry! can you say that again.")
            take_command()
    return command
