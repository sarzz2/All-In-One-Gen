import random, datetime

from typing import Union


DAYS = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


# Use gen_datetime to generate a random datetime and gen_time or random_time to generate a random time

def gen_datetime(start=1900, stop=2100) -> Union[datetime.datetime, bool]:
    '''
    :param: start = year to start with (inclusive, must be lower than stop)
    :param: stop = year to end with (inclusive, must be higher than start)
    :return: Union[datetime.datetime, bool] = bool False if invalid start or stop given else datetime.datetime random date
    '''
    if not isinstance(start, int) or not isinstance(stop, int) or start > stop: return False
    year = random.randint(start, stop)
    leap = not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
    month = random.randint(1, 12)
    if month == 2:
        days = 28 + leap
    else:
        days = DAYS[month]
    days = random.randint(1, days)
    h, m, s = random_time()
    time = datetime.timedelta(hours=h, minutes=m, seconds=s)
    return datetime.datetime(year, month, days) + time


def gen_time():
    h,m,s = random_time()
    return f'Time (hour:minute:second): {h:02}:{m:02}:{s:02}'


def random_time():
    return random.randint(0, 23), random.randint(0, 60), random.randint(0, 60)



