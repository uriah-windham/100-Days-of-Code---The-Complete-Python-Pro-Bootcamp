from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
current_checkmarks = ""
timer = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    global current_checkmarks
    global timer
    REPS = 0
    current_checkmarks = ""
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text=current_checkmarks)
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    elif count < 0:
        start_timer()
        if REPS % 2 == 0:
            single_checkmark = "✔"
            global current_checkmarks
            current_checkmarks += single_checkmark
            checkmark.config(text=current_checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Display the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= "./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Display the text "Timer" in green
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

#Start Button
start_button = Button(text="Start", command=start_timer, width=1, height=1, bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

#Reset Button
reset_button = Button(text="Reset", command=reset_timer, width=1, height=1, bg=YELLOW, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

#Checkmarks
checkmark = Label(text=current_checkmarks, fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()