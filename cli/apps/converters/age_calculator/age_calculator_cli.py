from datetime import date
from calendar import monthrange

def calculate_age(birthdate) -> tuple[int]:
  today = date.today()
  age_year = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
  
  if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
    age_month = 12 - birthdate.month + today.month
  elif today.month == birthdate.month and today.day < birthdate.day:
    age_month = (12 - birthdate.month) + today.month - 1
  else:
    age_month = today.month - birthdate.month
  
  if today.day < birthdate.day:
    month_before_today = today.month - 1 if today.month > 1 else 12
    days_in_month = monthrange(today.year, month_before_today)
    age_days = days_in_month[1] - (birthdate.day - today.day)
  else:
    age_days = today.day - birthdate.day

  return (age_year, age_month, age_days)

def run():
  birthday: str = input("Enter your birthday (YYYY-MM-DD): ") #1984-09-12
  year, month, day = map(int, birthday.split('-'))
  birthdate = date(year, month, day)
  
  age_year, age_month, age_day = calculate_age(birthdate)
  
  
  return f"You are {age_year} years, {age_month} month and {age_day} days old."


if __name__ == "__main__":
  result = run()
  print(result)
