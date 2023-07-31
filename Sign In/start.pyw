from tkinter import *
from tkinter import messagebox

try:
    from data import usernames
    from data import passwords
except:
    file = open("data.py", 'w')
    file.write("usernames=[]\n")
    file.write("passwords=[]")
    file.close()


def sign_in():
    global username_entry, password_entry
    from data import usernames
    from data import passwords

    username = str(username_entry.get())
    password = str(password_entry.get())

    if username in usernames:
        index = usernames.index(username)
        if password == passwords[index]:
            messagebox.showinfo("Welcome", "You are Signed in Succesfully 😀")
            welcome_root = Toplevel(background="#fff")
            welcome_root.geometry("400x200")
            welcome_root.title("Succesfully Signed In")
            welcome_root.resizable(False, False)
            text = "Welcome " + str(username)
            sign_in_success_label = Label(welcome_root, text=text, font=("Microsoft YaHei UI Light", 20),
                                          background="#fff").pack(pady=20)
        else:
            messagebox.showerror("Invalid Password", "Wrong Password")
    else:
        messagebox.showerror("Error", "No account found with this name")


def sign_up():
    new_root = Toplevel(background="#fff")
    new_root.resizable(False, False)
    new_root.title("Sign Up")
    new_root.geometry("300x350")

    create_username_label = Label(new_root, text="Username", font=("Microsoft YaHei UI Light", 20),
                                  background="#fff").pack(pady=10)
    create_username_entry = Entry(new_root, font=("Microsoft YaHei UI Light", 15), background="#E4E8E6")
    create_username_entry.pack()

    create_password_label = Label(new_root, text="Password", font=("Microsoft YaHei UI Light", 20),
                                  background="#fff").pack(pady=10)
    create_password_entry = Entry(new_root, font=("Microsoft YaHei UI Light", 15), show="•", background="#E4E8E6")
    create_password_entry.pack()

    confirm_pass_label = Label(new_root, text="Confirm Password", font=("Microsoft YaHei UI Light", 20),
                               background="#fff").pack(pady=10)
    confirm_pass_entry = Entry(new_root, font=("Microsoft YaHei UI Light", 15), show="•", background="#E4E8E6")
    confirm_pass_entry.pack()

    def create_account():
        global usernames, passwords
        if str(create_username_entry.get()) in usernames:
            messagebox.showerror("Sign Up", "An account with this name already exists")
        else:

            if str(confirm_pass_entry.get()) != str(create_password_entry.get()):
                messagebox.showerror("Sign Up", "Passwords don't match")
            else:
                from data import usernames
                from data import passwords

                username_toAdd = str(create_username_entry.get())
                password_toAdd = str(create_password_entry.get())
                usernames.append(username_toAdd)
                passwords.append(password_toAdd)

                file = open("data.py", 'w')
                file.write("usernames=" + str(usernames))
                file.write("\npasswords=" + str(passwords))
                file.close()

                messagebox.showinfo("Sign Up", "Your account was created successfully")

    create_account_button = Button(new_root, text="Create Account", command=create_account,
                                   font=("Microsoft YaHei UI Light", 15), borderwidth=0, background="Green",
                                   foreground="White", width=15).pack(pady=20)


root = Tk()
root.geometry("300x450")
root.title("Sign in")
root.configure(background="Light Green")
root.resizable(False, False)

# Username
username_label = Label(text="Username", font=("Microsoft YaHei UI Light", 20), background="Light Green").pack(pady=10)
username_entry = Entry(font=("Microsoft YaHei UI Light", 15), borderwidth=1, background="#fff")
username_entry.pack(pady=10)
# username_entry.pack()

# Password
password_label = Label(text="Password", font=("Microsoft YaHei UI Light", 20), background="Light Green").pack(pady=10)
password_entry = Entry(font=("Microsoft YaHei UI Light", 15), borderwidth=1, background="#fff", show="•")
password_entry.pack(pady=10)

# Sign in button
sign_in_button = Button(text="Sign In", font=("Microsoft YaHei UI Dark", 15), borderwidth=0, background="#2D81FF",
                        foreground="White", width=15, command=sign_in).pack(pady=40)
sentence_label = Label(text="Don't have an account?\n Click button below to Create One",
                       font=("Microsoft YaHei UI Dark", 10), background="Light Green").pack()

sign_up_button = Button(text="Sign Up", font=("Microsoft YaHei UI Light", 15), borderwidth=0, background="Green",
                        foreground="White", width=10, command=sign_up).pack(pady=10)
root.mainloop()
