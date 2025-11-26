from turtle import Screen
from foodClass import  Food
import time
from snakeClass import Snake
from scoreClass import ScoreBoard

# create object for the classes
screen = Screen()


screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
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
    # Detect collision with Food
    if snake.the_head.distance(food) < 15:
        food.new_location()
        score.increase_score()
        snake.expend_the_snake()
    # Detect Collision with wall
    snake_xcor = snake.the_head.xcor()
    snake_ycor = snake.the_head.ycor()

    if snake_xcor > 280 or snake_xcor < -280 or snake_ycor > 280 or snake_ycor < -280:
        game_is_on = False
        score.game_over()

    # Detect Collision with the snakes own tail
    for each in snake.segments[1:]:
        if snake.the_head.distance(each) < 10:
            game_is_on = False
            score.game_over()






















screen.exitonclick()

