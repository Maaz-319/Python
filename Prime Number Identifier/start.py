import time
def new_func():
    # code by Maaz Bin Asif
    # Email :: maazbinaasif@gmail.com
    while True:
        try:
            number = int(input("\n\tEnter a number: "))
            if number == 1:
                print("\n\t1 is not a prime number.")
            elif number >= 2:
                i = 2
                prime = True
                while i < number:
                    if number % i == 0:
                        prime = False
                    i += 1
                if prime == True:
                    print("\n\t",i," is a prime number")
                elif prime == False:
                    print("\n\t",i," is not a prime number")
            else:
                print("\n\tEnter a valid value.")
        except:
            print("\n\tNot a valid value.")
            time.sleep(0.5)
            print("Restarting program....")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            new_func()
new_func()