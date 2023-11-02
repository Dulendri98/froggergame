from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.FINISH_LINE_Y = 280
        self.STARTING_POSITION = (0, -280)
        self.MOVE_DISTANCE = 10
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.setpos(self.STARTING_POSITION)
        self.right(-90)

    def move(self):
        self.forward(self.MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() >= self.FINISH_LINE_Y:
            self.setpos(self.STARTING_POSITION)
