from tkinter import *
import random

choices = ["Heads", "Tails"]
image_file = None


def flip():
    global choice, choices, canvas, image_file
    choice = random.choice(choices)
    if choice == "Heads":
        image_path = str(r'FliptheCoindata/Heads.png')
        image_file = PhotoImage(file=image_path)
        canvas.create_image(52,45, anchor='nw', image=image_file)
    else:
        image_path = str(r'FliptheCoindata/Tails.png')
        image_file = PhotoImage(file=image_path)
        canvas.create_image(60,45, anchor='nw', image=image_file)



root = Tk()
root.title("Flip a coin | By Maaz")
root['background'] = 'Light Green'
root.resizable(False, False)

canvas = Canvas(root, width = 300, height = 300, background="Light Green", border=0, borderwidth=0)
canvas.pack(pady=10)

button = Button(text="Flip the Coin", background="pink", font=("Ariel", 20), borderwidth=1, command=flip)
button.pack(pady=10)
root.mainloop()