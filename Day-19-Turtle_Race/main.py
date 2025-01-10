import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle do you think will win the race?\nBlue, Red, Orange, Green, Purple, or Pink")
colors = ["blue", "red", "orange", "green", "purple", "pink"]
y_positions = [100, 60, 20, -20, -60, -100]
all_turtles = []

winning_text = Turtle()
winning_text.penup()
winning_text.hideturtle()
winning_text.goto(x=0, y=150)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 221:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                winning_text.write(arg=f"You won! The {winning_color} turtle won the race.", align="center", font=("Ariel", 16, "normal"))
            else:
                winning_text.write(arg=f"Sorry, you lost. The {winning_color} turtle won the race.", align="center", font=("Ariel", 16, "normal"))
            break



screen.exitonclick()