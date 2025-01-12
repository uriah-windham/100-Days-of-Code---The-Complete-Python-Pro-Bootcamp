from turtle import Turtle
import random
BALL_SPEED = 5

class Ball(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        directions = [-BALL_SPEED , BALL_SPEED]
        self.x_direction = random.choice(directions)
        self.y_direction = random.choice(directions)
        self.screen_left_right = screen_width
        self.screen_top_bottom = screen_height

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

        if self.ycor() + 10 >= self.screen_top_bottom or self.ycor() - 30 <= -self.screen_top_bottom:
            self.y_direction *= -1

    def hit_paddle(self):
        self.x_direction *= -1.2
