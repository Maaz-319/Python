from tkinter import *
from PIL import Image, ImageTk
import socket
import threading

IP = socket.gethostname()
port = 1235
client_socket = None
result_message = ""
player_1_choice = ""
rec = None


def connection():
    global result_label, rec
    rec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rec.connect((IP, port))
    # result_label['text'] = 'Connected'


def listen(command):
    global client_socket, player_1_choice, result_message, rec
    player_1_choice = rec.send(bytes(command, "utf-8"))
    rec.send(bytes(command, "utf-8"))
    result_message = rec.recv(1024).decode("utf-8")
    result_label['text'] = str(result_message)
    connection()


t = threading.Thread(target=connection)
t.start()

root = Tk()
root.title("Client")
root.state('zoomed')

top_label = Label(text="-:(Press the image below):-", font=('Bahnschrift', 15, 'bold'), background="light green")
top_label.place(x=500, y=0)

top_label = Label(font=('Bahnschrift', 15, 'bold'), background="light green")

rock_img = Image.open("images/default.png")
rock_img = rock_img.resize((200, 200))
rimg = ImageTk.PhotoImage(rock_img)
rock_button = Button(image=rimg, foreground="Red", borderwidth=0, background="Yellow", command=lambda: listen('r'))
rock_button.place(x=300, y=100)

paper_img = Image.open("images/paper.png")
paper_img = paper_img.resize((200, 200))
pimg = ImageTk.PhotoImage(paper_img)
paper_button = Button(image=pimg, borderwidth=0, background="Yellow", command=lambda: listen('p'))
paper_button.place(x=550, y=100)

scissor_img = Image.open("images/scissor.png")
scissor_img = scissor_img.resize((200, 200))
simg = ImageTk.PhotoImage(scissor_img)
scissors_button = Button(image=simg, borderwidth=0, background="Yellow", command=lambda: listen('s'))
scissors_button.place(x=800, y=100)

result_label = Label(text='Result Here', foreground="red", font=('bahnschrift', 20, 'bold', 'underline'),
                     background="light green")
result_label.place(x=550, y=500)
# rock_image = PhotoImage(file="D:\Rock.png")
# rock_button = Button(text='hello',image=rock_image, borderwidth=0)
# rock_button.pack(side=TOP)
root.mainloop()
