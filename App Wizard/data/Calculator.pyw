from tkinter import *

def command_1():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 1)

def command_2():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 2)

def command_3():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 3)

def command_4():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 4)

def command_5():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 5)

def command_6():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 6)

def command_7():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 7)

def command_8():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 8)

def command_9():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 9)

def command_0():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 0)

def command_point():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, '.')

def command_add():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, '+')

def command_subtract():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, '-')

def command_divide():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, '÷')

def command_multiply():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, '*')

def command_double_zero():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 0)
    text_box.insert(END, 0)

def command_three_zero():
    text_box.configure(foreground="BLUE")
    text_box.insert(END, 0)
    text_box.insert(END, 0)
    text_box.insert(END, 0)

def command_delete():
    text_box.delete(1)

def command_delete_2():
    text_box.delete(0, 'end')

def handle_keypress(event):
    if event.keysym == '1':
        command_1()
    elif event.keysym == '2':
        command_2()
    elif event.keysym == '3':
        command_3()
    elif event.keysym == '4':
        command_4()
    elif event.keysym == '5':
        command_5()
    elif event.keysym == '6':
        command_6()
    elif event.keysym == '7':
        command_7()
    elif event.keysym == '8':
        command_8()
    elif event.keysym == '9':
        command_9()
    elif event.keysym == '0':
        command_0()
    elif event.keysym == 'plus':
        command_add()
    elif event.keysym == 'minus':
        command_subtract()
    elif event.keysym == 'asterisk':
        command_multiply()
    elif event.keysym == 'slash':
        command_divide()
    elif event.keysym == 'period':
        command_point()  
    
    

def command_answer(_):
    statement = text_box.get()
    # if '+' in statement:
    #     expression = statement.split('+')
    #     try:
    #         answer =(int(expression[0])+int(expression[1]))
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="Green")
    #         text_box.insert(0, answer)
    #     except:
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="RED")
    #         text_box.insert(0, "Error")
    # elif '-' in statement:
    #     expression = statement.split('-')
    #     try:
    #         answer = (int(expression[0])-int(expression[1]))
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="Green")
    #         text_box.insert(0, answer)
    #     except:
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="RED")
    #         text_box.insert(0, "Error")
    # elif 'x' in statement:
    #     expression = statement.split('x')
    #     try:
    #         answer = int(expression[0])*int(expression[1])
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="Green")
    #         text_box.insert(0, answer)
    #     except:
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="RED")
    #         text_box.insert(0, "Error")
    # elif '÷' in statement:
    #     expression = statement.split('÷')
    #     try:
    #         answer = (int(expression[0])/int(expression[1]))
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="Green")
    #         text_box.insert(0, answer)
    #     except:
    #         text_box.delete(0, 'end')
    #         text_box.configure(foreground="RED")
    #         text_box.insert(0, "Error")
    statement = statement.replace('÷', '/')
    answer = eval(statement)
    text_box.delete(0, 'end')
    text_box.configure(foreground="Green")
    text_box.insert(0, answer)

root = Tk()
root.geometry("300x500")
root.resizable(False, False)
root.title("Calculator:- By Maaz")
root.bind("<Return>", command_answer)
root.bind("<Key-1>", handle_keypress)
root.bind("<Key-2>", handle_keypress)
root.bind("<Key-3>", handle_keypress)
root.bind("<Key-4>", handle_keypress)
root.bind("<Key-5>", handle_keypress)
root.bind("<Key-6>", handle_keypress)
root.bind("<Key-7>", handle_keypress)
root.bind("<Key-8>", handle_keypress)
root.bind("<Key-9>", handle_keypress)
root.bind("<Key-0>", handle_keypress)
root.bind("<plus>", handle_keypress)
root.bind("<minus>", handle_keypress)
root.bind("<asterisk>", handle_keypress)
root.bind("<slash>", handle_keypress)
root.bind("<period>", handle_keypress)



text_box = Entry(root, width=10, borderwidth=1,foreground="Blue" ,font=('courier', 25, 'bold'))
text_box.pack()

button_1 = Button(text="1", width=7, height=3, command=command_1, borderwidth=0, background='LIGHT GREY')
button_1.pack()
button_1.place(x=10, y=200)
button_2 = Button(text="2", width=7, height=3, command=command_2, borderwidth=0, background='LIGHT GREY')
button_2.pack()
button_2.place(x=70, y=200)
button_3 = Button(text="3", width=7, height=3, command=command_3, borderwidth=0, background='LIGHT GREY')
button_3.pack()
button_3.place(x=130, y=200)
button_4 = Button(text="4", width=7, height=3, command=command_4, borderwidth=0, background='LIGHT GREY')
button_4.pack()
button_4.place(x=10, y=270)
button_5 = Button(text="5", width=7, height=3, command=command_5, borderwidth=0, background='LIGHT GREY')
button_5.pack()
button_5.place(x=70, y=270)
button_6 = Button(text="6", width=7, height=3, command=command_6, borderwidth=0, background='LIGHT GREY')
button_6.pack()
button_6.place(x=130, y=270)
button_7 = Button(text="7", width=7, height=3, command=command_7, borderwidth=0, background='LIGHT GREY')
button_7.pack()
button_7.place(x=10, y=340)
button_8 = Button(text="8", width=7, height=3, command=command_8, borderwidth=0, background='LIGHT GREY')
button_8.pack()
button_8.place(x=70, y=340)
button_9 = Button(text="9", width=7, height=3, command=command_9, borderwidth=0, background='LIGHT GREY')
button_9.pack()
button_9.place(x=130, y=340)
button_0 = Button(text="0", width=7, height=3, command=command_0, borderwidth=0, background='LIGHT GREY')
button_0.pack()
button_0.place(x=70, y=410)
button_point = Button(text=".", width=7, height=3, command=command_point, borderwidth=0, background='LIGHT GREY')
button_add = Button(text="+", width=7, height=3, command=command_add, background="Orange", borderwidth=0)
button_add.pack()
button_add.place(x=200, y=130)
button_subtract = Button(text="-", width=7, height=3, command=command_subtract, background="Orange", borderwidth=0)
button_subtract.pack()
button_subtract.place(x=200, y=200)
button_multiply = Button(text="x", width=7, height=3, command=command_multiply, background="Orange", borderwidth=0)
button_multiply.pack()
button_multiply.place(x=200, y=270)
button_divide = Button(text="÷", width=7, height=3, command=command_divide, background="Orange", borderwidth=0)
button_divide.pack()
button_divide.place(x=200, y=340)
button_double_zero = Button(text="00", width=7, height=3, command=command_double_zero, borderwidth=0, background='LIGHT GREY')
button_double_zero.pack()
button_double_zero.place(x=10, y=410)
button_three_zero = Button(text="000", width=7, height=3, command=command_three_zero, borderwidth=0, background='LIGHT GREY')
button_three_zero.pack()
button_three_zero.place(x=130, y=410)
button_delete = Button(text="C", width=7, height=3, command=command_delete, foreground="Red", background="Yellow", borderwidth=0)
button_delete.pack()
button_delete.place(x=130, y=130)
button_answer = Button(text="=", width=7, height=3, command=lambda: command_answer(0), background="Light Green", borderwidth=0)
button_answer.pack()
button_answer.place(x=200, y=410)
button_delete_2 = Button(text="CE", width=7, height=3, command=command_delete_2, foreground="Red", background="Yellow", borderwidth=0)
button_delete_2.pack()
button_delete_2.place(x=70, y=130)
root.mainloop()
