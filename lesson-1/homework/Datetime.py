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
