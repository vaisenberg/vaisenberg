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
from datetime import datetime

def time_until_january_first():
    now = datetime.now()
    
   
    jan_first = datetime(now.year + 1, 1, 1)
    
    time_left = jan_first - now
    
    days_left = time_left.days
    total_seconds_left = time_left.seconds
    
    hours_left = total_seconds_left // 3600         
    remaining_seconds = total_seconds_left % 3600   
    minutes_left = remaining_seconds // 60         
    seconds_left = remaining_seconds % 60           
    
    print(f"The 1st of January is in {days_left} days and {hours_left}:{minutes_left:02}:{seconds_left:02} hours.")


time_until_january_first()

# exercise 6

from datetime import date

def cal_minutes_lived(year, month, day):
    birthdate = date(year, month, day)
    days_lived = (date.today() - birthdate).days
    minutes_lived = days_lived * 24 * 60
    print(f"You have lived approximately {minutes_lived:,} minutes.")

cal_minutes_lived(1975,3,21)

