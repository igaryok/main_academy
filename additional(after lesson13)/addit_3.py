"""
task for generator and iterator
print 30 courses lessons from 12/07/2018
"""
import datetime


class LessonsDay:
    """
    iterator return dates if it is Tuesday or Thursday
    from current_day
    in each iterating return string with date
    """
    def __init__(self, current_day):
        self.check_day = current_day

    def __iter__(self):
        return self

    def __next__(self):
        self.current_day = None
        while not self.current_day:
            week = self.check_day.weekday()
            if week in [1, 3]:
                self.current_day = self.check_day
                self.check_day = self.check_day + datetime.timedelta(days=1)
                return self.current_day
            else:
                self.check_day = self.check_day + datetime.timedelta(days=1)


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
    print("Lessons days from generator: ")
    for index, day in enumerate(gen_day(datetime.date(2018, 7, 12))):
        if index > 29:
            break
        else:
            print(index+1, day)

    print("Lessons days from iterator")
    lesson_day = LessonsDay(datetime.date(2018, 7, 12))
    for index, day in enumerate(lesson_day):
        if index > 29:
            break
        else:
            print(index+1, day)
