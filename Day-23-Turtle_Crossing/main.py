import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import CarManager
CARS_IN_GAME = 15
screen = Screen()

# TODO Only use this block of code when i'm testing on MacOS
###########################################################
# Bring the turtle graphics window to the front
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()  # Get the root Tk window
root.lift()  # Raise the window
root.attributes('-topmost', True)  # Keep it on top temporarily
# root.attributes('-topmost', False)  # Allow other windows to overlap
root.deiconify()  # Ensure the window is not minimized
############################################################

def main():
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player = Player()
    scoreboard = Scoreboard()

    cars = [CarManager() for i in range(CARS_IN_GAME)]

    screen.listen()
    screen.onkeypress(scoreboard.close_game, "Escape")
    screen.onkeypress(player.move_up, "Up")

    for car in cars:
        car.spawn_location()
    screen.update()
    while scoreboard.game_is_on:
        time.sleep(0.01)
        screen.update()
        while not scoreboard.game_is_over:
            time.sleep(0.1)
            screen.update()
            for car in cars:
                car.move_left()
                if int(car.distance(player)) < 20:
                    print("Game Over")
                    scoreboard.game_over()

            if player.ycor() >= FINISH_LINE_Y:
                player.goto(STARTING_POSITION)
                scoreboard.level_up()
                for car in cars:
                    car.speed_up()
        screen.onkeypress(None, "Up")

if __name__ == "__main__":
    main()
