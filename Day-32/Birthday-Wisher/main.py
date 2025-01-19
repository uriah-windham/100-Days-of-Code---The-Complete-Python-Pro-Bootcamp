import datetime as dt
import pandas
import smtplib
import random

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def birthday_message(name):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        message = letter.read()
        new_message = message.replace("[NAME]", name)
        with open("./birthday_letter.txt", "w") as new_letter:
            new_letter.write(new_message)
        return new_message

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
#DONE

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month = now.month
today_day = now.day

with open("./birthdays.csv") as data_file:
    birthdays = pandas.read_csv(data_file)
    for index, row in birthdays.iterrows():
        if row["month"] == today_month and row["day"] == today_day:
            birthday_name = row["name"]
            birthday_email = row["email"]
            bday_message = birthday_message(birthday_name)

# 4. Send the letter generated in step 3 to that person's email address.
my_email = ""
my_password = ""

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthday_email,
        msg=f"Subject:Happy Birthday!\n\n{bday_message}"
    )



