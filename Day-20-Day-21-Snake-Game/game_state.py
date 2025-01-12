from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Fixedsys", 24, "normal")
TEXT_COLOR = "black"
TEXT_BACKGROUND = "white"

class GameState(Turtle):
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

    def gain_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def fill_text_background(self, x, y, width, height, color):
        self.goto(x, y)
        self.fillcolor(color)
        self.begin_fill()

        self.setheading(0)  # Face right
        self.pendown()
        for _ in range(2):
            self.forward(width)
            self.right(90)
            self.forward(height)
            self.right(90)
        self.end_fill()
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"GAME OVER\nYOU SUCK", align=ALIGNMENT, font=FONT)

    def unbind_key(self):
        pass

    def restart_game(self):
        self.goto(0, 180)
        self.color("white")
        self.write(f"DO YOU WANT TO PLAY AGAIN?", align=ALIGNMENT,font=FONT)
        self.fill_text_background(x=-120, y=170, width=80, height=40, color=TEXT_BACKGROUND)
        self.goto(-80, 136)
        self.color(TEXT_COLOR)
        self.write("YES", align=ALIGNMENT, font=FONT)
        self.fill_text_background(x=40, y=170, width=80, height=40, color=TEXT_BACKGROUND)
        self.goto(80, 136)
        self.color(TEXT_COLOR)
        self.write("NO", align=ALIGNMENT, font=FONT)

class PauseGame(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.game_state = GameState()

    def game_paused(self, paused):
        if paused:
            self.game_state.fill_text_background(x=-100, y=36, width=200, height=40, color=TEXT_BACKGROUND)
            self.goto(0, 0)
            self.color(TEXT_COLOR)
            self.write(arg="GAME PAUSED", align=ALIGNMENT, font=FONT)
        else:
            self.game_state.clear()
            self.hideturtle()




