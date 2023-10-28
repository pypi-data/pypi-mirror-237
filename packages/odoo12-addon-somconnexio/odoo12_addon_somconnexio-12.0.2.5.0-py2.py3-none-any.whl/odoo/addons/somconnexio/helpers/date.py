import datetime


def first_day_next_month():
    today = datetime.date.today()
    first_day = today.replace(day=1, month=today.month + 1)
    if today.month == 12:
        first_day = first_day.replace(year=today.year + 1, month=1)
    return first_day


def last_day_of_month():
    return first_day_next_month() - datetime.timedelta(days=1)


def date_to_str(date):
    return date.strftime("%Y-%m-%d")
