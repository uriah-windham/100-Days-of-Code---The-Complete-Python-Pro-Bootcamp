import time
from turtle import Screen
from game_border import Gameborder
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, DivideCourt

GAME_IS_ON = True
MATCH_STARTED = False

screen = Screen()
screen.setup(width=1.0, height=1.0, startx=0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
screen.tracer(0)
screen_width = (screen.window_width() / 2)
screen_height = (screen.window_height() / 2)-10
screen.title("Pong")
screen.bgcolor("black")
Gameborder(screen_width, screen_height)
scoreboard = Scoreboard(screen_height)
divide_court = DivideCourt()
divide_court.divide_court(screen_height)

def main():
    right_paddle = Paddle(screen_width - 60, screen_height)
    left_paddle = Paddle(-screen_width + 60, screen_height)
    ball = Ball(screen_width, screen_height)

    screen.listen()
    screen.onkeypress(close_game, "Escape")
    screen.onkeypress(start_game, "space")
    screen.onclick(get_coordinates)

    while GAME_IS_ON:
        global MATCH_STARTED
        screen.update()
        time.sleep(0.01)
        while MATCH_STARTED:
            screen.onkeypress(right_paddle.move_up, "Up")
            screen.onkeypress(right_paddle.move_down, "Down")
            screen.onkeypress(left_paddle.move_up, "w") or screen.onkeypress(left_paddle.move_up, "W")
            screen.onkeypress(left_paddle.move_down, "s") or screen.onkeypress(left_paddle.move_down, "S")
            screen.onkeyrelease(right_paddle.stop_move, "Up")
            screen.onkeyrelease(right_paddle.stop_move, "Down")
            screen.onkeyrelease(left_paddle.stop_move, "w") or screen.onkeyrelease(left_paddle.stop_move, "W")
            screen.onkeyrelease(left_paddle.stop_move, "s") or screen.onkeyrelease(left_paddle.stop_move, "S")

            screen.update()
            time.sleep(0.01)
            ball.move()
            screen.ontimer(left_paddle.update, 1)
            screen.ontimer(right_paddle.update, 1)

            ball_x, ball_y = ball.position()

            if right_paddle.xcor() - 10 <= ball_x and right_paddle.ycor() - right_paddle.half_length <= ball_y <= right_paddle.ycor() + right_paddle.half_length:
                ball.hit_paddle()
            if left_paddle.xcor() + 10 >= ball_x and left_paddle.ycor() - left_paddle.half_length <= ball_y <= left_paddle.ycor() + left_paddle.half_length:
                ball.hit_paddle()


            #TODO When the a player scores, on respawn the ball need to travel toward the player who got scored on.
            if ball.position() > (screen_width + 40, 0):
                left_paddle.reset()
                right_paddle.reset()
                ball.reset()
                scoreboard.gain_point_left_player()
                MATCH_STARTED = False
                main()

            if ball.position() < (-screen_width - 40, 0):
                left_paddle.reset()
                right_paddle.reset()
                ball.reset()
                scoreboard.gain_point_right_player()
                MATCH_STARTED = False
                main()

def start_game():
    global MATCH_STARTED
    MATCH_STARTED = True

def close_game():
    global GAME_IS_ON
    global MATCH_STARTED
    GAME_IS_ON = False
    MATCH_STARTED = False

def get_coordinates(x, y):
    print(f"Coordinates: ({x}, {y})")

if __name__ == "__main__":
    main()










