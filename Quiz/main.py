def game():
    quiz = {
        "Which keyword is used to define a function in Python?": "def",
        "What is extension of python file?": ".py",
        "Which keyword is used to check a condition?": "if",
        "Set can store Duplicate Values? T/F": "F",
        "This is a very nice course. T/F": "T"
    }
    
    score = 0
    
    for question, answer in quiz.items():
        print(f"\nQ: {question}")
        user_input = input("Your answer: ").lower()
        if user_input == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {answer}")
    
    print(f"\nYour final score: {score} out of {len(quiz)}")

print("WELCOME TO QUIZ GAME")
print("="*20)
input("ENTER TO START")
print("="*20)
game()
