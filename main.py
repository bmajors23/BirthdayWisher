import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995, month=5, day=1)

import smtplib
import random

my_email = "billyjoe17667@gmail.com"
password = "12345!"

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="cmajors01@yahoo.com",
            msg=f"Subject:It's Bryce sending you a randomly generated motivational quote using python\n\n{quote}"
        )