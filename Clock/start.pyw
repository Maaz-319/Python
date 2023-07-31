from tkinter import *
from datetime import datetime
import time
import customtkinter as maaz

root = maaz.CTk()
root.title('Clock | By Maaz')
maaz.set_appearance_mode('system')
maaz.set_default_color_theme('green')
root.geometry('500x100')
root.resizable(False, False)

label = maaz.CTkLabel(text_font=("times", 70), fg_color=("Red", "Black"))
label.pack(anchor='center')


def start():
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%I:%M:%S-%p")
    label.configure(text=currentTime)
    root.after(1, start)


start()
root.mainloop()
