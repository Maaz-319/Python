from pydictionary import Dictionary
from urllib import request
import requests
from tkinter import *
from tkinter import messagebox


# Functions
def meanings_display():
		# Check Internet
		try:
			requests.post('https://www.google.com/')
			online = True
		except:
			online = False

		# Find Word
		if online == True:
			text.delete('1.0', END)
			word = Dictionary(str(entry.get()), 1)
			result = "Meaning- " + str(word.meanings())
			result = result.replace('[', '').replace(']', '').replace('\'', '').replace(';', '\n\nSynonym-').replace(':', '\n\nSentence-')
			text.insert(INSERT, str(result))
		else:
			messagebox.showerror("Dictionary", "Make sure that you are connected to internet")


def antonyms_display():
		# Check Internet
		try:
			requests.post('https://www.google.com/')
			online = True
		except:
			online = False

		# Find Word
		if online == True:
			text.delete('1.0', END)
			word = Dictionary(str(entry.get()), 5)
			result = str(word.antonyms())
			result = result.replace(',', '\n\n•').replace('[', '\n• ').replace(']', '').replace('\'', '')
			text.insert(INSERT, str(result))
		else:
			messagebox.showerror("Dictionary", "Make sure that you are connected to internet")


# Define GUI Window
root = Tk()
root.configure(bg="Light Green")
root.title("Dictionary | by Maaz")
root.state("zoomed")
root.resizable(False, False)

top_label = Label(text="Enter word below ↓",background="Light Green", font=("Microsoft YaHei UI Dark", 20)).pack(pady=10)

# TextBox
entry = Entry(font=("Microsoft YaHei UI Light", 20))
entry.pack(pady=10)

#Buttons
meaning = Button(text="Meanings", font=("Microsoft YaHei UI Light", 20), background="Pink", command=meanings_display).pack(pady=10)
antonym = Button(text="Antonyms", font=("Microsoft YaHei UI Light", 20), background="Pink", command=antonyms_display).pack(pady=10)

#Result
text = Text(font=('Microsoft YaHei UI Light', 15, 'bold'),background='Light Green', borderwidth=0)
text.pack(pady=10, expand= 1, fill= BOTH)

root.mainloop()