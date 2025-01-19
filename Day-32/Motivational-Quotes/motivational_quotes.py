import smtplib
import datetime as dt
import random

my_email = ""
my_password = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as data_file:
        quotes = data_file.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Weekly Dose of Motivation\n\n{random_quote}"
        )
