from turtle import Screen
from stick_class import  Stick
from ballClass import TheBall
from scoreClass import ScoreBoard
import time



screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0) # turnOff the animation

right_stick = Stick((370,0))
left_stick = Stick((-380,0))

ball = TheBall()
score =ScoreBoard()




screen.listen()
screen.onkey(right_stick.up,"Up")
screen.onkey(right_stick.down,"Down")
screen.onkey(left_stick.up,"q")
screen.onkey(left_stick.down,"w")





game_on = True
while game_on:
    screen.update() # updates the screen after turtle is created
    time.sleep(0.1)
    ball.ball_movement()


    # Detect if the ball make contact in the stick
    if ball.distance(right_stick) < 50 and ball.xcor() > 340:
        ball.bounce_x_axis()


    if ball.distance(left_stick) < 50 and ball.xcor() < -340:
        ball.bounce_x_axis()
    #Detect if Right side player misses the ball
    if ball.xcor() > 380:
        ball.refresh_the_ball()
        score.right_player_score()
    if ball.xcor() < -380:
        ball.refresh_the_ball()
        score.left_player_score()
        if score.left_player == 3:
            ball.gave_over()
            game_on = False

























screen.exitonclick()