import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_MAXIMIZE = 3

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)
import base64
def Encode():
    message = str(input("Enter Message: "))
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print("\n\n\tEncodeed: " + base64_message)
    input()
def Decode():
    base64_message = str(input("Enter Message: "))
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print("Decodeed\n\n\t" + message)
    input()

def Runfunc():
    user_choice = input("\n\tChoose:\n\n\t1) Encode\n\t2) Decode\n\t3) Exit\n\tAnswer: ")
    if user_choice == '1':
        Encode()
    elif user_choice == '2':
        Decode()
    elif user_choice == '3':
        exit()
    else:
        Runfunc()
Runfunc()