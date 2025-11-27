from turtle import Turtle , Screen
import random


jimy = Turtle()
jimy.shape("classic")
jimy.color("Blue")
jimy.pensize(6)

# create random walk with random colors
colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink",
    "cyan", "magenta", "lime", "turquoise", "gold", "violet",
    "indigo", "coral", "salmon", "plum", "brown", "navy", "maroon",
    "olive", "teal", "skyblue", "khaki", "crimson"
]
directions = [ 0, 90, 180, 270 ]
for _ in range(200):
    jimy.forward(30)
    jimy.setheading(random.choice(directions))
    jimy.speed(0)
    jimy.color(random.choice(colors))









screen = Screen()
screen.exitonclick()