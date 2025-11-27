from turtle import Screen
from stick_class import  Stick
import time



screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0) # turnOff the animation

right_stick = Stick((370,0))
left_stick = Stick((-380,0))



screen.listen()
screen.onkey(right_stick.up,"Up")
screen.onkey(right_stick.down,"Down")
screen.onkey(left_stick.up,"q")
screen.onkey(left_stick.down,"w")





game_on = True
while game_on:
    screen.update() # updates the screen after turtle is created
    time.sleep(0.1)














screen.exitonclick()