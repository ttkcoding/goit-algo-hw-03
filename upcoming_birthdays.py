from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    #create current date and new list
    today = datetime.today().date()
    congratulation_list = []
    #going through the list
    for user in users:
        #convert string to datetime object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        #convert year to current, for correct comparison
        birthday_this_year = birthday.replace(year=today.year)
        #check if the birthday is over this year, if so add for next year 
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        #check the birthday for the next week, if the birthday is on a weekend, change the greeting to the next Monday
        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday < 8:
            if birthday_this_year.weekday() >= 5:
                days_to_birthday += (7 - birthday_this_year.weekday())

            # add all information to new list
            congratulation_date = today + timedelta(days=days_to_birthday)
            congratulation_list.append({"name": user["name"], "congratulation_date": congratulation_date})

    return congratulation_list


users = [
    {"name": "Alice", "birthday": "2000.03.03"},
    {"name": "Bob", "birthday": "1995.03.14"},
    {"name": "Charlie", "birthday": "1988.03.10"}
]


upcoming_birthdays = get_upcoming_birthdays(users=users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
