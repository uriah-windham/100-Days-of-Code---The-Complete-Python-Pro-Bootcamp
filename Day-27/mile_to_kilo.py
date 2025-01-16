from tkinter import *

def convert_mile_to_kilo():
    user_input = miles_entry.get()
    new_kilo = round(float(user_input) * 1.609344, 2)
    kilo_conversion.config(text=f"{new_kilo}")

#Screen
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

#User input box
miles_entry = Entry()
miles_entry.config(width=7)
miles_entry.grid(column=1, row=0)

#Display "is equal to"
label = Label(text="is equal to")
label.grid(column=0, row=1)

#Display "Miles"
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

#Display "Km"
kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

#Display current kilo is 0
kilo_conversion = Label(text=0)
kilo_conversion.grid(column=1, row=1)

#When clicked it runs the takes the user's input of miles and converts it to kilometers
convert_button = Button(text="Calculate", command=convert_mile_to_kilo)
convert_button.grid(column=1, row=2)

window.mainloop()