
#----------------------------Import Modules+bnksysdata-------------------------------

from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
try:
    from bnksysdata import names
    from bnksysdata import moneys
    from bnksysdata import pins
except:
    file = open('bnksysdata.py', 'w')
    file.write('names = []\nmoneys = []\npins = []')
    file.close()
    from bnksysdata import names
    from bnksysdata import moneys
    from bnksysdata import pins

# Functions of Buttons
#------------------------create account function--------------------------
def create_account():
    global names, moneys, pins
    name = str(entry_n_c.get())
    if name not in names:

        # Checks if ammount of money is correct
        try:
            money = int(entry_m_c.get())
        except ValueError:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror('Bank', 'Enter correct ammount of money')
            
        # Check if a pin is a valid pin
        try:
            pin = int(entry_p_c.get())
        except ValueError:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror('Bank', 'Enter correct Pin')
        pin = str(pin)
        if len(pin) != 4:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror('Bank', 'Length of pin must be 4-digits')
        pin = int(pin)
        names.append(name)
        moneys.append(money)
        pins.append(pin)
        file = open('bnksysdata.py', 'w')
        file.write('names = ' + str(names))
        file.write('\nmoneys = ' + str(moneys))
        file.write('\npins = ' + str(pins))
        file.close()
        from bnksysdata import names
        entry_n_c.delete(0, END)
        entry_m_c.delete(0, END)
        entry_p_c.delete(0, END)
        messagebox.showinfo("Bank", 'Your account was created successfully.')
        result = str("Account Name: " + name + '\nBalance: ' + str(money))
        label_result_c.configure(text=result)
    else:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror('Bank', 'An account with this name already exists')

#-----------------------------deposit money function----------------------------

def deposit_account():
    global names, moneys, pins
    name = str(entry_n_d.get())
    if name not in names:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror("Bank", 'No account with this name was found')
    else:
        try:
            money = int(entry_m_d.get())
        except ValueError:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror('Bank', 'Enter correct ammount of money')
        try:
            pin = int(entry_p_d.get())
        except ValueError:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror('Bank', 'Enter correct Pin')
        index = names.index(name)
        if pin == pins[index]:
            moneys[index] = moneys[index] + money
            file = open('bnksysdata.py', 'w')
            file.write('names = ' + str(names))
            file.write('\nmoneys = ' + str(moneys))
            file.write('\npins = ' + str(pins))
            file.close()
            from bnksysdata import names
            from bnksysdata import moneys
            from bnksysdata import pins
            entry_n_d.delete(0, END)
            entry_m_d.delete(0, END)
            entry_p_d.delete(0, END)
            result = str("Account Name: " + name + '\nBalance: ' + str(moneys[index]))
            label_result_d.configure(text=result)
        else:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror("Bank", 'Incorrect Pin')

#----------------------------withdraw money function---------------------------

def withdraw_account():
    global names, moneys, pins
    name = str(entry_n_w.get())
    try:
        money = int(entry_m_w.get())
    except ValueError:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror('Bank', 'Enter correct ammount of money')
    try:
        pin = int(entry_p_w.get())
    except ValueError:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror('Bank', 'Enter correct Pin')
    index = names.index(name)
    if pin == pins[index]:
        if money <= moneys[index]:
            moneys[index] = moneys[index] - money
            file = open('bnksysdata.py', 'w')
            file.write('names = ' + str(names))
            file.write('\nmoneys = ' + str(moneys))
            file.write('\npins = ' + str(pins))
            file.close()
            from bnksysdata import names
            from bnksysdata import moneys
            from bnksysdata import pins
            entry_n_w.delete(0, END)
            entry_m_w.delete(0, END)
            entry_p_w.delete(0, END)
            result = str("Account Name: " + name + '\nBalance: ' + str(moneys[index]))
            label_result_w.configure(text=result)
        else:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror("Bank", "There are not enough money in your account")
    else:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror("Bank", 'Incorrect Pin')

#----------------------------delete account function------------------------

def delete_account():
    global names, moneys, pins#from bnksysdata import names, moneys, pins
    name = str(entry_n_de.get())
    try:
        pin = int(entry_p_de.get())
    except ValueError:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror('Bank', 'Enter correct Pin')
    if name not in names:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror("Bank", "No account found with this name")
    else:
        index = names.index(name)
        if pin == pins[index]:
            names.remove(name)
            moneys.remove(moneys[index])
            pins.remove(pins[index])
            file = open('bnksysdata.py', 'w')
            file.write('names = ' + str(names))
            file.write('\nmoneys = ' + str(moneys))
            file.write('\npins = ' + str(pins))
            file.close()
            entry_n_de.delete(0, END)
            entry_p_de.delete(0, END)
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showinfo("Bank", "Account was deleted successfully")
        else:
            label_result_f.configure(text='')
            label_result_c.configure(text='')
            label_result_w.configure(text='')
            label_result_d.configure(text='')
            messagebox.showerror("Bank", "Incorrect Pin")

#----------------------------------Find account function-------------------------

def find_account():
    global names, moneys
    name = str(entry_n_f.get())
    entry_n_f.delete(0, END)
    if name in names:
        index = names.index(name)
        result = "Results:\n\nName: " + str(name) + '\nBalance: ' + str(moneys[index])
        label_result_f.configure(text=result)
    else:
        label_result_f.configure(text='')
        label_result_c.configure(text='')
        label_result_w.configure(text='')
        label_result_d.configure(text='')
        messagebox.showerror("Bank", "No account found with this name.")
                
#----------------------------------Page Layout-----------------------------------

colours_list = ["Light Green", "Light Blue", "Pink"]
colour = random.choice(colours_list)

