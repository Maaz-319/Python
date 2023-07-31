while True:
    user_input = input("\n\tEnter a string: ")
    l = len(user_input)
    l = l * -1
    a = -1
    while a >= l:
        
        print("\n\t",user_input[a])
        a -= 1