import pyperclip
import random
import threading
from tkinter import *
from tkinter.messagebox import showerror, showinfo

password_lengths = ['4', '8', '16', '32', '128']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
letter_list = list('abcdefghijklmnopqrstuvwxyz')
symbols_list = list('!@#$%^&*()_+=-}|;:<>.,/?')
include_symbols = False
include_numbers = False
include_letters = False
do_not_generate_password = False


def thread():
    password_field.delete(0, END)
    t2 = threading.Thread(target=start)
    t2.start()


def decoration_controller(temp):
    global include_symbols, include_letters, include_numbers
    if temp == 's':
        include_symbols = True
    elif temp == 'n':
        include_numbers = True
    elif temp == 'l':
        include_letters = True

    if not include_numbers and not include_symbols and not include_letters :
        global do_not_generate_password
        do_not_generate_password = True
    else:
        return


root = Tk()
bg_black_color = '#2f2f2f'

root.state('zoomed')
root.configure(bg=bg_black_color)
root.title('Password Generator')


def start():
    decoration_controller(0)
    global include_symbols, include_letters, include_numbers, do_not_generate_password

    while True:
        if include_letters:
            passw = random.choice(letter_list)
            password_field.insert(0, passw)
        if len(password_field.get()) == int(length.get()):
            break;

        if include_numbers:
            passw = random.choice(number_list)
            password_field.insert(0, passw)
        if len(password_field.get()) == int(length.get()):
            break;

        if include_symbols:
            passw = random.choice(symbols_list)
            password_field.insert(0, passw)
        if len(password_field.get()) == int(length.get()):
            break;


def copy():
    pyperclip.copy(str(password_field.get()))
    showinfo('Clipboard Command', 'Password copied to clipboard')


decoration_controller(0)
Label(text='Password:', font=('Helvetica', 25), bg=bg_black_color, fg='White').place(x=50, y=100)
password_field = Entry(font=('Helvetica', 25), width=30, bg=bg_black_color, fg='white', borderwidth=0.5)
password_field.place(x=230, y=100)

copy_button = Button(text='Copy Password', font=('Helvetica', 25), bg='Green', fg='#fff', borderwidth=0,
                     activeforeground='#fff', activebackground='#005000', command=copy)
copy_button.place(x=270, y=150)

Label(text='Password Type:', font=('Helvetica', 15), bg=bg_black_color, fg='White').place(x=900, y=50)

symbols_checkbox = Checkbutton(text='Include Symbols(!,@,$..)', bg=bg_black_color, font=('Helvetica', 15),
                               fg='Green', activebackground=bg_black_color, activeforeground='Green',
                               command=lambda: decoration_controller('s'))
symbols_checkbox.place(x=920, y=100)

numbers_checkbox = Checkbutton(text='Include Numbers(123..)', bg=bg_black_color, font=('Helvetica', 15),
                               fg='Green', activebackground=bg_black_color, activeforeground='Green',
                               command=lambda: decoration_controller('n'))
numbers_checkbox.place(x=920, y=150)

letters_checkbox = Checkbutton(text='Include letter(a,b,c..)', bg=bg_black_color, font=('Helvetica', 15),
                               fg='Green', activebackground=bg_black_color, activeforeground='Green',
                               command=lambda: decoration_controller('l'))
letters_checkbox.place(x=920, y=200)

start_button = Button(text='Generate Password', font=('Helvetica', 25), bg='Green', fg='#fff', borderwidth=0,
                      activeforeground='#fff', activebackground='#005000', command=thread)
start_button.place(x=300, y=400)

Label(text='Select Password Length', font=('Helvetica', 15), bg=bg_black_color, fg='White', borderwidth=0.5).place(
    x=900, y=350)
length = StringVar()
length.set(password_lengths[2])
password_length_menu = OptionMenu(root, length, *password_lengths)
password_length_menu.place(x=970, y=400)

root.mainloop()
