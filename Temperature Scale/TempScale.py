from tkinter import *

window = Tk()

def submit():
    print("\n\tThe temperature is " + str(scale.get()) + " degrees Celcius\n")

scale = Scale(window, from_=100,to=0, length=600, orient=VERTICAL, font=('Consolas',20), tickinterval=10)
scale.set(37)
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
