#puzzle 1
from datetime import datetime

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()

age_years = today.year - birthdate.year
age_months = today.month - birthdate.month
age_days = today.day - birthdate.day

# Adjust if the birthday hasn't occurred yet this year
if age_months < 0 or (age_months == 0 and age_days < 0):
    age_years -= 1
    age_months += 12 if age_months < 0 else 0
    age_days += (today - datetime(today.year, birthdate.month, birthdate.day)).days

print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")
#puzzle 2
from datetime import datetime

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()

next_birthday = datetime(today.year, birthdate.month, birthdate.day)
if today > next_birthday:
    next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

days_until_birthday = (next_birthday - today).days
print(f"There are {days_until_birthday} days remaining until your next birthday.")
#puzzle3
from datetime import datetime, timedelta

current_time = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
duration_hours = int(input("Enter meeting duration in hours: "))
duration_minutes = int(input("Enter meeting duration in minutes: "))

meeting_end_time = current_time + timedelta(hours=duration_hours, minutes=duration_minutes)
print(f"The meeting will end at: {meeting_end_time.strftime('%Y-%m-%d %H:%M')}")
#puzzle 4
from datetime import datetime
import pytz

timezone_from = input("Enter your current timezone (e.g., 'US/Eastern'): ")
timezone_to = input("Enter the timezone to convert to (e.g., 'Europe/London'): ")

timezone_from = pytz.timezone(timezone_from)
timezone_to = pytz.timezone(timezone_to)

current_time = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M")
localized_time = timezone_from.localize(current_time)

converted_time = localized_time.astimezone(timezone_to)
print(f"The time in {timezone_to} is: {converted_time.strftime('%Y-%m-%d %H:%M')}")
#puzzle 5
import time
from datetime import datetime

future_time = input("Enter the future date and time (YYYY-MM-DD HH:MM): ")
future_time = datetime.strptime(future_time, "%Y-%m-%d %H:%M")

while True:
    now = datetime.now()
    remaining_time = future_time - now
    if remaining_time.total_seconds() <= 0:
        print("The countdown has ended!")
        break
    print(f"Time remaining: {remaining_time}")
    time.sleep(1) 
#puzzle 6
import re

email = input("Enter an email address: ")
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")
#puzzle 7
import re

phone_number = input("Enter a phone number (without dashes or parentheses): ")
formatted_number = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', phone_number)
print(f"Formatted phone number: {formatted_number}")
#puzzle 8
import re

password = input("Enter a password: ")

if len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password):
    print("Password is strong.")
else:
    print("Password is weak.")
#puzzle 9
text = input("Enter a text: ")
word = input("Enter the word to find: ")

word_occurrences = [i for i in range(len(text)) if text.startswith(word, i)]
print(f"The word '{word}' occurs at positions: {word_occurrences}")
#puzzle 10
import re

text = input("Enter a text: ")
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)  # Match dates in format YYYY-MM-DD
print("Dates found:", dates)



