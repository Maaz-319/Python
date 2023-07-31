from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.title('Dice Roll | By Maaz')
root.resizable(False,False)


canvas = Canvas(root, width = 300, height = 300)
canvas.pack(padx=80)
text = Label(font=('courier', 20, 'bold'), foreground='Red')
text.pack()


def choose_random():
    global list_6,random_choice,canvas,img
    list_6 = [1,2,3,4,5,6]
    random_choice = str(random.choice(list_6))    
    text.configure(text=random_choice)
    random_choice =  str('uttills/' + random_choice + '.png')
    img = PhotoImage(file=random_choice)      
    canvas.create_image(20,20, anchor=NW, image=img)

roll = Button(text='Roll', command=choose_random, font=('courier', 20, 'bold'))
roll.pack()
root.mainloop()
