from math import gcd as gcd
import tkinter as maaz
from random import randint
import ttkbootstrap as maazb
from tkinter import messagebox
from Crypto.Util import number
import webbrowser
from tkinter import filedialog
import pickle


class GUI:
    def __init__(self, key_bit_length):
        self.root = maaz.Tk()
        self.root.title("RSA Encryption ⸻ by | Maaz Bin Asif")
        self.root.state('zoomed')
        self.root.resizable(False, False)

        self.key_bit_length = key_bit_length

        self.create_tabs()
        self.create_encrypt_tab_widgets()
        self.create_decrypt_tab_widgets()
        self.create_keys_tab_widgets()

    @staticmethod
    def contact_us(_):
        webbrowser.open_new_tab("https://maaz.me/#contact")

    def create_tabs(self):
        self.tabs = maazb.Notebook(self.root)
        self.tabs.pack(fill='both', expand=True)

        self.tab1 = maazb.Frame(self.tabs)
        self.tab2 = maazb.Frame(self.tabs)
        self.tab3 = maazb.Frame(self.tabs)

        self.tabs.add(self.tab1, text='Encrypt')
        self.tabs.add(self.tab2, text='Decrypt')
        self.tabs.add(self.tab3, text='New Keys')

        self.contact_us_label = maaz.Label(self.root, text="Contact Us", foreground='white', cursor='hand2')
        self.contact_us_label.pack()
        self.contact_us_label.bind("<Button-1>", self.contact_us)


    def create_encrypt_tab_widgets(self):
        self.encrypt_label = maazb.Label(self.tab1, text='Enter the Message:', font=('Arial', 20))
        self.encrypt_label.place(x=10, y=10)
        self.encrypt_text_1 = maazb.Text(self.tab1, height=8, width=120, font=('Arial', 14))
        self.encrypt_text_1.place(x=10, y=50)

        maazb.Label(self.tab1, text='Public Key(n):', font=('Arial', 20)).place(x=10, y=250)
        self.public_key_entry_1 = maazb.Entry(self.tab1, font=('Arial', 14), foreground="light green")
        self.public_key_entry_1.place(x=210, y=250)

        maazb.Label(self.tab1, text='Private Key(d):', font=('Arial', 20)).place(x=460, y=250)
        self.private_key_entry_1 = maazb.Entry(self.tab1, font=('Arial', 14), foreground="red")
        self.private_key_entry_1.place(x=650, y=250)

        maazb.Label(self.tab1, text='Public Key(e):', font=('Arial', 20)).place(x=890, y=250)
        self.private_key_entry_1_e = maazb.Entry(self.tab1, font=('Arial', 14), foreground="light green")
        self.private_key_entry_1_e.place(x=1090, y=250)

        self.encrypt_button = maaz.Button(self.tab1, text='Encrypt', command=self.encrypt, font=('Arial', 20),
                                          cursor='hand2')
        self.encrypt_button.place(x=400, y=320)

        self.import_from_file_button = maaz.Button(self.tab1, text='Import Keys', command=self.import_from_file,
                                                    font=('Arial', 20), cursor='hand2')
        self.import_from_file_button.place(x=800, y=320)

        maazb.Label(self.tab1, text='Result:', font=('Arial', 20)).place(x=10, y=400)
        self.output_text_1 = maazb.Text(self.tab1, height=8, width=120, font=('Arial', 14))
        self.output_text_1.place(x=10, y=450)

    def create_decrypt_tab_widgets(self):
        self.decrypt_label = maazb.Label(self.tab2, text='Enter the Message:', font=('Arial', 20))
        self.decrypt_label.place(x=10, y=10)
        self.decrypt_text_2 = maazb.Text(self.tab2, height=8, width=120, font=('Arial', 14))
        self.decrypt_text_2.place(x=10, y=50)

        maazb.Label(self.tab2, text='Public Key(n):', font=('Arial', 20)).place(x=100, y=250)
        self.public_key_entry_2 = maazb.Entry(self.tab2, font=('Arial', 14), foreground="light green")
        self.public_key_entry_2.place(x=300, y=250)

        maazb.Label(self.tab2, text='Private Key(d):', font=('Arial', 20)).place(x=650, y=250)
        self.private_key_entry_2 = maazb.Entry(self.tab2, font=('Arial', 14), show='•', foreground="red")
        self.private_key_entry_2.place(x=840, y=250)

        self.decrypt_button = maaz.Button(self.tab2, text='Decrypt', command=self.decrypt, font=('Arial', 20),
                                          cursor='hand2')
        self.decrypt_button.place(x=600, y=320)

        maazb.Label(self.tab2, text='Result:', font=('Arial', 20)).place(x=10, y=400)
        self.output_text_2 = maazb.Text(self.tab2, height=10, width=120, font=('Arial', 14))
        self.output_text_2.place(x=10, y=450)
    
    def create_keys_tab_widgets(self):
        self.generate_keys_button = maaz.Button(self.tab3, text='Generate Keys', command=self.generate_keys,
                                                font=('Arial', 20), cursor='hand2')
        self.generate_keys_button.pack(pady=10)

        maazb.Label(self.tab3, text='Public Key(n):', font=('Arial', 20)).pack(pady=10)
        self.public_key_entry_3 = maazb.Entry(self.tab3, font=('Arial', 14), foreground="light green", width=70)
        self.public_key_entry_3.pack(pady=10)

        maazb.Label(self.tab3, text='Private Key(d):', font=('Arial', 20)).pack(pady=10)
        self.private_key_entry_3 = maazb.Entry(self.tab3, font=('Arial', 14), foreground="red", width=70)
        self.private_key_entry_3.pack(pady=10)

        maazb.Label(self.tab3, text='Public Key(e):', font=('Arial', 20)).pack(pady=10)
        self.public_key_entry_3_e = maazb.Entry(self.tab3, font=('Arial', 14), foreground="light green", width=70)
        self.public_key_entry_3_e.pack(pady=10)

        self.save_to_file_button = maaz.Button(self.tab3, text='Save Keys', command=self.save_to_file,
                                                  font=('Arial', 20), cursor='hand2')
        self.save_to_file_button.pack(pady=50)

    def generate_keys(self):
        p = number.getPrime(self.key_bit_length // 2)
        q = number.getPrime(self.key_bit_length // 2)

        n = p * q
        phi = (p - 1) * (q - 1)

        e = randint(3, phi - 1)
        while gcd(e, phi) != 1:
            e = randint(3, phi - 1)

        d = number.inverse(e, phi)
        
        self.public_key_entry_3.delete(0, 'end')
        self.private_key_entry_3.delete(0, 'end')
        self.public_key_entry_3_e.delete(0, 'end')

        self.public_key_entry_3.insert(0, f'{n}')
        self.private_key_entry_3.insert(0, f'{d}')
        self.public_key_entry_3_e.insert(0, f'{e}')

    def encrypt(self):
        message = self.encrypt_text_1.get('1.0', 'end-1c')

        if not message:
            messagebox.showerror('Error', 'Message Empty!')
            return

        n, d, e = int(self.public_key_entry_1.get()), int(self.private_key_entry_1.get()), int(self.private_key_entry_1_e.get())

        if not n or not d or not e:
            messagebox.showerror('Error', 'Keys Empty!')
            return
     
        encrypted_message = [pow(ord(char), e, n) for char in message]
        encrypted_message = ' '.join(map(str, encrypted_message))

        self.output_text_1.delete('1.0', 'end')
        self.output_text_1.insert('1.0', encrypted_message)

    def decrypt(self):
        message = self.decrypt_text_2.get('1.0', 'end-1c')
        if not message:
            messagebox.showerror('Error', 'Message Empty!')
            return
        try:
            n = int(self.public_key_entry_2.get().split(':')[-1].strip())
            d = int(self.private_key_entry_2.get().split(':')[-1].strip())
        except ValueError:
            messagebox.showerror('Error', 'Invalid Public Key or Private Key!')
            return

        decrypted_message = [chr(pow(int(char), d, n)) for char in message.split()]
        decrypted_message = ''.join(decrypted_message)

        self.output_text_2.delete('1.0', 'end')
        self.output_text_2.insert('1.0', decrypted_message)
    
    def save_to_file(self):

        data = f"{self.public_key_entry_3.get()}\n{self.private_key_entry_3.get()}\n{self.public_key_entry_3_e.get()}"

        if not data:
            return
        elif not self.public_key_entry_3.get() or not self.private_key_entry_3.get() or not self.public_key_entry_3_e.get():
            messagebox.showerror('Error', 'Key Empty Error! Not all keys are there, Generate New Keys!')
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Binary File",
            filetypes=[("Binary files", "*.bin")]
        )
        if file_path:
            with open(file_path, "wb") as file:
                pickle.dump(data, file)
    
    def import_from_file(self):
        file_path = filedialog.askopenfilename(
        title="Open Binary File",
        filetypes=[("Binary files", "*.bin")]
        )
    
        if file_path:
            with open(file_path, "rb") as file:
                data = pickle.load(file)
                data = data.split('\n')
                
                self.public_key_entry_1.delete(0, 'end')
                self.private_key_entry_1.delete(0, 'end')
                self.private_key_entry_1_e.delete(0, 'end')

                self.public_key_entry_1.insert(0, f'{data[0]}')
                self.private_key_entry_1.insert(0, f'{data[1]}')
                self.private_key_entry_1_e.insert(0, f'{data[2]}')
            

if __name__ == '__main__':
    gui = GUI(key_bit_length=80)
    maazb.Style().theme_use('darkly')
    gui.root.mainloop()
