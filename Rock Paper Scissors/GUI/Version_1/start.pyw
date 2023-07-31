from tkinter import *
import random

root = Tk()

computer_choice = None

root.title("Rock Paper Scissor")
root.geometry('600x600')
root.configure(bg="Light Green")

def rock():
    computer_choices = ['Paper', 'Scissors', 'Rock']
    computer_choice = random.choice(computer_choices)
    computer_choice_var.set("Computer = " + computer_choice)
    if computer_choice == 'Rock':
        result.set("Tied! :|")
    elif computer_choice == 'Paper':
        result.set("You lost! :(")
    elif computer_choice == 'Scissors':
        result.set("You won! :)")

def paper():
    computer_choices = ['Paper', 'Scissors', 'Rock']
    computer_choice = random.choice(computer_choices)
    computer_choice_var.set("Computer = " + computer_choice)
    if computer_choice == 'Rock':
        result.set("You won! :)")
    elif computer_choice == 'Paper':
        result.set("Tied! :|")
    elif computer_choice == 'Scissors':
        result.set("You lost! :(")

def scissor():
    computer_choices = ['Paper', 'Scissors', 'Rock']
    computer_choice = random.choice(computer_choices)
    computer_choice_var.set("Computer = " + computer_choice)
    if computer_choice == 'Rock':
        result.set("You lost! :(")
    elif computer_choice == 'Paper':
        result.set("You won! :)")
    elif computer_choice == 'Scissors':
        result.set("Tied! :|")

top_label = Label(text="-:(Press the button below):-", font=('Bahnschrift', 15, 'bold'), background="light green")
top_label.pack(pady=0)

computer_choice_var = StringVar()
computer_choice_var.set("")
top_label = Label(textvariable=computer_choice_var, font=('Bahnschrift', 15, 'bold'), background="light green")
top_label.pack(pady=20)

rock_button = Button(text="Rock", font=('Bahnschrift', 20, 'bold'), foreground="Red", borderwidth=2, background="Yellow", command=rock, width=10)
rock_button.pack(pady=10)

paper_button = Button(text="Paper", font=('Bahnschrift', 20, 'bold'), foreground="Red", borderwidth=2, background="Yellow", command=paper, width=10)
paper_button.pack(pady=10)

scissors_button = Button(text="Scissors", font=('Bahnschrift', 20, 'bold'), foreground="Red", borderwidth=2, background="Yellow", command=scissor, width=10)
scissors_button.pack(pady=10)

computer_choice_var = StringVar()
computer_choice_var.set("")
computer_choice_label = Label(textvariable=computer_choice_var,font=('bahnschrift', 20, 'bold'), background="light green", foreground="purple")
computer_choice_label.pack()

result = StringVar()
result.set("Result")
result_label = Label(textvariable=result, foreground="red", font=('bahnschrift', 20, 'bold', 'underline'), background="light green")
result_label.pack(pady=60)
#rock_image = PhotoImage(file="D:\Rock.png")
#rock_button = Button(text='hello',image=rock_image, borderwidth=0)
#rock_button.pack(side=TOP)
writer_label = Label(text="\n\n\t\t\t\t\tMade by Maaz", foreground="Blue", font=('courier', 13, 'bold', 'underline'), background="light green")
writer_label.pack()
root.mainloop()
