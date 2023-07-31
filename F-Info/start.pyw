from faker import Faker
from tkinter import *
from faker.providers import internet

fake = Faker()


def function(temp):
    if temp == 'name':
        text_box.delete(1.0, END)
        text_box.insert(1.0, fake.name())
    elif temp == 'address':
        text_box.delete(1.0, END)
        text_box.insert(1.0, fake.address())
    elif temp == 'text':
        text_box.delete(1.0, END)
        text_box.insert(1.0, fake.text())
    elif temp == 'ip':
        fake.add_provider(internet)
        text_box.delete(1.0, END)
        text_box.insert(1.0, fake.ipv4_private())
    elif temp == 'sentence':
        text_box.delete(1.0, END)
        text_box.insert(1.0, fake.sentence())


root = Tk()
root.title('Faker')
root.geometry('400x550')
root.resizable(False, False)
root.configure(bg='Black')

text_box = Text(font=('Times', 15), width=25, height=10, bg='White', fg='red')
text_box.pack()

name = Button(text='Name', font=('Ariel', 17), command=lambda: function('name'), bg='light green')
name.pack(pady=10)

address = Button(text='Address', font=('Ariel', 17), command=lambda: function('address'), bg='light green')
address.pack(pady=10)

text = Button(text='Text', font=('Ariel', 17), command=lambda: function('text'), bg='light green')
text.pack(pady=10)

ip = Button(text='ip', font=('Ariel', 17), command=lambda: function('ip'), bg='light green')
ip.pack(pady=10)

sentence = Button(text='sentence', font=('Ariel', 17), command=lambda: function('sentence'), bg='light green')
sentence.pack(pady=10)
root.mainloop()
