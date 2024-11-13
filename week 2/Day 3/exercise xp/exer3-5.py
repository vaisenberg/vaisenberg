# Exercise 3: String module
import random
import string

def generate_random_string(length=5):
   
    letters = string.ascii_letters  
    random_string = ''.join(random.choices(letters, k=length))
    return random_string
print(generate_random_string())

#  Exercise 4 : Current Date
from datetime import datetime

def display_current_date():
    current_date = datetime.now().date()
    print("Current Date:", current_date)

display_current_date()

# exercise 5

from datetime import date

def cal_minutes_lived(year, month, day):
    birthdate = date(year, month, day)
    days_lived = (date.today() - birthdate).days
    minutes_lived = days_lived * 24 * 60
    print(f"You have lived approximately {minutes_lived:,} minutes.")

cal_minutes_lived(1975,3,21)

