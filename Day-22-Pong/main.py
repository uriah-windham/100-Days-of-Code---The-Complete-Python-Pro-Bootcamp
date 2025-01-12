from turtle import Screen
from game_border import Gameborder


screen = Screen()
screen.setup(width=1.0, height=1.0, startx=0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
screen_width = screen.window_width() / 2
screen_height = screen.window_height() / 2
screen.title("Pong")
screen.bgcolor("black")
border = Gameborder(screen_width, screen_height)













screen.exitonclick()