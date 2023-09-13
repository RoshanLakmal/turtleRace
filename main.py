import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup (width=500, height=400)
user_guess = screen.textinput("Make your bet", "Who will win the race? Enter a colour:")

tim = Turtle()
tim.color('purple')
tim.penup()
tim.goto(-240,0)
tim.speed(random.randint(0, 10))

bob = Turtle()
bob.color('green')
bob.penup()
bob.goto(-240,50)
bob.speed(random.randint(0, 10))


james = Turtle()
james.color('blue')
james.penup()
james.goto(-240,100)
james.speed(random.randint(0, 10))

sam = Turtle()
sam.color('red')
sam.penup()
sam.goto(-240,-50)
sam.speed(random.randint(0, 10))

david = Turtle()
david.color('orange')
david.penup()
david.goto(-240,-100)
david.speed(random.randint(0, 10))

winner = ""
while True:
    tim.forward(10)
    bob.forward(10)
    james.forward(10)
    sam.forward(10)
    david.forward(10)
    current_tim_xcor = round(tim.xcor())
    current_bob_xcor = round(bob.xcor())
    current_james_xcor = round(james.xcor())
    current_sam_xcor = round(sam.xcor())
    current_david_xcor = round(david.xcor())
    if current_tim_xcor == 250:
        winner = "purple"
        break
    elif current_bob_xcor == 250:
        winner = "green"
        break
    elif current_james_xcor == 250:
        winner = "blue"
        break
    elif current_sam_xcor == 250:
        winner = "red"
        break
    elif current_david_xcor == 250:
        winner = "orange"
        break




if user_guess == winner:
    print('you won')
else:
    print('you lost')
screen.exitonclick()