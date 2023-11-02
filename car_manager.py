from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(COLORS[random.randint(0, 5)])
        self.shapesize(1, 2)
        self.setpos(300, random.randint(-250, 250))


    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
