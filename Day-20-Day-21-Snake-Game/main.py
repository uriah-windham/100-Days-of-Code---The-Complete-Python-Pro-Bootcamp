import os
import sys
import time
from pickle import GLOBAL
from turtle import Screen
from game_border import GameBorder
from snake import Snake
from food import Food
from game_state import GameState, PauseGame
PAUSED = False
GAME_IS_ON = True


def main():
    global GAME_IS_ON
    game_over = False
    screen = Screen()
    screen.bgcolor("black")
    game_state = GameState()
    pause_game = PauseGame()
    screen.setup(width=800, height=800)
    screen.title("Snake Game")
    screen.tracer(0)
    GameBorder()
    snake = Snake()
    food = Food()

    def toggle_pause():
        global  PAUSED
        PAUSED = not PAUSED
        pause_game.game_paused(PAUSED)
        screen.update()

    def on_click(x, y):
        global GAME_IS_ON

        yes_area_left = -120
        yes_area_right = -40
        yes_area_top = 170
        yes_area_bottom = 131

        no_area_left = 41
        no_area_right = 119
        no_area_top = 170
        no_area_bottom = 131

        if yes_area_left <= x <= yes_area_right and yes_area_bottom <= y <= yes_area_top:
            screen.clear()
            main()
        elif no_area_left <= x <= no_area_right and no_area_bottom <= y <= no_area_top:
            screen.bye()
            GAME_IS_ON = False

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(toggle_pause, "space")

    while GAME_IS_ON:
        while not game_over:
            global PAUSED
            screen.update()
            time.sleep(0.1)
            if not PAUSED:
                snake.move()

                #Detect collision with food
                if snake.snake_list[0].distance(food) < 10:
                    game_state.gain_point()
                    food.refresh()
                    snake.extend_snake()

                #Detect collision with wall
                if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
                    game_state.game_over()
                    snake.move_backward()
                    game_over = True

                #Detect collision with its tail
                for segment in snake.snake_list[1:]:
                    if snake.head.distance(segment) < 10:
                        game_state.game_over()
                        snake.move_backward()
                        game_over = True

        while GAME_IS_ON:
            screen.onkeypress(game_state.unbind_key(), "space")
            game_state.restart_game()
            screen.onscreenclick(fun=on_click)
            screen.update()
            time.sleep(0.1)

main()









