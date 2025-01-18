from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import password_generator

# ---------------------------- SEARCH FOR PASSWORD ------------------------------ #
def search_password():
    try:
        with open("./data.json", "r") as data_file:
            website = website_entry.get().title()
            data_dict = json.load(data_file)
            if website in data_dict:
                messagebox.showinfo(title=website, message=f"Email: {data_dict[website]["email"]}\nPassword: {data_dict[website]["password"]}")
            else:
                messagebox.showinfo(title="Password", message=f"No password saved for {website}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
        new_password = password_generator.main()
        password_entry.delete(0, END)
        password_entry.insert(END, new_password)
        pyperclip.copy(new_password)
        messagebox.showinfo(title="Password Generator", message="New password copied to clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
                "email": email,
                "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Empty Boxes", message="Please don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nDo you want to save?")

        if is_ok:
            try:
                with open("./data.json", "r") as data_file:
                    #Read the old data
                    data = json.load(data_file)
                    #Update the old data with the new data
                    data.update(new_data)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("./data.json", "w") as data_file:
                    #Create new file with new data
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("./data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=50)
email_entry.insert(END, "uriah@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

#Buttons
generate_password = Button(text="Generate Password", width=14, command=make_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()