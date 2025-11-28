from turtle import Turtle,Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        """Create one car in to goto position"""
        random_chance = random.randint(1,6)
        if random_chance == 1:
            self.new_car = Turtle()
            self.new_car.shape("square")
            self.new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            self.new_car.goto(300, random_y)
            self.all_cars.append(self.new_car)


    def move_cars(self):
        """Move all cars to the left"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT










