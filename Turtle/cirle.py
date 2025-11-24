from turtle import Turtle , Screen
import random


jimy = Turtle()
jimy.shape("circle")
colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink",
    "cyan", "magenta", "lime", "turquoise", "gold", "violet",
    "indigo", "coral", "salmon", "plum", "brown", "navy", "maroon",
    "olive", "teal", "skyblue", "khaki", "crimson"
]


jimy.color(random.choice(colors))
jimy.circle(100)
jimy.speed("fastest")



screen = Screen()
screen.exitonclick()