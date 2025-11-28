from turtle import Turtle,Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_STARTING_POSITION =[(102, -287)]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.screen = Screen()

    def create_car(self):
        for new_car in range(0,10):
            self.shape("square")
            self.penup()
            self.goto(280, 0)
            self.cars.append(new_car)





