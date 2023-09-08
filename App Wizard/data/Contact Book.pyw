try:
    from contactbookdata import names
    from contactbookdata import phones
    from contactbookdata import addresses
except:
    file = open('contactbookdata.py', 'w')
    file.write("names = []")
    file.write("\nphones = []")
    file.write("\naddresses = []")
    file.close()
    from contactbookdata import names
    from contactbookdata import phones
    from contactbookdata import addresses

from tkinter import *
from tkinter import ttk, Entry
from tkinter import messagebox
import pyperclip


def search_funtion():
    user_name = str(input_1.get())
    user_name = user_name.upper()
    if user_name not in names:
        messagebox.showerror("Contact Book | by Maaz", "No Contact Found with name '" + user_name + "'")
    else:
        new_root = Tk()
        new_root.title("Search Results")
        new_root.configure(bg='Pink')
        new_root.geometry("500x400")
        new_root.resizable(False, False)

        def copy_name():
            pyperclip.copy(names[index])

        def copy_phone():
            pyperclip.copy(phones[index])

        def copy_address():
            pyperclip.copy(addresses[index])

        Label(new_root, text="Name: ", font=('Ariel', 20, 'underline'), bg='Pink', foreground='Black').place(x=10, y=10)
        Label(new_root, text="Phone#", font=('Ariel', 20, 'underline'), bg='Pink', foreground='Black').place(x=10, y=70)
        Label(new_root, text="Address: ", font=('Ariel', 20, 'underline'), bg='Pink', foreground='Black').place(x=10, y=120)

        found_name = Label(new_root, font=('Ariel', 15), bg='Pink', foreground='Red')
        found_name.place(x=110, y=15)

        found_phone = Label(new_root, font=('Ariel', 15), bg='Pink', foreground='Red')
        found_phone.place(x=110, y=75)

        found_address = Label(new_root, font=('Ariel', 10), bg='Pink', foreground='Red')
        found_address.place(x=1, y=175)

        copy_name_button = Button(new_root, text='copy', bg='Light Green', borderwidth=1, font=('Ariel', 15),
                                  command=copy_name)
        copy_name_button.place(x=400, y=10)

        copy_phone_button = Button(new_root, text='copy', bg='Light Green', borderwidth=1, font=('Ariel', 15),
                                   command=copy_phone)
        copy_phone_button.place(x=400, y=70)

        copy_address_button = Button(new_root, text='copy', bg='Light Green', borderwidth=1, font=('Ariel', 15),
                                     command=copy_address)
        copy_address_button.place(x=400, y=120)

        index = names.index(user_name)
        if addresses[index] == '\n':
            addresses[index] = 'Unknown'
        found_name['text'] = names[index]
        found_phone['text'] = phones[index]
        found_address['text'] = addresses[index]


def save_function():
    user_name = str(input_name.get())
    user_phone = str(input_phone.get())
    user_address = address_box.get(1.0, END)
    if len(user_phone) != 11:
        messagebox.showerror('Contact Book | by Maaz', 'The Number you entered is not valid!')
    else:
        input_name.delete(0, END)
        input_phone.delete(0, END)
        address_box.delete(1.0, END)
        user_address.replace('\n', '')
        user_name = user_name.upper()
        names.append(user_name)
        phones.append(user_phone)
        addresses.append(user_address)
        file = open('contactbookdata.py', 'w')
        file.write("names = " + str(names))
        file.write("\nphones = " + str(phones))
        file.write("\naddresses = " + str(addresses))
        file.close()
        messagebox.showinfo("Contact Book | by Maaz", "Your Contact was saved successfully")


def delete_function():
    name_of_contact = delete_name_entry.get()
    name_of_contact = name_of_contact.upper()
    if name_of_contact not in names:
        messagebox.showerror("Contact Book | By Maaz", "No Contact Found with name '" + str(name_of_contact) + "'")
    else:
        index = names.index(name_of_contact)
        names.remove(names[index])
        phones.remove(phones[index])
        addresses.remove(addresses[index])
        delete_name_entry.delete(0, END)
        file = open('contactbookdata.py', 'w')
        file.write("names = " + str(names))
        file.write("\nphones = " + str(phones))
        file.write("\naddresses = " + str(addresses))
        file.close()
        messagebox.showinfo("Contact Book | by Maaz", "Contact was deleted Successfully")


root = Tk()
root.geometry('500x600')
root.title('Contact Book | By Maaz')
root.resizable(False, False)

notebook = ttk.Notebook(root)

tab_1 = Frame(notebook)
tab_1.configure(bg='Light Green')
tab_2 = Frame(notebook)
tab_2.configure(bg='Light Blue')
tab_3 = Frame(notebook)
tab_3.configure(bg='#fff')

notebook.add(tab_1, text='Find')
notebook.add(tab_2, text='Save')
notebook.add(tab_3, text='Delete')
notebook.pack(expand=True, fill='both')

Label(tab_1, bg='Light Green').pack(pady=80)

search_name = Label(tab_1, text='Enter name Here:', font=('Ariel', 20), background='Light Green')
search_name.pack(padx=20)
input_1 = Entry(tab_1, font=('Ariel', 20, 'bold'), foreground='Red')
input_1.pack(padx=10)
find = Button(tab_1, text='Find', font=('Ariel', 20, 'bold'), background='Yellow', borderwidth=1, foreground='Red',
              command=search_funtion)
find.pack(pady=20)

search_name = Label(tab_2, text='Enter name Here:', font=('Ariel', 20), background='Light Blue')
search_name.pack(padx=20)

input_name = Entry(tab_2, font=('Ariel', 20, 'bold'), foreground='Red')
input_name.pack(padx=10)

search_phone = Label(tab_2, text='Enter phone number Here:', font=('Ariel', 20), background='Light Blue')
search_phone.pack(pady=20)

input_phone = Entry(tab_2, font=('Ariel', 20, 'bold'), foreground='Red')
input_phone.pack(padx=20)

address_box_label = Label(tab_2, text='Enter Address here: (Optional)', font=('Ariel', 20), bg="Light Blue")
address_box_label.pack(pady=10, padx=20)

address_box = Text(tab_2, font=('Ariel', 11), borderwidth=0, width=50, height=5)
address_box.pack(padx=20)

save = Button(tab_2, text='Save', font=('Ariel', 20, 'bold'), background='Pink', borderwidth=1, foreground='Red',
              command=save_function)
save.pack(pady=20)

delete_name_label = Label(tab_3, text='Enter Name here:', font=('Ariel', 15), background='#fff', foreground='Red')
delete_name_label.pack(padx=50, pady=20)

delete_name_entry = Entry(tab_3, font=('Ariel', 15), background='Light Green')
delete_name_entry.pack(padx=50)

delete_contact_button = Button(tab_3, text='Delete', font=('Ariel', 15), background='Light Blue', command=delete_function)
delete_contact_button.pack(padx=50, pady=20)


root.mainloop()
