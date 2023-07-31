from tkinter import *


def up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-6)

def down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+6)

def right(event):
    label.place(x=label.winfo_x()+6, y=label.winfo_y())

def left(event):
    label.place(x=label.winfo_x()-6, y=label.winfo_y())

root = Tk()
root.state('zoomed')
root.title("Move a car with keys | By Maaz")
# root.iconbitmap("D:/Programs/Python/icon.ico")

root.bind('<w>', up)
root.bind("<s>", down)
root.bind("<d>", right)
root.bind("<a>", left)
root.bind('<Up>', up)
root.bind("<Down>", down)
root.bind("<Right>", right)
root.bind("<Left>", left)

image = PhotoImage(file="race.png")
label = Label(image=image)
label.place(x=170, y=230)

root.mainloop()