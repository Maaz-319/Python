from tkinter import *
import pyautogui

def mouse_position(temp):
   label['text'] = str(pyautogui.position()).replace('Point', '')

root = Tk()
root.state('zoomed')
# root.geometry('200x200')
root.resizable(False, False)
root.title("Mouse Position")

label = Label(text='x:y', font=('Ariel', 10), fg='Black')
label.place(x=0, y=0)

root.bind('<Motion>', mouse_position)

root.mainloop()