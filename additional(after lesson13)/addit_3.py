"""
task for generator
print 30 courses lessons from 12/07/2018
"""
import datetime


def gen_day(current_day):
    """
    generator return dates if it is Tuesday or Thursday
    from current_day
    :param current_day: date in datetime format
    :yield: string with date
    """
    check_day = current_day
    while True:
        week = check_day.weekday()
        if week in [1, 3]:
            yield check_day
        check_day = check_day + datetime.timedelta(days=1)


if __name__ == '__main__':
    for index, day in enumerate(gen_day(datetime.date(2018, 7, 12))):
        if index > 29:
            break
        else:
            print(index+1, day)
