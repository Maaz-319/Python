from actdeact import run
from tkinter import *


def turn_off():
	file = open('actdeact.py', 'w')
	file.write('run = False')
	file.close()
	indicating_label['fg'] = 'Red'
	indicating_label['text'] = 'Startup Greetings Turned Off'


def turn_on():
	file = open('actdeact.py', 'w')
	file.write('run = True')
	file.close()
	indicating_label['fg'] = 'Green'
	indicating_label['text'] = 'Startup Greetings Turned On'


root = Tk()
root.geometry('500x200')
root.resizable(False, False)
root.title('Personal Greetings Controller')
root.configure(bg='#0f0f0f')


indicating_label = Label(text='Click', font=('Ariel', 25), bg='#0f0f0f', fg='#fff')
indicating_label.pack(pady=10)
on_trigger = Button(text='ON', command=turn_on, font=('Ariel', 15, 'bold'), width=10, bg='Green', fg='#fff')
on_trigger.place(x=65, y=100)
off_trigger = Button(text='OFF', command=turn_off, font=('Ariel', 15, 'bold'), width=10, bg='Red', fg='#fff')
off_trigger.place(x=300, y=100)

root.mainloop()