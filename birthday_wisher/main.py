##################### Extra Hard Starting Project ######################
import pandas as pd
#import smtpd
import random
import datetime as dt
from datetime import datetime
import smtplib

MY_EMAIL = "jennylovtrvlnbooks@gmail.com"
MY_PASSWORD = "ulxm eyfx pecg cldh"

data = pd.read_csv("birthday_wisher/birthdays.csv")
data['birth_date'] = data['year'].map(str)+'-'+data['month'].map(str)+'-'+data['day'].map(str)
bday_list = data.to_dict(orient='records')

today = dt.datetime.now().date()
letter_temp = ['letter_1.txt', 'letter_2.txt','letter_3.txt']

for b in bday_list:
     temp = b['birth_date']
     bday = datetime.strptime(temp, '%Y-%m-%d').date()
     if bday == today: 
        name = b['name']
        template = random.choice(letter_temp)
        print(template)
        
        with open(f"birthday_wisher/letter_templates/{template}",'r') as f: 
            letter = f.read()
        with open(f"birthday_wisher/letter_templates/{template}",'w') as f:
             bday_wish = letter.replace("[NAME]",name)
        print(bday_wish)
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="jjjenny.kao@gmail.com",
                                msg=f"Subject: Happy Birthday!\n\n{bday_wish}".encode("utf-8"))
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




