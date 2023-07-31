from tkinter import *


def calculate():
    height = float(height_entry.get()) * 0.304
    weight = int(weight_entry.get())
    result = round(weight / (height * height), 1)
    if 18.5 <= result <= 24.9:
        result_label["fg"] = "Green"
        result_label["text"] = "BMI is " + str(result) + ". Normal BMI. Well done"
    elif result < 18.5:
        result_label["fg"] = "White"
        result_label["text"] = "BMI is " + str(result) + ". UnderWeight.\n\nYou need food if you want to survive."
    elif result > 24.9:
        result_label["fg"] = "Red"
        result_label["text"] = "BMI is " + str(result) + ". OverWeight.\n\nPlease give some food to others also."


root = Tk()
bg = "#1f1f1f"

root.title("BMI Calculator | By Maaz")
root.geometry("500x400")
root.resizable(False, False)
root.config(bg='#1f1f1f')

Label(text="Enter Height (feet):", font=('Ariel', 15), bg=bg, foreground='Light Green').place(x=10, y=30)
height_entry = Entry(font=('Ariel', 18), background='#bbb', borderwidth=0, width=20, foreground='purple', )
height_entry.place(x=181, y=29)

Label(text="Enter Weight (kg) :", font=('Ariel', 15), bg=bg, foreground='Light Green').place(x=10, y=100)
weight_entry = Entry(font=('Ariel', 18), background='#bbb', borderwidth=0, width=20, foreground='purple', )
weight_entry.place(x=180, y=100)

calculate_button = Button(text='Calculate', font=('Ariel', 15), bg='Green', foreground='#fff', borderwidth=0, width=15,
                          height=2, command=calculate)
calculate_button.place(x=170, y=200)

result_label = Label(font=('Ariel', 15), bg=bg)
result_label.place(x=70, y=320)
root.mainloop()
