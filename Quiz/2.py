from colorama import init, Fore, Back, Style
import webbrowser

# essential for Windows environment
init()
red1 = [Fore.RED]
green1 = [Fore.GREEN]
BRIGHTNESS = [Style.BRIGHT ]


def print_with_color(s, color=Fore.GREEN, brightness=Style.BRIGHT, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

# printing all available foreground colors with different brightness



















Total_Marks = int(0)
answers1 = True
answers2 = True
answers3 = True
answers4 = True
answers5 = True
answers6 = True
answers7 = True
answers8 = True

falseAnswers = "You have entered wrong answer of following::\n "

print("Please enter a ,b or c")
userReply1 = input ("From which language google chrome is made?\na) JavaScript          b)C & C++          c)Python\n")
if userReply1 == 'b' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness) 
else:
    answers1 = False    
    falseAnswers = falseAnswers + "Q1 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)

userReply2 = input ("How is a string variable defined in c++?\na) String          b)str          c)str()\n")
if userReply2 == 'a' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)
else:
    answers2 = False    
    falseAnswers = falseAnswers + "Q2 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
userReply3 = input ("What is square root of 169?\na) 9          b)11          c)13\n")
if userReply3 == 'c' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)
else:
    answers3 = False    
    falseAnswers = falseAnswers + "Q3 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
userReply4 = input ("How much area of Pakistan consist of forests?\na) 5percent          b) 10percent          c)15percent\n")
if userReply4 == 'a' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)
else:
    answers4 = False    
    falseAnswers = falseAnswers + "Q4 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
userReply5 = input ("Where did qua•id e Azam Died?\na) Islamabad          b) Lahore          c)Karachi\n")
if userReply5 == 'c' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)
else:
    answers5 = False    
    falseAnswers = falseAnswers + "Q5 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
userReply6 = input ("Tomato is a _______?\na) Friut          b) Vegatable          c)None\n")
if userReply6 == 'a' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)
else:
    answers6 = False    
    falseAnswers = falseAnswers + "Q6 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
userReply7 = input ("Who is Present President of Pakistan?\na) Mamnoon Hussain          b) Arif Alvi          c)Asif Ali Zardari\n")
if userReply7 == 'b' :
        Total_Marks += int(1) 
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)   
else:
    answers7 = False    
    falseAnswers = falseAnswers + "Q7 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
userReply8 = input ("Who is chief Minister of Punjab?\na) Shahbaz Sharif          b) Usman Buzdar          c)Qaim Ali Shah\n")
if userReply8 == 'b' :
        Total_Marks += int(1)
        for x in green1:
            for brightness in BRIGHTNESS:
                print_with_color("Ok!", color=x, brightness=brightness)
else:
    answers8 = False    
    falseAnswers = falseAnswers + "Q8 "
    for x in red1:
        for brightness in BRIGHTNESS:
            print_with_color("Wrong!", color=x, brightness=brightness)
   
    
if Total_Marks < 8 :
    print (falseAnswers)
print ("\nYou got " , Total_Marks , " out of 8")
    

input ("\n Made by Maaz\n")
webbrowser.open('https://www.donotcheck319.blogspot.com')