from tkinter import *
import random
import time

bk = "#202020"

root = Tk()
root.configure(bg=bk)

attempts = 10
answer = random.randint(1, 50)


def check_answer():
	global attempts
	global win_label
	global answer
	global text_label
	global entry_window
	
	user_guess = int(entry_window.get())
	attempts -= 1

	if answer == user_guess:
		text_label.set("\nVictory!!!! You got the number :)")
		check_button.pack_forget()
	elif attempts == 0:
		text_label.set("\n\nAttempts are over :(")
		check_button.pack_forget()

	elif user_guess < answer:
		text_label.set("\n\nGo Higher. You have " + str(attempts) + " turns left.")
	elif user_guess >	 answer:
		text_label.set("\n\nGo Lower. You have " + str(attempts) + " turns left.")
	else:
		attempts += 1


root.bind('<Return>', check_answer)
root.title("Number Guessing Game")

root.geometry("500x500")

label = Label(root, text="\n\nGuess a number between 1-50.\n\n", font=('courier', 22, 'bold'), foreground="orange", bg=bk)
label.pack()

entry_window = Entry(root, width=20, borderwidth=2, justify=CENTER,foreground="white" ,font=('courier', 25, 'bold'), bg='Grey')
entry_window.pack()

space_label = Label(text="\n\n", bg=bk)
space_label.pack()

check_button = Button(text="Check", command=check_answer, relief=GROOVE, font =('calibri', 20),foreground = 'green', bg='#ccad25', border=0)
check_button.pack()

text_label = StringVar()
text_label.set("\n\nYou have 10 attempts!.")

guess_attempts = Label(textvariable=text_label,foreground="Red" ,font=('courier', 18, 'bold'), bg=bk)
guess_attempts.pack()

writer_label = Label(text="\n\n\n\t\t\t\tMade by Maaz", foreground="Blue", font=('courier', 13, 'bold', 'underline'), bg=bk)
writer_label.pack()

root.mainloop()
