from tkinter import *
from tkinter import messagebox

# Default Colour
color = '#1f1f1f'


def change_indicating_label(selection):
    option_temp = default_selection.get()
    if option_temp == '°C to °F':
        indicating_label['text'] = 'Enter Celsius'
    elif option_temp == '°F to °C':
        indicating_label['text'] = 'Enter Fahrenheit'
    elif option_temp == '°C to  K':
        indicating_label['text'] = 'Enter Celsius'
    elif option_temp == '°F to  K':
        indicating_label['text'] = 'Enter Fahrenheit'
    elif option_temp == ' K to °C':
        indicating_label['text'] = 'Enter Kelvin'
    elif option_temp == ' K to °F':
        indicating_label['text'] = 'Enter Kelvin'


def calculate_answer():
    option_temp = default_selection.get()
    if option_temp == '°C to °F':
        try:
            temperature = float(input_entry.get())
            result = str((temperature * 9 / 5) + 32) + ' °F'
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        except ValueError:
            messagebox.showerror('System', 'Enter Correct Value')
    elif option_temp == '°F to °C':
        try:
            temperature = float(input_entry.get())
            result = str((temperature - 32) * 5 / 9) + ' °C'
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        except ValueError:
            messagebox.showerror('System', 'Enter Correct Value')
    elif option_temp == '°C to  K':
        try:
            temperature = float(input_entry.get())
            result = str(temperature + 273.15) + ' K'
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        except ValueError:
            messagebox.showerror('System', 'Enter Correct Value')
    elif option_temp == '°F to  K':
        try:
            temperature = float(input_entry.get())
            result = str(((temperature - 32) * 5 / 9) + 273.15) + ' K'
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        except ValueError:
            messagebox.showerror('System', 'Enter Correct Value')
    elif option_temp == ' K to °C':
        try:
            temperature = float(input_entry.get())
            result = str(temperature - 273.15) + ' °C'
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        except ValueError:
            messagebox.showerror('System', 'Enter Correct Value')
    elif option_temp == ' K to °F':
        try:
            temperature = float(input_entry.get())
            result = str((temperature - 273.15) * 9 / 5 + 32) + ' °F'
            result_entry.delete(0, END)
            result_entry.insert(0, result)
        except ValueError:
            messagebox.showerror('System', 'Enter Correct Value')


# Window Interface Configuration
root = Tk()
root.geometry('650x250')
root['bg'] = color
root.title('Temperature Convertor | By Maaz')
root.resizable(False, False)

# All Options list
options = ['°C to °F',
           '°C to  K',
           '°F to °C',
           '°F to  K',
           ' K to °C',
           ' K to °F'
           ]
# Default Selected Option
default_selection = StringVar()
default_selection.set(options[0])

indicating_label = Label(root, text="Enter Celsius", font=('Ariel', 15), bg=color, foreground='Light Green')
indicating_label.place(x=30, y=10)

# Input Box
input_entry = Entry(font=('Ariel', 20), background='#bbb', borderwidth=0, width=20, foreground='purple')
input_entry.place(x=210, y=9)

# Options Bar
option_bar = OptionMenu(root, default_selection, *options, command=change_indicating_label)
option_bar.configure(bg='Light Blue', borderwidth=0)
option_bar.place(x=520, y=12)

# Initialize Button
button = Button(text='Convert', font=('Ariel', 15), bg='Green', foreground='#fff', borderwidth=0, width=15, height=2,
                command=calculate_answer)
button.place(x=260, y=90)

answer_label = Label(root, text="Answer", font=('Ariel', 18), bg=color, foreground='Light Green')
answer_label.place(x=100, y=185)

# Result Box
result_entry = Entry(font=("Ariel", 20), background='#bbb', borderwidth=0, width=20, foreground='Green')
result_entry.place(x=210, y=180)

root.mainloop()
