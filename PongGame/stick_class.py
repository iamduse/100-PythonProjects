from turtle import Turtle

class Stick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.up()
        self.down()
        self.create_stick()
        self.goto(position)

    def create_stick(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()

    def up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)














