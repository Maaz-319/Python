from tkinter import *
from tkinter import filedialog


def save():
    data = str(text.get(1.0, END))
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    initialdir="C:/Users/Dell/Desktop",
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ('HTML Document', '.html'),
                                        ('All Files', '.*')],
                                    )
    file.write(data)
    file.close()


root = Tk()
root.geometry('1366x768')
root.title('Text Editor | By Maaz')
try:
    root.iconbitmap("D:/Programs/Python/icon.ico")
except:
    pass

text = Text(font=('Ariel', 16, 'bold'), background='Light Green')
text.pack(pady=5)

button = Button(text='Save', font=('Ink Free', 20, 'bold'), foreground='Green', command=save)
button.pack()

root.state('zoomed')
root.mainloop()
