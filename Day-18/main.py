import turtle as t
from random import choice, randint

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.shape("turtle")
my_turtle.speed("fastest")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_tuple = (r, g, b)
    return random_tuple


def draw_shape(num_sides):
    my_turtle.color(random_color())
    turn_angle = 360 / num_sides

    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(turn_angle)

def random_walk(random_turn):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(choice(random_turn))

# for shape_side in range(3, 11):
#     draw_shape(shape_side)

# for _ in range(200):
#     random_walk(turns)

steps = round(360 / 70)
for i in range(0, 360, steps):
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.left(steps)

screen = t.Screen()
screen.exitonclick()
