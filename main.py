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

cars = [CarManager()]

scoreboard = Scoreboard()

level = 1

while game_is_on:
    game_loop += 1
    screen.listen()
    screen.onkey(player.move, "w")
    time.sleep(0.1)
    if player.ycor() > 280:
        level += 1
        player.setpos(player.STARTING_POSITION)
        scoreboard.update_score()
        for i in range(len(cars)):
            cars[i].speedup()

    screen.update()

    if 0 == game_loop % 6:
        cars.append(CarManager())

    for i in range(len(cars)):
        cars[i].set_speed(level)
        cars[i].move()
        if player.distance(cars[i]) < 20:
            game_is_on = False

print("Game Over")
