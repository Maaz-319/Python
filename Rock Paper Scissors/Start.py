import time
import random
count = 0
print("Welcome to Maaz Rock Paper Scissors  game\n")
time.sleep(3)
while count < 3:
    count = count +1
    a = input("Enter 'Rock' 'Paper' 'Scissors ':  ")
    Computer = ["Rock", "Paper", "Scissors"]
    choice = random.choice(Computer)
    time.sleep(2)
    print(choice)
    time.sleep(2)
    if choice == "Rock" and a == "Paper":
        print("You win")
    elif choice == "Paper" and a == "Rock":
        print("You Loose!")
    elif choice == a:
        print("Match Tied")
    elif choice == "Paper" and a == "Scissors":
        print("You win")
    elif a == "Paper" and choice == "Scissors":
        print("You Loose!")
    elif choice == "Rock" and a == "Scissors":
        print("You Loose!")
    elif choice == "Scissors" and a == "Rock":
        print("You Win")
    else:
        print("Please enter a valid choice")
input("")
