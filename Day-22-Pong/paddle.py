from turtle import Turtle, Screen
PADDLE_SPEED = 10


class Paddle(Turtle):
    def __init__(self, x_cor, screen_height):
        super().__init__()
        self.shape("square")
        self.shapesize()
        self.color("white")
        self.shapesize(7, 1)
        self.length_in_pixels = 7 * 20
        self.half_length = self.length_in_pixels / 2
        self.penup()
        self.goto(x_cor, 0)
        self.screen_height = screen_height
        self.movement = Screen()
        self.current_direction = None

    def move_up(self):
        self.current_direction = "Up"

    def move_down(self):
        self.current_direction = "Down"

    def stop_move(self):
        self.current_direction = None

    def update(self):
         if self.current_direction == "Up":
             if self.ycor() + self.half_length < self.screen_height:
                 new_y_cor = self.ycor() + PADDLE_SPEED
                 x_cor = self.xcor()
                 self.goto(x_cor, new_y_cor)
         elif self.current_direction == "Down":
             if self.ycor() - self.half_length > -self.screen_height:
                 new_y_cor = self.ycor() - PADDLE_SPEED
                 x_cor = self.xcor()
                 self.goto(x_cor, new_y_cor)
         elif self.current_direction is None:
             self.forward(0)