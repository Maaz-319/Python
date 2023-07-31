import random
from tkinter import Text, messagebox

import customtkinter as maaz
import pyperclip
from customtkinter import *

small_case = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z']

large_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', '(', '_', '-', '=', '+']

maaz.set_default_color_theme('green')
maaz.set_appearance_mode('system')
root = maaz.CTk()
root.title("Password Generator")
root.state('zoomed')
root.resizable(False, False)


def four():
    global text
    password_4 = str(
        random.choice(small_case) + random.choice(symbols) + str(random.choice(numbers)) + random.choice(
            large_case))

    text.delete('1.0', END)
    text.insert(INSERT, password_4)


def six():
    password_6 = str(
        random.choice(small_case) + random.choice(symbols) + str(random.choice(numbers)) + random.choice(
            large_case) + random.choice(small_case) + random.choice(symbols) + str(
            random.choice(numbers)) + random.choice(
            large_case))

    text.delete('1.0', END)
    text.insert(INSERT, password_6)


def eight():
    password_8 = str(
        random.choice(small_case) + random.choice(symbols) + str(random.choice(numbers)) + random.choice(
            large_case) + random.choice(small_case) + random.choice(symbols) + str(
            random.choice(numbers)) + random.choice(
            large_case) + random.choice(small_case) + str(random.choice(numbers)))

    text.delete('1.0', END)
    text.insert(INSERT, password_8)


def twelve():
    password_12 = str(
        random.choice(small_case) + str(random.choice(numbers)) + random.choice(symbols) + random.choice(
            large_case) + random.choice(small_case) + random.choice(symbols) + str(
            random.choice(numbers)) + random.choice(
            large_case) + random.choice(small_case) + str(random.choice(numbers)) + str(
            random.choice(symbols)) + random.choice(large_case) + random.choice(small_case) + str(
            random.choice(numbers)))

    text.delete('1.0', END)
    text.insert(INSERT, password_12)


def sixteen():
    password_16 = str(
        random.choice(small_case) + str(random.choice(numbers)) + random.choice(symbols) + random.choice(
            large_case) + random.choice(small_case) + random.choice(symbols) + str(
            random.choice(numbers)) + random.choice(
            large_case) + random.choice(small_case) + str(random.choice(numbers)) + str(
            random.choice(numbers)) + random.choice(large_case) + random.choice(symbols) + str(
            random.choice(numbers)) + random.choice(symbols) + random.choice(small_case) + str(
            random.choice(numbers)) + random.choice(large_case))

    text.delete('1.0', END)
    text.insert(INSERT, password_16)


def copy_password():
    pyperclip.copy(str(text.get('1.0', END)))
    messagebox.showinfo('System', 'Password has been copied to clipboard')


label = maaz.CTkLabel(text="Password:", text_font=('Ariel', 20))
label.place(x=390, y=50)

text = Text(root, font=('Ariel', 20), width=20, height=1, background='#1f1f1f', foreground='#fff', border=0)
text.pack(pady=50)

button4 = maaz.CTkButton(text='4-Characters', text_font=('Ariel', 20), command=four, height=100)
button4.place(x=150, y=400)

button6 = maaz.CTkButton(text='6-Characters', text_font=('Ariel', 20), command=six, height=100)
button6.place(x=350, y=400)

button8 = maaz.CTkButton(text='8-Characters', text_font=('Ariel', 20), command=eight, height=100)
button8.place(x=550, y=400)

button12 = maaz.CTkButton(text='12-Characters', text_font=('Ariel', 20), command=twelve, height=100)
button12.place(x=750, y=400)

button16 = maaz.CTkButton(text='16-Characters', text_font=('Ariel', 20), command=sixteen, height=100)
button16.place(x=960, y=400)

copy_button = maaz.CTkButton(text='Copy', text_font=('Ariel', 20), command=copy_password, height=100)
copy_button.place(x=1000, y=200)

root.mainloop()
