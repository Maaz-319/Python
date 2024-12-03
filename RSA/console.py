from math import gcd
from sympy import randprime
from random import randint
from os import system
from colorama import Fore, Style, init

init(autoreset=True)


def modular_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d


def encrypt(message):
    print(Fore.CYAN + "\nEncrypting...")
    p, q = randprime(3999, 10000), randprime(1000, 10000)

    while p == q:
        p, q = randprime(3999, 10000), randprime(1000, 10000)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = randint(3, phi - 1)  # Public Key
    while gcd(e, phi) != 1:
        e = randint(3, phi - 1)

    d = modular_inverse(e, phi)  # Private Key

    encoded = [ord(c) for c in message]

    print(Fore.YELLOW + "\nPublic Key:")
    print(Fore.GREEN + f"\tn: {n}")
    print(Fore.GREEN + f"\te: {e}")
    print(Fore.YELLOW + "\nPrivate Key:")
    print(Fore.GREEN + f"\td: {d}\n")

    print(f"\n{'='*25}")
    print(Fore.MAGENTA + "\nEncrypted text:")
    for x in [pow(c, e, n) for c in encoded]:
        print(Fore.WHITE + f"{x}", end=' ')
    print(f"\n{'='*25}")

    print("\n")
    start_App()


def decrypt(message, d, n):
    print(Fore.CYAN + "\nDecrypting...")
    message = message.split(' ')
    encoded = [pow(int(c), d, n) for c in message]

    message = [chr(c) for c in encoded]
    msg = "".join(ch for ch in message)
    print(f"\n{'='*25}")
    print(Fore.MAGENTA + f"\nDecrypted Message: {Fore.WHITE}{msg}\n")
    print(f"\n{'='*25}")

    start_App()


def start_App():
    print(Fore.BLUE + """
    Choose an option:
    1) Encrypt
    2) Decrypt
    """)
    choice = int(input(Fore.YELLOW + "Choice > "))
    message = str(input(Fore.CYAN + "Message: "))

    if choice == 1:
        encrypt(message)
    elif choice == 2:
        d = int(input(Fore.YELLOW + "Private Key (d): "))
        n = int(input(Fore.YELLOW + "Public Key (n): "))
        decrypt(message, d, n)
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        start_App()


if __name__ == '__main__':
    system('cls')
    print(Fore.GREEN + """
    ****************************************************
    *                                                  *
    *          WELCOME TO RSA Encryption App           *
    *               AUTHOR -> Maaz Bin Asif            *
    *                                                  *
    ****************************************************
    *                                                  *
    *                RSA ALGORITHM                     *
    *                                                  *
    ****************************************************
    """)
    start_App()
