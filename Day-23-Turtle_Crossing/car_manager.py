from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.speed = 0


    def spawn_location(self):
        self.goto(x=random.randrange(-300, 301, 5),y=random.randrange(-221, 262, 10))
        self.speed += STARTING_MOVE_DISTANCE

    def respawn_car(self):
        self.goto(x=305,y=random.randrange(-221, 262, 10))

    def move_left(self):
        if self.xcor() > -350:
            self.forward(self.speed)
        elif self.xcor() <= -350:
            self.color(random.choice(COLORS))
            self.respawn_car()

    def speed_up(self):
        self.speed += MOVE_INCREMENT
