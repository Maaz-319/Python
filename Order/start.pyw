from tkinter import *
import os

window = Tk()


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("\n\tYou ordered:")
    for index in food:
        print("\n\t\t-" + index)


def add():
    listbox.insert(listbox.size(), entrybox.get())


def delete():
    try:
        listbox.delete(listbox.curselection())
        listbox.config(height=listbox.size())
    except:
        print("\n\tDelete One by One\n\n")
        input("Press Enter to Continue....")
        os.system('cls')
        os.system('start.py')


listbox = Listbox(window, selectmode=MULTIPLE, font=("Constancia", 40))
listbox.insert(1, "Pizza")
listbox.insert(2, "Burger")
listbox.insert(3, "Wrap")
listbox.insert(4, "Drink")
listbox.insert(5, "Salad")
listbox.config(height=listbox.size())
listbox.pack()

entrybox = Entry(window)
entrybox.pack()

submit_button = Button(text="Submit Order", command=submit)
submit_button.pack()

add_button = Button(text="Add Item", command=add)
add_button.pack()

delete_button = Button(text="Delete Item", command=delete)
delete_button.pack()

window.mainloop()
