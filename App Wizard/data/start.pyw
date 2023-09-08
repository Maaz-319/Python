from tkinter import *
import os

programs = []
file_dir = None


def start_program():
    global programs, file_dir
    selected_program = listbox.curselection()
    file = os.path.join(file_dir, programs[selected_program[0]])
    os.system('"'+file+'"')


def initializer():
    global programs, file_dir
    file_dir = "."
    files = os.listdir(file_dir)
    programs = [file for file in files if file.endswith((".pyw"))]
    for file in programs:
        listbox.insert(END, file)
    listbox.config(height=14, width=25)
    listbox.place(x=10, y=10)


root = Tk()
bg = "#1f1f1f"

root.title("App Wizard")
root.geometry("300x400")
root.resizable(False, False)
root.config(bg=bg)

listbox = Listbox(root, selectmode=SINGLE, font=("Constancia", 15), bg=bg, borderwidth=0, selectborderwidth=0,
                  fg='#FFFFFF', selectbackground='#2E7D32')
listbox.place(x=10, y=10)

open_button = Button(root, font=("Times new Roman", 15), text="Open", bg='#2E7D32', width=12, fg="#FFFFFF", command=start_program, border=0)
open_button.place(x=82, y=360)

initializer()

root.mainloop()