root = Tk()
notebook = ttk.Notebook(root)
root.geometry('500x650')
root.title('Bank Management System | By Maaz')

crt_tab = Frame(notebook, background=colour)
dp_tab = Frame(notebook, background=colour)
wd_tab = Frame(notebook, background=colour)
del_tab = Frame(notebook, background=colour)
fnd_tab = Frame(notebook, background=colour)

notebook.add(crt_tab, text='Create Account')
notebook.add(dp_tab, text='Deposit Money')
notebook.add(wd_tab, text='Withdraw Money')
notebook.add(del_tab, text='Delete Account')
notebook.add(fnd_tab, text='Find Account')
notebook.pack(expand=True, fill='both')

#--------------------------------------------create_tab-------------------------------------------------------------------------------

entry_n_c = Entry(crt_tab, font=('Ariel', 15), foreground='Purple')
entry_m_c = Entry(crt_tab, font=('Ariel', 15), foreground='purple')
entry_p_c = Entry(crt_tab, font=('Ariel', 15), foreground='purple', show='•')

label_n_c = Label(crt_tab, text='Enter Name for account:', font=('Ariel', 20), background=colour)
label_m_c = Label(crt_tab, text='Enter Initial ammount of Money:', font=('Ariel', 20), background=colour)
label_p_c = Label(crt_tab, text='Enter Pin (4-digit)', font=('Ariel:', 20), background=colour)
label_result_c = Label(crt_tab, font=('Ariel', 20), background=colour)

button_c = Button(crt_tab, text='Create',  font=('Ariel:', 20), background='Black', foreground='White', borderwidth=0, command=create_account)

label_n_c.pack(pady=20)
entry_n_c.pack()
label_m_c.pack(pady=20)
entry_m_c.pack()
label_p_c.pack(pady=20)
entry_p_c.pack()
button_c.pack(pady=20)
label_result_c.pack(pady=30)

#----------------------------------------------deposit_tab-------------------------------------------------------------------------------

entry_n_d = Entry(dp_tab, font=('Ariel', 15), foreground='purple')
entry_m_d = Entry(dp_tab, font=('Ariel', 15), foreground='purple')
entry_p_d = Entry(dp_tab, font=('Ariel', 15), foreground='purple', show='•')

label_n_d = Label(dp_tab, text='Enter Name of your account:', font=('Ariel', 20), background=colour)
label_m_d = Label(dp_tab, text='Enter ammount of Money to deposit:', font=('Ariel', 20), background=colour)
label_p_d = Label(dp_tab, text='Enter your Pin:', font=('Ariel', 20), background=colour)
label_result_d = Label(dp_tab, font=('Ariel', 20), background=colour)

button_d = Button(dp_tab, text='Deposit',  font=('Ariel:', 20), background='Black', foreground='White', borderwidth=0, command=deposit_account)

label_n_d.pack(pady=20)
entry_n_d.pack()
label_m_d.pack(pady=20)
entry_m_d.pack()
label_p_d.pack(pady=20)
entry_p_d.pack()
button_d.pack(pady=20)
label_result_d.pack(pady=30)

#-------------------------------------------withdraw_tab-------------------------------------------------------------------------------

entry_n_w = Entry(wd_tab, font=('Ariel', 15), foreground='purple')
entry_m_w = Entry(wd_tab, font=('Ariel', 15), foreground='purple')
entry_p_w = Entry(wd_tab, font=('Ariel', 15), foreground='purple', show='•')

label_n_w = Label(wd_tab, text='Enter Name of your account:', font=('Ariel', 20), background=colour)
label_m_w = Label(wd_tab, text='Enter ammount of Money to withdraw:', font=('Ariel', 20), background=colour)
label_p_w = Label(wd_tab, text='Enter your Pin:', font=('Ariel', 20), background=colour)
label_result_w = Label(wd_tab, font=('Ariel', 20), background=colour)

button_w = Button(wd_tab, text='Withdraw',  font=('Ariel:', 20), background='Black', foreground='White', borderwidth=0, command=withdraw_account)

label_n_w.pack(pady=20)
entry_n_w.pack()
label_m_w.pack(pady=20)
entry_m_w.pack()
label_p_w.pack(pady=20)
entry_p_w.pack()
button_w.pack(pady=20)
label_result_w.pack(pady=30)

#---------------------------------------------delete_tab-------------------------------------------------------------------------------

entry_n_de = Entry(del_tab, font=('Ariel', 15), foreground='purple')
entry_p_de = Entry(del_tab, font=('Ariel', 15), foreground='purple', show='•')

label_n_de = Label(del_tab, text='Enter Name of your account:', font=('Ariel', 20), background=colour)
label_p_de = Label(del_tab, text='Enter your Pin:', font=('Ariel', 20), background=colour)

button_de = Button(del_tab, text='Delete',  font=('Ariel:', 20), background='Black', foreground='White', borderwidth=0, command=delete_account)

label_n_de.pack(pady=20)
entry_n_de.pack()
label_p_de.pack(pady=20)
entry_p_de.pack()
button_de.pack(pady=20)

#---------------------------------------------find_tab-------------------------------------------------------------------------------

entry_n_f = Entry(fnd_tab, font=('Ariel', 15), foreground='purple')

label_n_f = Label(fnd_tab, text='Enter Name of the account:', font=('Ariel', 20), background=colour)
label_result_f = Label(fnd_tab,font=('Ariel', 20), background=colour)

button_f = Button(fnd_tab, text='Find',  font=('Ariel:', 20), background='Black', foreground='White', borderwidth=0, command=find_account)

label_n_f.pack(pady=20)
entry_n_f.pack()
label_result_f.pack(pady=30)
button_f.pack(pady=20)


root.mainloop()
