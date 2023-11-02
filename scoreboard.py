from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setpos(0, 270)
        self.level = 1
        self.write(self.level, align="center", font=FONT)

    def next_level(self):
        self.level += 1

    def update_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.next_level()
        self.write(self.level, align="center", font=FONT)