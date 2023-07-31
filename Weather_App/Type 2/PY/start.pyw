from tkinter import *
from tkinter import messagebox
import requests
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import timezonefinder
import threading


def starter(temp):
    button['state'] = DISABLED
    t2 = threading.Thread(target=find_weather(1))
    t2.start()


def search_bar_temp_text_focus_in(text):
    search_bar.delete(0, END)
    search_bar['fg'] = '#fff'


def search_bar_temp_text_focus_out(text2):
    search_bar.delete(0, END)
    search_bar.insert(0, "Enter City Name eg. Lahore")
    search_bar['fg'] = '#aaa'


def find_weather(temp):
    if search_bar.get() == None:
        messagebox.showerror('System', "Enter a city name")
    else:
        global url
        city_name = search_bar.get()
        geolocator = Nominatim(user_agent='geoapiExercises')
        try:
            location = geolocator.geocode(city_name)
        except:
            messagebox.showerror("System", "There was an error while getting Weather")
        initial = TimezoneFinder()
        try:
            result = initial.timezone_at(lng=location.longitude, lat=location.latitude)
        except:
            messagebox.showerror("System", "There was an error while getting Weather")
        get_time = pytz.timezone(result)
        local_time = datetime.now(get_time)
        time = local_time.strftime('%I:%M %p')
        time_name_label['text'] = 'Current Time'
        time_label['text'] = time
        url = str(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=d4be8e123adba5a49a451c7bd54e558b")
        weather_data = requests.get(url).json()
        condition = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = int(weather_data['main']['temp'] - 273.15)
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        pressure_label['text'] = pressure
        humidity_label['text'] = humidity
        wind_speed_label['text'] = wind_speed
        description_label['text'] = description
        temperature_label['text'] = str(temperature) + ' °C'
        condition_label['text'] = condition + " | " + "FEELS LIKE " + str(temperature)
        button['state'] = NORMAL


root = Tk()
root.geometry('700x500+300+200')
root.resizable(False, False)
root.title('Weather App | by Maaz')
root.configure(bg='Light Green')

search_bar_image = PhotoImage(file='Utills/search bar.png')
search_bar_image_label = Label(image=search_bar_image, width=400, height=100, background='Light Green')
search_bar_image_label.place(x=0, y=0)

search_bar = Entry(font=('Ariel', 15), width=26, background='#3f3f3f', borderwidth=0, foreground='#aaa')
search_bar.insert(0, "Enter City Name eg. Lahore")
search_bar.place(x=30, y=40)
search_bar.bind("<FocusIn>", search_bar_temp_text_focus_in)
search_bar.bind("<FocusOut>", search_bar_temp_text_focus_out)

weather_icon_image = PhotoImage(file='Utills/Weather icon.png')
weather_icon_label = Label(image=weather_icon_image, background='Light Green')
weather_icon_label.place(x=200, y=150)

weather_info_image = PhotoImage(file='Utills/all_weather_info.png')
weather_info_label = Label(image=weather_info_image, background='Light Green')
weather_info_label.place(x=10, y=400)

wind_speed_label = Label(text='---', background='#179DCF', foreground='#fff', width=10, font=('Ariel', 12))
wind_speed_label.place(x=30, y=440)

humidity_label = Label(text='---', background='#179DCF', foreground='#fff', width=10, font=('Ariel', 12))
humidity_label.place(x=160, y=440)

description_label = Label(text='---', background='#179DCF',
                          foreground='#fff', font=('Ariel', 12), width=15)
description_label.place(x=320, y=440)

pressure_label = Label(text='---', background='#179DCF', foreground='#fff', width=10, font=('Ariel', 12))
pressure_label.place(x=500, y=440)

time_name_label = Label(font=('Ariel', 20, 'underline'), background='Light Green')
time_name_label.place(x=20, y=100)

time_label = Label(font=('Times', 20), background='Light Green')
time_label.place(x=25, y=150)

temperature_label = Label(font=('Times', 50), foreground='Purple', background='Light Green')
temperature_label.place(x=450, y=150)

condition_label = Label(font=('Ariel', 15), background='Light Green')
condition_label.place(x=450, y=250)

button = Button(text='GO', foreground='#1f1f1f', background='Pink', font=('Times', 20),
                command=lambda: starter(0), borderwidth=1, width=10)
button.place(x=430, y=25)

root.bind('<Return>', starter)

root.mainloop()
