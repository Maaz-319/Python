from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()

computer_choice = None

root.title("Rock Paper Scissor")
root.geometry('1000x400')
root.state('zoomed')
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

top_label = Label(text="-:(Press the image below):-", font=('Bahnschrift', 15, 'bold'), background="light green")
top_label.place(x=500, y=0)

computer_choice_var = StringVar()
computer_choice_var.set("")
top_label = Label(textvariable=computer_choice_var, font=('Bahnschrift', 15, 'bold'), background="light green")

rock_img = Image.open("rpsdata/default.png")
rock_img = rock_img.resize((200, 200))
rimg=ImageTk.PhotoImage(rock_img)
rock_button = Button(image=rimg, foreground="Red", borderwidth=0, background="Yellow", command=rock)
rock_button.place(x=300, y=100)

paper_img = Image.open("rpsdata/paper.png")
paper_img = paper_img.resize((200, 200))
pimg=ImageTk.PhotoImage(paper_img)
paper_button = Button(image=pimg, borderwidth=0, background="Yellow", command=paper)
paper_button.place(x=550, y=100)

scissor_img = Image.open("rpsdata/scissor.png")
scissor_img = scissor_img.resize((200, 200))
simg=ImageTk.PhotoImage(scissor_img)
scissors_button = Button(image=simg, borderwidth=0, background="Yellow", command=scissor)
scissors_button.place(x=800, y=100)

computer_choice_var = StringVar()
computer_choice_var.set("")
computer_choice_label = Label(textvariable=computer_choice_var,font=('bahnschrift', 20, 'bold'), background="light green", foreground="purple")
computer_choice_label.place(x=550, y=350)

result = StringVar()
result.set("Result")
result_label = Label(textvariable=result, foreground="red", font=('bahnschrift', 20, 'bold', 'underline'), background="light green")
result_label.place(x=600, y=500)
#rock_image = PhotoImage(file="D:\Rock.png")
#rock_button = Button(text='hello',image=rock_image, borderwidth=0)
#rock_button.pack(side=TOP)
root.mainloop()
