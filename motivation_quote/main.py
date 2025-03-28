import smtplib
import datetime as dt
import random 

MY_EMAIL = "jennylovtrvlnbooks@gmail.com"
MY_PASSWORD = "ulxm eyfx pecg cldh"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0: 
    with open("motivation_quote/quotes.txt","r") as file: 
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    message = f"Subject: Monday Motivation💛\n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection: 
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="jjjenny.kao@gmail.com", 
            msg=message.encode("utf-8"))
        connection.close()
        
