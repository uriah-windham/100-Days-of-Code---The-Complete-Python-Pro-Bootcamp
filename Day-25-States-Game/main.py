from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic(picname="./blank_states_img.gif")
screen.setup(width=725, height=491)
fill_state = Turtle()
fill_state.penup()
fill_state.speed("fastest")
fill_state.hideturtle()

correct_answers = []
missing_answers = []

x = 0
y = 0


all_states = pandas.read_csv("./50_states.csv")
states_dict = all_states.to_dict("dict")


def write_answer():
    fill_state.goto(x, y)
    fill_state.write(answer_state)

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Guessed",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    for key, val in states_dict["state"].items():
        if val == answer_state:
            x = states_dict["x"][key]
            y = states_dict["y"][key]
            write_answer()
            correct_answers.append(answer_state)

    if len(correct_answers) == 50:
        game_on = False
        screen.bye()

for key, val in states_dict["state"].items():
    if val not in correct_answers:
        missing_answers.append(val)

pandas.Series(missing_answers).to_csv("./missing_states.csv")
