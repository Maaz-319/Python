import webbrowser



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
userReply2 = input ("How is a string variable defined in c++?\na) String          b)str          c)str()\n")
userReply3 = input ("What is square root of 169?\na) 9          b)11          c)13\n")
userReply4 = input ("How much area of Pakistan consist of forests?\na) 5percent          b) 10percent          c)15percent\n")
userReply5 = input ("Where did qua•id e Azam Died?\na) Islamabad          b) Lahore          c)Karachi\n")
userReply6 = input ("Tomato is a _______?\na) Friut          b) Vegatable          c)None\n")
userReply7 = input ("Who is Present President of Pakistan?\na) Mamnoon Hussain          b) Arif Alvi          c)Asif Ali Zardari\n")
userReply8 = input ("Who is chief Minister of Punjab?\na) Shahbaz Sharif          b) Usman Buzdar          c)Qaim Ali Shah\n")


if 1==0:
# if userReply1 and userReply2 and userReply3 and userReply4 and userReply5 and userReply6 and userReply7 and userReply8 is not('a' or 'b' or 'c'):
    print ("\nPlease enter only a, b, c\n")
else:
    if userReply1 == 'b' :
        Total_Marks += int(1) 
    else:
        answers1 = False    
        falseAnswers = falseAnswers + "Q1 "
    if userReply2 == 'a' :
        Total_Marks += int(1)
    else:
        answers2 = False    
        falseAnswers = falseAnswers + "Q2 "
    
    if userReply3 == 'c' :
        Total_Marks += int(1)
    else:
        answers3 = False    
        falseAnswers = falseAnswers + "Q3 "
    
    if userReply4 == 'a' :
        Total_Marks += int(1)
    else:
        answers4 = False    
        falseAnswers = falseAnswers + "Q4 "
    
    if userReply5 == 'c' :
        Total_Marks += int(1)
    else:
        answers5 = False    
        falseAnswers = falseAnswers + "Q5 "
    
    if userReply6 == 'a' :
        Total_Marks += int(1)
    else:
        answers6 = False    
        falseAnswers = falseAnswers + "Q6 "
    
    if userReply7 == 'b' :
        Total_Marks += int(1)    
    else:
        answers7 = False    
        falseAnswers = falseAnswers + "Q7 "
    
    if userReply8 == 'b' :
        Total_Marks += int(1)
    else:
        answers8 = False    
        falseAnswers = falseAnswers + "Q8 "
    
    
    if Total_Marks < 8 :
        print (falseAnswers)
    print ("\nYou got " , Total_Marks , " out of 8")
    

input ("\n Made by Maaz\n")
webbrowser.open('https://donotcheck319.blogspot.com')












































































#Old Code
#from colorama import Fore
#from colorama import Style


#Total_Marks = int(0)
#answers1 = True
#answers2 = True
#answers3 = True
#answers4 = True
#answers5 = True
#answers6 = True
#answers7 = True
#answers8 = True


#print("Please enter a ,b or c")
#a = input ("From which language google chrome is made?\na) JavaScript          b)C & C++          c)Python\n")
#b = input ("How is a string variable defined in c++?\na) String          b)str          c)str()\n")
#c = input ("What is square root of 169?\na) 9          b)11          c)13\n")
#d = input ("How much area of Pakistan consist of forests?\na) 5percent          b) 10percent          c)15percent\n")
#e = input ("Where did qua•id e Azam Died?\na) Islamabad          b) Lahore          c)Karachi\n")
#f = input ("Tomato is a _______?\na) Friut          b) Vegatable          c)None\n")
#g = input ("Who is Present President of Pakistan?\na) Mamnoon Hussain          b) Arif Alvi          c)Asif Ali Zardari\n")
#h = input ("Who is chief Minister of Punjab?\na) Shahbaz Sharif          b) Usman Buzdar          c)Qaim Ali Shah\n")


#if a and b and c and d and e and f and g and h is not('a' or 'b' or 'c'):
 #   print ("\nPlease enter only a, b, c\n")
#else:
#    if a == 'b' :
#        Total_Marks += int(1) 
#    else:
#        answers1 = False    
#    if b == 'a' :
#        Total_Marks += int(1)
#    else:
#        answers2 = False    
#    
 #   if c == 'c' :
#       Total_Marks += int(1)
#    else:
#        answers3 = False    
#    
#    if d == 'a' :
#        Total_Marks += int(1)
#    else:
#        answers4 = False    
    
#    if e == 'c' :
 #       Total_Marks += int(1)
   # else:
  #      answers5 = False    
    
    #if f == 'a' :
     #   Total_Marks += int(1)
    #else:
     #   answers6 = False    
    
    #if g == 'b' :
     #   Total_Marks += int(1)    
   # else:
    #    answers7 = False    
    
    #if h == 'b' :
     #   Total_Marks += int(1)
    #else:
     #   answers8 = False    
    
    
    #print ("\nYou got " , Total_Marks , " out of 8")
    
    
    #input ("\n Made by Maaz\n")

#input ("\n Made by Maaz\n")