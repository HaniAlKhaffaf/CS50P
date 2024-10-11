from datetime import datetime, date
from num2words import num2words
import re, sys

def main():
    user_age = user_req()
    result = calculate_age(user_age)
    print(f"{result} minutes")

def user_req():
    user_input = input("Date of Birth: ")
    regex = r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"

    match = re.search(regex, user_input)
    if match:
        age_data = match.groups()
        return age_data 
    else:
        return sys.exit("Invalid date")

def calculate_age(user_age):
    year = int(user_age[0])
    month = int(user_age[1])
    day = int(user_age[2])

    birthdate = datetime(year, month, day, 0, 0, 0)  

    current_date = date.today()
    comparison_date = datetime(current_date.year, current_date.month, current_date.day, 0, 0, 0)

    age_timedelta = comparison_date - birthdate

    age_in_minutes = int(age_timedelta.total_seconds() // 60)

    age_in_minutes_words = num2words(age_in_minutes)

    age_in_minutes_words = age_in_minutes_words.replace(' and ', ' ')

    return age_in_minutes_words



if __name__ == "__main__":
    main()