import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgpic("car.gif")
screen.title("car crossing game")

player = Player()
cars = CarManager()
score = Scoreboard()




screen.listen()
screen.onkeypress(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()



# Detect Collision the car and the turtle
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.gave_over()

# Detect if car reaches the finish line and restart the game level
    # also speed up the cars with each level and count the score
    if player.is_at_finish_line():
        player.start_new_level()
        cars.speed_up()
        score.increase_level()








screen.exitonclick()