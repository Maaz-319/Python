from math import gcd
from  sympy import randprime
from random import randint
from os import system


def modular_inverse(e, phi):
		for d in range(3, phi):
			if (d * e) % phi == 1:
				return d


def encrypt(message):
	print("Encrypting...")
	p, q = randprime(3999, 10000), randprime(1000, 10000)

	while p == q:
		p, q = randprime(3999, 10000), randprime(1000, 10000)

	n = p*q
	phi = (p-1) * (q-1)

	e = randint(3, phi-1) # Public Key
	while gcd(e, phi) != 1:
		e = randint(3, phi-1)


	d = modular_inverse(e, phi) # Private Key

	encoded = [ord(c) for c in message]

	print(f"Public Key:\n\tn:{n}\n\td:{d}\n")

	print("\n\nEncrypted text:")
	for x in [pow(c, e, n) for c in encoded]:
		print(f"{x}", end=' ')

	start_App()


def decrypt(message, d, n):
	message = message.split(' ')
	encoded = [pow(int(c), d, n) for c in message]

	message = [chr(c) for c in encoded]
	msg = "".join (ch for ch in message)
	print(f"Message: {msg}")

	start_App()


def start_App():
	choice = int(input("\n\n\n1) Encrypt\n2) Decrypt\n\nChoice > "))
	message = str(input("Message: "))

	if choice == 1:
		encrypt(message)
	elif choice == 2:
		d = int(input("d: "))
		n = int(input("n: "))
		decrypt(message, d, n)
	else:
		while(choice not in [1, 2]):
			choice = int(input("\n1) Encrypt\n2)Decrypt\n\nChoice >"))


if __name__ == '__main__':
	system('cls')
	print("""
    ****************************************************
    *                                                  *
    *              WELCOME TO RSA Encryption           *
    *               AUTHOR -> Maaz Bin Asif            *
    *                                                  *
    ****************************************************
    *                                                  *
    *     This App encrypts and decrypts using RSA     *
    *                                                  *
    ****************************************************
    """)

	start_App()
