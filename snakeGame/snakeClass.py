from turtle import  Turtle

# const variables
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
move_speed = 20
SOUTH = 90
WEST = 180
EAST = 0
NORTH = 270


class Snake():
    def __init__(self):
        # attributes =  what the class has
        self.segments = []
        self.create_snake()
        self.the_head = self.segments[0]
        self.the_tail = self.segments[-1]
        # self.increase_speed()




    # methods = what the class does and this class two methods
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    #  create add function
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(0.8, 0.8, 1)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # create growth function that allow the snake to grow when he eats the food
    def expend_the_snake(self):
        self.add_segment(self.the_tail.position())


    def move_snake(self):
        """" Create for loop to link the snake segment and move the last position to the second to last
          the range function has 3 parameters first one is start, second one is end position and last one is step """
        for each_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[each_segment - 1].xcor()
            new_y = self.segments[each_segment - 1].ycor()
            self.segments[each_segment].goto(new_x, new_y)
        self.the_head.forward(move_speed)




    def up(self):
        if self.the_head.heading() != NORTH:
            self.the_head.setheading(SOUTH)

    def down(self):
        if self.the_head.heading() != SOUTH:
            self.the_head.setheading(NORTH)
    def left(self):
        if self.the_head.heading() != EAST:
            self.the_head.setheading(WEST)
    def right(self):
        if self.the_head.heading() != WEST:
            self.the_head.setheading(EAST)






