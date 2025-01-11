from turtle import Turtle, Screen

class GameBorder:

    def __init__(self):
        screen = Screen()
        turtle = Turtle()

        #SCREEN EDGE HAS TO BE SET IN INTERVALS OF TWENTY
        screen_edge = 300
        turtle.penup()
        turtle.hideturtle()
        turtle.width(20)
        turtle.color("darkgrey")
        turtle.goto(screen_edge,screen_edge)
        turtle.pendown()
        turtle.goto(screen_edge,-screen_edge)
        turtle.goto(-screen_edge,-screen_edge)
        turtle.goto(-screen_edge,screen_edge)
        turtle.goto(screen_edge,screen_edge)
        screen.update()