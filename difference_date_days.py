from datetime import datetime

# It's a function which calculate difference between current date and input date
# given str format "YYYY.MM.DD" and output int format days
def get_days_from_today(*, date: str) -> int:
    #convert str date to datetime obj
    old_date_obj = datetime.strptime(date, "%Y.%m.%d")
    #create curent date obj
    current_date = datetime.today()
    numbers_day = current_date - old_date_obj
    return numbers_day.days


print(f"Difference in days is: {get_days_from_today(date="2021.08.23")}")