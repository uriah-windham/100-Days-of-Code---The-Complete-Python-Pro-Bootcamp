from turtle import Turtle
ALIGNMENT = "center"
FONT = ("ArcadeClassic", 120, "normal")

class Scoreboard(Turtle):
    def __init__(self, s_height):
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, s_height - 160)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_player_score}   {self.right_player_score}", align=ALIGNMENT, font=FONT)


    def gain_point_left_player(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def gain_point_right_player(self):
        self.right_player_score += 1
        self.update_scoreboard()

class DivideCourt(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(3)
        self.penup()
        self.hideturtle()

    def divide_court(self, s_height):
        self.goto(0, s_height)
        self.setheading(270)
        for i in range(0, 30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(30)

