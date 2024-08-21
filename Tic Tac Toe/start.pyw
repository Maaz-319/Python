from tkinter import *
from tkinter import messagebox
from plyer import notification

root = Tk()
#root.resizable(False, False)
root.title("Maaz")
# root.iconbitmap("D:/Programs/Python/icon.ico")
root.resizable(False, False)

tracker = True


def reset():
    global tracker
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)

    button1.configure(text=' ')
    button2.configure(text=' ')
    button3.configure(text=' ')
    button4.configure(text=' ')
    button5.configure(text=' ')
    button6.configure(text=' ')
    button7.configure(text=' ')
    button8.configure(text=' ')
    button9.configure(text=' ')

    button1.configure(background='white')
    button2.configure(background='white')
    button3.configure(background='white')
    button4.configure(background='white')
    button5.configure(background='white')
    button6.configure(background='white')
    button7.configure(background='white')
    button8.configure(background='white')
    button9.configure(background='white')

    tracker = True


def disable_button():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)    


def btn_func(b):
    global tracker
    if tracker == True and b["text"] == ' ':
        b.configure(text='X')
        tracker = False
        #b["state"] = DISABLED
        if button1["text"] == 'X' and button2["text"] == 'X' and button3["text"] == 'X':
            button1["background"] = 'Light Green'
            button2["background"] = 'Light Green'
            button3["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button4["text"] == 'X' and button5["text"] == 'X' and button6["text"] == 'X':
            button4["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button6["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button7["text"] == 'X' and button8["text"] == 'X' and button9["text"] == 'X':
            button7["background"] = 'Light Green'
            button8["background"] = 'Light Green'
            button9["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button1["text"] == 'X' and button4["text"] == 'X' and button7["text"] == 'X':
            button1["background"] = 'Light Green'
            button4["background"] = 'Light Green'
            button7["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button2["text"] == 'X' and button5["text"] == 'X' and button8["text"] == 'X':
            button2["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button8["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button3["text"] == 'X' and button6["text"] == 'X' and button9["text"] == 'X':
            button3["background"] = 'Light Green'
            button6["background"] = 'Light Green'
            button9["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button1["text"] == 'X' and button5["text"] == 'X' and button9["text"] == 'X':
            button1["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button9["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
        elif button3["text"] == 'X' and button5["text"] == 'X' and button7["text"] == 'X':
            button3["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button7["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "X wins! congradulations!")
            disable_button()
    elif tracker == False and b["text"] == ' ':
        b.configure(text='O')
        tracker = True
        #b["state"] = DISABLED
        if button1["text"] == 'O' and button2["text"] == 'O' and button3["text"] == 'O':
            button1["background"] = 'Light Green'
            button2["background"] = 'Light Green'
            button3["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button4["text"] == 'O' and button5["text"] == 'O' and button6["text"] == 'O':
            button4["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button6["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button7["text"] == 'O' and button8["text"] == 'O' and button9["text"] == 'O':
            button7["background"] = 'Light Green'
            button8["background"] = 'Light Green'
            button9["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button1["text"] == 'O' and button4["text"] == 'O' and button7["text"] == 'O':
            button1["background"] = 'Light Green'
            button4["background"] = 'Light Green'
            button7["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button2["text"] == 'O' and button5["text"] == 'O' and button8["text"] == 'O':
            button2["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button8["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button3["text"] == 'O' and button6["text"] == 'O' and button9["text"] == 'O':
            button3["background"] = 'Light Green'
            button6["background"] = 'Light Green'
            button9["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button1["text"] == 'O' and button5["text"] == 'O' and button9["text"] == 'O':
            button1["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button9["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()
        elif button3["text"] == 'O' and button5["text"] == 'O' and button7["text"] == 'O':
            button3["background"] = 'Light Green'
            button5["background"] = 'Light Green'
            button7["background"] = 'Light Green'
            messagebox.showinfo("Tic Tac Toe | By Maaz", "O wins! congradulations!")
            disable_button()    
    else:
        notification.notify(
            #title of the notification,
            title = "Tic Tac Toe",
            message = "The box you are trying to fill is already filled".format(
            timeout  = 50)
        )
        #messagebox.showerror("Tic Tac Toe | By Maaz", "Box Already Clicked!")


menubar = Menu(root)
root.config(menu=menubar)

option_menu = Menu(menubar, tearoff=False)
menubar.add_command(label='Reset Game', command=reset)


button1 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button1), font=('Helvetica', 9, 'bold'), bg='white')
button1.grid(row=0, column=0)
button2 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button2), font=('Helvetica', 9, 'bold'), bg='white')
button2.grid(row=0, column=1)
button3 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button3), font=('Helvetica', 9, 'bold'), bg='white')
button3.grid(row=0, column=2)

button4 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button4), font=('Helvetica', 9, 'bold'), bg='white')
button4.grid(row=1, column=0)
button5 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button5), font=('Helvetica', 9, 'bold'), bg='white')
button5.grid(row=1, column=1)
button6 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button6), font=('Helvetica', 9, 'bold'), bg='white')
button6.grid(row=1, column=2)

button7 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button7), font=('Helvetica', 9, 'bold'), bg='white')
button7.grid(row=2, column=0)
button8 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button8), font=('Helvetica', 9, 'bold'), bg='white')
button8.grid(row=2, column=1)
button9 = Button(text=' ', height=5, width=8, command=lambda: btn_func(button9), font=('Helvetica', 9, 'bold'), bg='white')
button9.grid(row=2, column=2)

messagebox.showinfo('Tic Tac Toe | By Maaz', '"X" will go first')

root.mainloop()
