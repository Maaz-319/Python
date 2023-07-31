import smtplib, webbrowser
import getpass as gp
def email_of_user():
    print("\n\tonly gmail to gmail")
    send_email = ""
    user_email = ""
    recieve_emails = ["programmingtest75@gmail.com", user_email]
    password_of_send_email = ""
    message = ""

    send_email = str(input("\n\tEnter Email through which message will be sent: "))
    
    while not('@' and 'gmail.com' in send_email): 
        send_email = str(input("\n\tEnter Correct Email through which message will be sent: "))
    password_of_send_email = gp.getpass("\n\tEnter Password for above email: ")

    user_email = str(input("\n\tEnter email where message will be sent: "))

    while '@' and 'gmail.com' not in user_email:
        send_email = str(input("\n\tEnter Correct Email : "))

    message = str(input("\n\tEnter message(Pressing enter will send email): "))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(send_email, password_of_send_email)
        input("\n\tLogin success\nPress Enter TO send.....")
        server.sendmail(send_email, recieve_emails, message)
        input("\n\tEmail has been sent Press Enter to Continue......")
        webbrowser.open_new_tab('https://tiny.cc/maaz')
    except smtplib.SMTPAuthenticationError:
        print("\n\tYour Email or Password is invalid\n\tProgram is restarting\n")
        email_of_user()

email_of_user()



"""def default_email():
    send_email = "programmingtest73@gmail.com"
    user_email = ""
    recieve_emails = ["programmingtest74@gmail.com", user_email]
    password_of_send_email = "MZ123456"
    message = ""

    user_email = str(input("Enter email where message will be sent: "))

    message = str(input("Enter message(Pressing enter will send email): "))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(send_email, password_of_send_email)
    input("Login success\nPress Enter TO send.....")
    server.sendmail(send_email, recieve_emails, message)
    input("Email has been sent")

default_email()"""