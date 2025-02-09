import time

today_date = time.strftime("%Y-%m-%d")
print(today_date)
print(type(today_date))
user_date = input("Enter your date of birth (yyyy-mm-dd): ")

def calculate_days(user_date, today_date):
      born_year, born_month, born_day = map(int, user_date.split('-'))
      today_year, today_month, today_day = map(int, today_date.split('-'))
      
      born_date = time.mktime((born_year, born_month, born_day, 0, 0, 0, 0, 0, 0))
      today_date = time.mktime((today_year, today_month, today_day, 0, 0, 0, 0, 0, 0))
      
      age_seconds = today_date - born_date
      age_days = int(age_seconds / (24 * 60 * 60))
      
      return age_days

days_old = calculate_days(user_date, today_date)

print(f"You are {days_old} days old.")

# Additional feature: calculating age in years, months, and days

years = days_old // 365
days_left = days_old % 365
months = days_left // 30
days = days_left % 30

print(f"You are {years} years, {months} months, and {days} days old.")

# Additional feature: calculating age in weeks, days, hours, and minutes

weeks = days_old // 7
days_left = days_old % 7
hours = days_left // 24
minutes = (days_left % 24) * 60

print(f"You are {weeks} weeks, {days_left} days, {hours} hours, and {minutes} minutes old.")