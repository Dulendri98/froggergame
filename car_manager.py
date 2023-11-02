from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.current_speed = MOVE_INCREMENT
        self.penup()
        self.shape("square")
        self.color(COLORS[random.randint(0, 5)])
        self.shapesize(1, 2)
        self.setpos(300, random.randint(-250, 250))

    def move(self):
        new_x = self.xcor() - self.current_speed
        self.goto(new_x, self.ycor())

    def speedup(self):
        self.current_speed += 5

    def set_speed(self, level):
        self.current_speed = level * 5
