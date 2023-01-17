import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Initialize  the player
player = Player()
# initialize Car Manager
car_manager = CarManager()


# initialize scoreboard
scoreboard = Scoreboard()



def game():
    loop_run = 0

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        if loop_run == 6:
            car_manager.create_cars()
            loop_run = 0

        car_manager.move_cars()
        loop_run += 1

        car_manager.remove_out_of_sight_cars()

        # move up when the Up button is pressed
        screen.onkey(player.move, "Up")

    #     if the user crosses the finish line, go to the next level
        if player.ycor() > 280:
            scoreboard.level += 1
            scoreboard.display_level()
            player.new_game()

    #     if turtle get's hit. print game over
        if car_manager.turtle_hit(player.position()):
            game_is_on = False
            scoreboard.game_over()


        screen.onkey(game, 'y')
    screen.exitonclick()

game()