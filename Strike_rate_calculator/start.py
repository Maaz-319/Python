runs = 0
balls = 0
strike_rate = 0

def user_input():
    global strike_rate
    global balls
    global runs

    runs = int(input("\n\tEnter Runs of batsman: "))
    balls = int(input("\n\tEnter balls faced by batsman: "))
    strike_rate = (runs / balls) * 100

user_input()

print("\n\tThe strike rate is " , strike_rate)
input()