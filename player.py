from turtle import Turtle

FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.setpos(STARTING_POSITION)
        self.right(-90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
