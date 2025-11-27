from turtle import  Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_player = 0
        self.left_player = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-80, 250)
        self.write(self.right_player, align="center", font=("Arial", 24, "normal"))
        self.goto(80, 250)
        self.write(self.left_player, align="center", font=("Arial", 24, "normal"))

    def right_player_score(self):
        self.right_player += 1
        self.update_score()
    def left_player_score(self):
        self.left_player += 1
        self.update_score()



