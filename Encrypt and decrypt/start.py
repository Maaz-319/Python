import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_MAXIMIZE = 3

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)
import base64
def encrypt():
    message = str(input("Enter Message: "))
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print("\n\n\tEncrypted: " + base64_message)
    input()
def decrypt():
    base64_message = str(input("Enter Message: "))
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print("Decrypted\n\n\t" + message)
    input()

def Runfunc():
    user_choice = input("\n\tChoose:\n\n\t1) Encrypt\n\t2) Decrypt\n\t3) Exit\n\tAnswer: ")
    if user_choice == '1':
        encrypt()
    elif user_choice == '2':
        decrypt()
    elif user_choice == '3':
        exit()
    else:
        Runfunc()
Runfunc()