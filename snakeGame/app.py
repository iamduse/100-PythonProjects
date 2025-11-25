from turtle import Turtle, Screen
import time
from snakeClass import Snake

# create object for the classes
screen = Screen()


screen.setup(width=600 , height=500)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()


















screen.exitonclick()

