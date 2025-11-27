from turtle import Turtle

class TheBall(Turtle ):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction_move = 10
        self.y_direction_move = 10

    def ball_movement(self):
        # Move the ball using its velocity
        new_x = self.xcor() + self.x_direction_move
        new_y = self.ycor() + self.y_direction_move
        self.goto(new_x, new_y)


        # Detect Top and bottom wall collision and make bounce
        if self.ycor() > 290 or self.ycor()< -280:
                self.y_direction_move *= -1

    def bounce_x_axis(self):
        self.x_direction_move *= -1
        #Increase ball speed after it touches to the stick or paddle
        # self.x_direction_move *= 1.1

    def bounce_y_axis(self):
        self.y_direction_move *= -1
        # Increase ball speed after it touches to the stick or paddle
        # self.y_direction_move *= 1.1


    def gave_over(self):
        self.write("GAME OVER", align="center", font= ("Arial", 24, "normal"))
        self.goto(0,0)

    def refresh_the_ball(self):
        self.goto(0,0)
        self.bounce_x_axis()











