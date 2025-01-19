from tkinter import *
import requests

def get_quote():
    response = requests.get("https://taylorswiftapi.onrender.com/get")
    response.raise_for_status()
    data = response.json()
    tswift_quote = data["quote"]
    canvas.itemconfig(quote_text, text=tswift_quote)

window = Tk()
window.title("Taylor Swift Says...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Get Taylor Swift Lyric", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

tswift_img = PhotoImage(file="tswift.png")
tswift_button = Button(image=tswift_img, highlightthickness=0, borderwidth=0, bg="white", command=get_quote)
tswift_button.grid(row=1, column=0)

window.mainloop()