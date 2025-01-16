from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("Using Tkinter as a GUI")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Ariel", 32, "normal"))
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Button 2
button_2 = Button(text="Click Me Too", command=button_clicked)
button_2.grid(column=2, row=0)

#Input
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()