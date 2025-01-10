###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import turtle as t


my_turtle = t.Turtle()
t.colormode(255)
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setposition(-250, -250)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for _ in range(10):
    for _ in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)

    my_turtle.setheading(90)
    my_turtle.forward(50)
    my_turtle.setheading(180)
    my_turtle.forward(500)
    my_turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()