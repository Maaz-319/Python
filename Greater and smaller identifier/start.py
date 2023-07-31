a = input("Enter 'a' to find largest number and enter 'b' to find smallest Number: ")
def small():
    n1 = float(input("Enter First Number: "))
    n2 = float(input("Enter second Number: "))
    n3 = float(input("Enter Third Number: "))
    if n1 < n2 and n1 < n3:
        print (n1)
    elif n2 < n1 and n2 < n3 :
        print (n2) 
    elif n3 < n2 and n3 < n1 :
        print (n3)
    elif n1 == n2 and n1 == n3 and n2 == n3 :
        print ("\nAll Numbers are equal\n")
    else :
        print ("Invalid Input")
    input ("\nThanks for using this program .Made by Maaz.\n")   







 
def large():
    N1 = float(input("Enter First Number: "))
    N2 = float(input("Enter second Number: "))
    N3 = float(input("Enter Third Number: "))
    if N1 > N2 and N1 > N3:
        print (N1)
    elif N2 > N1 and N2 > N3 :
        print (N2) 
    elif N3 > N2 and N3 > N1 :
        print (N3)
    elif N1 == N2 and N1 == N3 and N2 == N3 :
        print ("\nAll Numbers are equal\n")
    else :
        print ("Invalid Input")
    input ("\nThanks for using this program .Made by Maaz.\n")










if a == 'a' :
    print(large())     
elif a == 'b' :
    print(small())
else :
    print ("\nInvalid input\n")
    input ("\nThanks for using this program .Made by Maaz.\n")

