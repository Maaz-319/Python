from  tkinter import *
from tkinter import messagebox
import python_weather, asyncio,os

root = Tk()
root.geometry('500x500')
root.title('Weather_App | By Maaz')
root.state('zoomed')

async def getweather():
    
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(format=python_weather.IMPERIAL) as client:
    global temperature, humidity, type_of_temperature


    # fetch a weather forecast from a city
    try:
      weather = await client.get("Lahore")
    except:
      messagebox.showerror('Weather_App', 'There was an error while getting Weather.\nCheck your Internet Connection')
    global type_of_weather, temperature, humidity
    # returns the current day's forecast temperature (int)
    type_of_weather = weather.current.description
    temperature = int((int(weather.current.temperature) - 32) * (5/9))
    humidity = weather.current.humidity


def start_1():
    if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
                if os.name == "nt":
                    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                asyncio.run(getweather())
                total_1 = 'Temperature: ' + str(temperature)
                total_2 =  '\nType: ' + type_of_weather
                total_3 =  '\nHumidty: '+ str(humidity) + '%'
                city = 'City: Lahore\n'
                total = city + total_1 + total_2 + total_3
                label.configure(text = total)
            
label = Label(foreground = 'Green', font=('courier', 20, 'bold'))
label.pack(pady=10)
button = Button(text='Update_Weather', font=('courier', 20, 'bold'),command=start_1, foreground='Yellow', background = 'Red', borderwidth=0.5)
button.pack(pady=10)




root.mainloop()
