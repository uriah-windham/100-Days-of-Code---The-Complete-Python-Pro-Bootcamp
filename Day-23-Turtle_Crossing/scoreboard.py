from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.game_is_over = False
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.game_is_over = True

    def close_game(self):
        self.game_is_over = True
        self.game_is_on = False

    def play_again(self):
        self.game_is_on = True
        self.game_is_over = False

