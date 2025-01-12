from turtle import Turtle, Screen

class Gameborder(Turtle):
    def __init__(self, window_width, window_height):
        super().__init__()
        border = Turtle()
        border.color("white")
        border.penup()
        border.pensize(20)
        border.speed("fastest")
        border.goto(window_width, window_height+10)
        border.pendown()
        border.goto(-window_width, window_height+10)
        border.penup()
        border.goto(window_width, -window_height-10)
        border.pendown()
        border.goto(-window_width, -window_height-10)
