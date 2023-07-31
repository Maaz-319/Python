import random


def game():
    choice = random.randint(0, 50)
    Guesses = 10
    UserInput = ""
    secret_code = 753951
    while Guesses != 0 and UserInput is not choice and UserInput != secret_code:
        print("\n\n\t" , Guesses , " turns left\n\n")
        try:
            UserInput = int(input("Enter Your Guess(Between 1 and 50): "))
        except:
            print("Enter valid number")
            game()
        if UserInput < choice:
            print("Your number is smaller\n")
        elif UserInput == secret_code:
            print("You have found secret key. You won!!!. Number was " , choice)
        
        elif UserInput > choice:
            print("Your number is larger\n")
        elif UserInput == choice:
            print("Yes You won!!")
        else:
            print("try again")
        Guesses = Guesses - 1
    input("\nThanks for playing Maaz Number guessing game")


def again():
    hello = input("\n\tChoose: \n\t1) Play again\n\t2) exit\n\tAnswer: ")
    if hello == '1':
        game()
    elif hello == '2':
        exit()
    else:
        again()


print(game())
print(again())

