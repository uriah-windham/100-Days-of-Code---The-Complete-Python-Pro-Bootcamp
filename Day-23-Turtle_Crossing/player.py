from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.fillcolor("pink")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        # self.moving = False

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        # self.moving = True

    # def stop_moving(self):
    #     self.forward(0)
    #     self.moving = False

    # def check_movement(self):
    #     if self.moving:
    #         self.forward(MOVE_DISTANCE)
    #     elif not self.moving:
    #         self.forward(0)

    def check_finish_line(self):
        pass
