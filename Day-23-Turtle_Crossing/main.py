import time
from turtle import Screen, Turtle
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import CarManager
CARS_IN_GAME = 15
#TODO Work on collision between player and cars


screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
# screen.bgcolor("gray60")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
hitbox = Turtle()

cars = [CarManager() for i in range(CARS_IN_GAME)]

screen.listen()
screen.onkeypress(scoreboard.close_game, "Escape")
screen.onkeypress(player.move_up, "Up")
# screen.onkeyrelease(player.stop_moving, "Up")



#TODO Only use this block of code when i'm testing on MacOS
###########################################################
# Bring the turtle graphics window to the front
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()  # Get the root Tk window
root.lift()                     # Raise the window
root.attributes('-topmost', True)  # Keep it on top temporarily
# root.attributes('-topmost', False)  # Allow other windows to overlap
root.deiconify()                # Ensure the window is not minimized
############################################################

def main():
    for car in cars:
        car.spawn_location()
    screen.update()
    while scoreboard.game_is_on:
        time.sleep(0.01)
        screen.update()
        while not scoreboard.game_is_over:
            for car in cars:
                car.move_left()
            check_collision()

            # screen.ontimer(player.check_movement, 1)

            if player.ycor() >= FINISH_LINE_Y:
                player.goto(STARTING_POSITION)
                scoreboard.level_up()
                for car in cars:
                    car.speed_up()


            time.sleep(0.1)
            screen.update()

def check_collision():
    for car in cars:
        if car.x_left_hit <= player.xcor() <= car.x_right_hit and car.y_bottom_hit <= player.ycor() <= car.y_top_hit:
            print("Game Over")
            scoreboard.game_is_over = True
            return







if __name__ == "__main__":
    main()
