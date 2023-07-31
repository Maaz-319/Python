from tkinter import *
from tkinter import messagebox
import time
import customtkinter as maaz

maaz.set_default_color_theme('green')


def run():
    button.state = DISABLED
    try:
        seconds = int(entry.get())
        entry.delete(0, 'end')
        while seconds != -1:
            total = str(seconds) + ' seconds left'
            label2.configure(text=total)
            seconds -= 1
            time.sleep(1)
            root.update()
        label2.configure(text='Done!')
        messagebox.showinfo('Timer | By Maaz', 'Time Completed')
        button.state = NORMAL
    except:
        entry.delete(0, 'end')
        messagebox.showerror("Timer | By Maaz", "Enter positive 'Numbers' only")
        button.state = NORMAL


root = maaz.CTk()
root.geometry('500x300')
root.title('Timer | By Maaz')
root.set_appearance_mode('system')
root.resizable(False, False)

label = maaz.CTkLabel(text="Enter seconds:", text_font=('Hevetica', 20, "bold"))
label.pack(padx=10, pady=5)

entry = maaz.CTkEntry(text_font=('Hevetica', 20))
entry.pack(padx=8, pady=20)

button = maaz.CTkButton(text='start', text_font=('Hevetica', 20), command=run)
button.pack(padx=10)

label2 = maaz.CTkLabel(text='', text_font=('Hevetica', 20))
label2.pack(padx=10, pady=20)

root.mainloop()
