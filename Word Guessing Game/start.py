import random
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_MAXIMIZE = 3

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)

Rules = ("\nThere are several words that are stored in this program. You have to guess it in 5 turns."
" There is a secret backdoor key. If you found it word will be revealed\n\n\n\n")
secret_code = "maaz007"
words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
Secret_Word = random.choice(words_to_guess)
length = len(Secret_Word)
print(Rules)
print("Word is ",length," characters long\n")
guess = ""      
guess_Count = 5      #Keep track of how many guess you have made
out_Of_Guesses = False                  
print ("\n\tYou have only 5 turns\n")                       
while guess != Secret_Word and not (out_Of_Guesses) and guess != secret_code:  
    if guess_Count > 0 :
        print("\n\tEnter your guess:-               " , guess_Count, " turns left\n\t")
        guess = input("\n\tGuess: ")
        guess_Count -= 1
    else :
        out_Of_Guesses = True     
if out_Of_Guesses :     
    input ("\nYou Loose!!\n\t Made by Maaz\nThe word was " + Secret_Word)
elif guess == secret_code:
    input ("\nYou found secret key the word was " + Secret_Word)
else :
    input ("\nYou win!!\nMade by Maaz\n")

