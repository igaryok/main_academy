# /usr/bin/env python

import datetime


def main():
    curent_day = datetime.date(2018, 8, 22)
    count_of_lesson = 25
    with open("dates_of_course.txt", "w") as file_write:
        while count_of_lesson:
            curent_day = curent_day + datetime.timedelta(days=1)
            week = curent_day.weekday()
            if week in [1, 3]:
                print(curent_day)
                file_write.write(curent_day.isoformat() + "\n")
                count_of_lesson -= 1


if __name__ == '__main__':
    main()
