import turtle
t = turtle.Turtle()

t.color('Green')
style = ('Courier', 20, 'italic')
t.write('Made by Maaz', font=style, align='right')

t. goto(50 , 0)
while True:
    for n in ['Green', 'Red', 'Orange', 'Blue', 'Yellow']:
       
        t.color(n)
        t.pensize(6)
        t.speed(4.5)
        t.left(90)
        t.forward(90)
        t.right(135)
        t.forward(90)
        t.left(90)
        t.forward(90)
        t.right(135)
        t.forward(90)


input()