import socket
from tkinter import *
from tkinter import messagebox
import smtplib


def send_email():
    if "@" not in email_entry.get() or ".com" not in email_entry.get():
        messagebox.showerror("Error", "Enter a valid Send Email")
    elif "@" not in recipient_entry.get() or ".com" not in recipient_entry.get():
        messagebox.showerror("Error", "Enter a valid Recipient Email")
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        try:
            server.login(str(email_entry.get()), str(password_entry.get()))
            server.sendmail(str(email_entry.get()), str(recipient_entry.get()), str(message_entry.get()))
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Your Email or Password is invalid")
        except:
            messagebox.showerror("Error", "There was a Problem while sending Email")



root = Tk()
root.title("Email Sender | by Maaz")
root.geometry("500x500")
root.configure(bg='Light Green')
root.resizable(False, False)

email_entry = Entry(font=('Ariel', 20), border=1, fg='#0f0f0f', width=30)
email_entry.pack(pady=20)

password_entry = Entry(font=('Ariel', 20), border=1, fg='#0f0f0f', width=30, show='•')
password_entry.pack(pady=20)

recipient_entry = Entry(font=('Ariel', 20), border=1, fg='#0f0f0f', width=30)
recipient_entry.pack(pady=20)

message_entry = Text(width=60, height=10)
message_entry.pack(pady=10)

send_button = Button(text='Send', font=('Times new Roman', 20), bg="Light Blue", width=10, command=send_email)
send_button.pack(pady=20)

root.mainloop()
