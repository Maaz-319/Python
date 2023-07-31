"""from tkinter import *
from PIL import Image, ImageTk
import socket
# import threading

IP = socket.gethostname()
port = 1235
client_socket = None
address = None
result1 = ""
result_message = ""
player_2_choice = ""
t = None

init = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
init.bind((IP, port))
init.listen(1024)
root = Tk()


# def connection():
#     global client_socket, address, t
#     computer_choice_label = Label(font=('bahnschrift', 20, 'bold'),
#                                   background="light green", foreground="purple")
#     computer_choice_label.place(x=550, y=350)
#     # computer_choice_label['text'] = IP
#     client_socket, address = init.accept()
#     # global client_socket, address
#     computer_choice_label.config(text="Connected")


def listen(command):
    global player_2_choice, result1, client_socket, address, result_message
    client_socket, address = init.accept()
    player_2_choice = client_socket.recv(1024).decode("utf-8")
    if command == 'r' and player_2_choice == 'r':
        result1 = "0"
    elif command == 'r' and player_2_choice == 'p':
        result1 = "2"
    elif command == 'r' and player_2_choice == 's':
        result1 = "1"
    elif command == 'p' and player_2_choice == 'r':
        result1 = "1"
    elif command == 'p' and player_2_choice == 'p':
        result1 = "0"
    elif command == 'p' and player_2_choice == 's':
        result1 = "2"
    elif command == 's' and player_2_choice == 'r':
        result1 = "2"
    elif command == 's' and player_2_choice == 'p':
        result1 = "1"
    elif command == 's' and player_2_choice == 's':
        result1 = "0"

    if result1 == "0":
        result_message = "Match Tied"
    elif result1 == "1":
        result_message = "Player 1 wins"
    elif result1 == "2":
        result_message = "Player 2 wins"

    client_socket.send(bytes(result_message, "utf-8"))


# t1 = threading.Thread(target=connection)
# t1.start()

root.title("Server")
# root.state('zoomed')

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

# computer_choice_label = Label(font=('bahnschrift', 20, 'bold'),
#                               background="light green", foreground="purple")
# computer_choice_label.place(x=550, y=350)

result = StringVar()
result.set("Result")
result_label = Label(textvariable=result, foreground="red", font=('bahnschrift', 20, 'bold', 'underline'),
                     background="light green")
result_label.place(x=600, y=500)
# rock_image = PhotoImage(file="D:\Rock.png")
# rock_button = Button(text='hello',image=rock_image, borderwidth=0)
# rock_button.pack(side=TOP)
root.mainloop()
"""
import threading
from tkinter import *
from PIL import Image, ImageTk
import socket

IP = socket.gethostname()
port = 1235
client_socket = None
address = None
result1 = ""
result_message = "None"
player_2_choice = "test data"
answer = ""
init = None


def connection():
    global client_socket, address, init
    init = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    init.bind((IP, port))
    init.listen(1024)


root = Tk()


def listen(command):
    global answer
    answer = command
    t3 = threading.Thread(target=decider)
    t3.start()


def decider():
    global player_2_choice, result1, client_socket, address, result_message, answer, init
    result_label['text'] = 'Waiting for Player 2 response'
    print(f"{address} connected")
    client_socket, address = init.accept()
    player_2_choice = client_socket.recv(1024).decode("utf-8")
    print(player_2_choice)
    if answer == 'r' and player_2_choice == 'r':
        result1 = "0"
    elif answer == 'r' and player_2_choice == 'p':
        result1 = "2"
    elif answer == 'r' and player_2_choice == 's':
        result1 = "1"
    elif answer == 'p' and player_2_choice == 'r':
        result1 = "1"
    elif answer == 'p' and player_2_choice == 'p':
        result1 = "0"
    elif answer == 'p' and player_2_choice == 's':
        result1 = "2"
    elif answer == 's' and player_2_choice == 'r':
        result1 = "2"
    elif answer == 's' and player_2_choice == 'p':
        result1 = "1"
    elif answer == 's' and player_2_choice == 's':
        result1 = "0"
    print(result1)
    if result1 == "0":
        result_message = "Match Tied"
    elif result1 == "1":
        result_message = "Player 1 wins"
    elif result1 == "2":
        result_message = "Player 2 wins"
    print(result_message)
    client_socket.send(bytes(result_message, "utf-8"))
    result_label.config(text=result_message)
    client_socket.close()


def tester(com):
    t = threading.Thread(target=listen(com))
    t.start()


t4 = threading.Thread(target=connection)
t4.start()

root.title("Server")

top_label = Label(text="-:(Press the image below):-", font=('Bahnschrift', 15, 'bold'), background="light green")
top_label.place(x=500, y=0)

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

result_label = Label(text="Result Here", foreground="red", font=('bahnschrift', 20, 'bold', 'underline'),
                     background="light green")
result_label.place(x=550, y=500)

root.mainloop()
