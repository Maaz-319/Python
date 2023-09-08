from tkinter import *
from datetime import date


def calculator():
    year = int(year_entry.get())
    month = int(month_entry.get())
    datee = int(date_entry.get())
    today = date.today()
    birthdate = date(year, month, datee)
    age = today.year - birthdate.year
    # if today%4 == 0:
    #     age_year = age/366
    # else:
    #     age_year = age/365
    age_error_coverage = birthdate.month - today.month
    if age_error_coverage <= 0:
        result_label['text'] = 'You are ' + str(age) + ' years old.'
    else:
        age -= 1
        result_label['text'] = ('You are ' + str(age) + ' years old.\nAfter ' + str(age_error_coverage) + 'months, you will be ' + str(age+1) + ' years old.')


black_bg_colour = '#1f1f1f'

root = Tk()
root.configure(bg=black_bg_colour)
root.title('Age Calculator')
root.geometry('400x500')
root.resizable(False, False)

label = Label(text='Enter your Birthdate', font=('Helvetica', 20), background = black_bg_colour, fg='#fff').pack(pady=5)

Label(text='Year eg. 2006', bg=black_bg_colour, fg='Grey').place(x=52, y=180)
year_entry = Entry(font=('Times', 12), width=7)
year_entry.place(x=60, y=200)

Label(text='Month 01-12', bg=black_bg_colour, fg='Grey').place(x=155, y=180)
month_entry = Entry(font=('Times', 12), width=7)
month_entry.place(x=160, y=200)

Label(text='Date 01-31', bg=black_bg_colour, fg='Grey').place(x=258, y=180)
date_entry = Entry(font=('Times', 12), width=7)
date_entry.place(x=260, y=200)

calculate_button = Button(text='Calculate', font=('Ariel', 20), bg='Green', border=0, command=calculator)
calculate_button.place(x=130, y=300)

result_label = Label(text='Result', font=('Times', 15), background=black_bg_colour, fg='Light Green')
result_label.place(x=25, y=400)

root.mainloop()