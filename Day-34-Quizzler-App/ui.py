from tkinter import *
from quiz_brain import QuizBrain
from data import categories_true_false

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, font=("Arial", 24, "bold"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.show_question = self.canvas.create_text(
            150,
            125,
            text="",
            fill="black",
            font=FONT,
            width=280,
            justify="center",
        )

        self.true_button = Button()
        true_image = PhotoImage(file="./images/true.png")
        self.true_button.config(
            image=true_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.answered_true,
        )
        self.true_button.grid(column=1, row=2)

        self.false_button = Button()
        false_image = PhotoImage(file="./images/false.png")
        self.false_button.config(
            image=false_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.answered_false,
        )
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.show_question, text=q_text)
        else:
            self.canvas.itemconfig(self.show_question, text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state="disabled")

    def answered_true(self):
        self.answer_feedback(self.quiz.check_answer("True"))
        # self.get_next_question()

    def answered_false(self):
        self.answer_feedback(self.quiz.check_answer("False"))
        # self.get_next_question()

    def answer_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def on_select(self):
        pass