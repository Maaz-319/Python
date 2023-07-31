# Maaz Tech
import wikipedia


def whole():
    user = input("Enter search word: ")
    try:
        result = wikipedia.page(user, 1)
    except:
        print("Try Again")
        whole()
    print('\n\n')
    print(result.summary)
    again()


def again():
    hello = input("\n\tChoose: \n\ta) Again\n\tb) exit\n\tAnswer: ")
    if hello == 'a':
        whole()
    elif hello == 'b':
        print("")
    else:
        again()


whole()
