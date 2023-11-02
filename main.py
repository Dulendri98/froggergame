import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

game_is_on = True
game_loop = 0

cars = CarManager()

while game_is_on:
    game_loop += 1
    screen.listen()
    screen.onkey(player.move, "w")
    time.sleep(0.1)
    player.finish_line()
    screen.update()

    if 0 == game_loop % 6:
        cars = CarManager()

    cars.move()
