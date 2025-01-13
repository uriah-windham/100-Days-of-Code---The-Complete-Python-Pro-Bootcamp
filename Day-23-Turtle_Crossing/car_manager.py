from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.x_right_hit = 0
        self.x_left_hit = 0
        self.y_top_hit = 0
        self.y_bottom_hit = 0
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.speed = 0
        self.hit_box()


    def spawn_location(self):
        self.goto(x=random.randrange(-300, 301, 5),y=random.randrange(-260, 261, 10))
        self.y_top_hit = self.ycor() + 15
        self.y_bottom_hit = self.ycor() - 20
        self.speed += STARTING_MOVE_DISTANCE

    def respawn_car(self):
        self.goto(x=305,y=random.randrange(-260, 261, 10))

    def move_left(self):
        self.x_right_hit = self.xcor() + 25
        self.x_left_hit = self.xcor() - 30
        if self.x_right_hit > -300:
            self.forward(self.speed)
        elif self.x_right_hit <= -300:
            self.color(random.choice(COLORS))
            self.respawn_car()

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def hit_box(self):
        self.penup()
        self.goto(self.xcor() - 20, self.ycor() - 10)
        self.pendown()
        self.goto(self.xcor() - 20, self.ycor() + 10)
        self.goto(self.xcor() + 20, self.ycor() + 10)
        self.goto(self.xcor() + 20, self.ycor() - 10)
        self.goto(self.xcor() - 20, self.ycor() - 10)
        self.penup()