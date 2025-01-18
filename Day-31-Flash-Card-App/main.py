from tkinter import *
import pandas
from random import randint
index_number = 0
BACKGROUND_COLOR = "#B1DDC6"

def flip_card():
    canvas.itemconfig(tagOrId=card_face, image=card_back)
    canvas.itemconfig(tagOrId=language_text, text="English", fill="white")
    canvas.itemconfig(tagOrId=practice_word, text=french_words_dict["English"][random_index], fill="white")

def wrong_answer():
    global random_index
    random_index = randint(0, len(french_words_dict["French"]))
    if canvas.itemcget(tagOrId=language_text, option="text") == "French":
        pass
    else:
        canvas.itemconfig(tagOrId=card_face, image=card_front)
        canvas.itemconfig(tagOrId=language_text, text="French", fill="black")
        canvas.itemconfig(tagOrId=practice_word, text=french_words_dict["French"][random_index], fill="black")

def right_answer():
    global random_index
    if canvas.itemcget(tagOrId=language_text, option="text") == "French":
        pass
    else:
        french_words_dict["French"].pop(random_index)
        french_words_dict["English"].pop(random_index)
        french_words_dict["French"] = {i:value for i, (key, value) in enumerate(french_words_dict["French"].items())}
        french_words_dict["English"] = {i:value for i, (key, value) in enumerate(french_words_dict["English"].items())}
        with open("./data/words_to_learn.csv", "w", newline="") as new_data:
            words_to_learn = pandas.DataFrame(french_words_dict)
            print(words_to_learn)
            words_to_learn.to_csv(new_data, index=False, lineterminator="")
        random_index = randint(0, len(french_words_dict["French"]))
        canvas.itemconfig(tagOrId=card_face, image=card_front)
        canvas.itemconfig(tagOrId=language_text, text="French", fill="black")
        canvas.itemconfig(tagOrId=practice_word, text=french_words_dict["French"][random_index], fill="black")

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    with open("./data/words_to_learn.csv", "r") as data_file:
        french_words = pandas.read_csv(data_file)
        french_words_dict = french_words.to_dict()
        random_index = randint(0, len(french_words_dict["French"]))
except FileNotFoundError:
    with open("./data/french_words.csv", "r") as data_file:
        french_words = pandas.read_csv(data_file)
        french_words_dict = french_words.to_dict()
        random_index = randint(0, len(french_words_dict["French"]))

#Flash Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_face = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
practice_word = canvas.create_text(400, 263, text=french_words_dict["French"][random_index], font=("Ariel", 60, "bold"), fill="black")

#Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=wrong_answer)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)

flip_image = PhotoImage(file="./images/flip.png")
flip_button = Button(image=flip_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_card)
flip_button.grid(column=0, row=1, columnspan=2)

window.mainloop()