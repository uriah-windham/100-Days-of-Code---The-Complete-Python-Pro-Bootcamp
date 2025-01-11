from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Fixedsys", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 310)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\nYOU SUCK", align=ALIGNMENT, font=FONT)

    def gain_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
