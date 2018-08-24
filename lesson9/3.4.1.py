# /usr/bin/env python
"""
This script have two options: 1 - check if year is leap if not then print closest leap year
2 - Print all leap years in given range
"""


def check_year(number):
    """
    Function check if entered number ic correct for year
    :param number: string (year)
    :return: int(year) or None if year not correct
    """
    try:
        if int(number) < 0:
            number = None
        else:
            number = int(number)
    except ValueError:
        number = None

    return number


def leap_year(year):
    """
    Function return True if year is leap or False if not
    :param year: integer
    :return: boolean
    """
    # leap year must divided by 4 without remaining
    if year % 4 == 0:
        # but there is a exclusion for year which divided by 100 without remaining and not divided by 400
        if year % 100 == 0 and not(year % 400 == 0):
            answer = False
        else:
            answer = True
    else:
        answer = False

    return answer


def find_closest_leap_year(year):
    """
    Function return closest leap year
    :param year: integer - year
    :return: integer - leap year
    """

    while not leap_year(year):
        # for the exclusion year closest leap year will be in four years
        if year % 100 == 0 and not (year % 400 == 0):
            year += 4
        # for the previous year to exclusion year closest leap year will be before three years
        elif (year+1) % 100 == 0 and not ((year+1) % 400 == 0):
            year -= 3
        # for other years closest leap year depend on remaining from division by four
        elif year % 4 > 2:
            year += 1
        else:
            year -= 1

    return year


if __name__ == '__main__':

    print("Hello. Choose what you want.")
    print("1. Check if year is leap")
    print("2. Print all leap years in given range")

    n = None
    while n not in [1, 2]:
        try:
            n = int(input("Enter correct choice: "))
        except ValueError:
            n = None
        if n not in [1, 2]:
            print("You have entered wrong choice. Try again")

    if n == 1:
        enter_year = None
        while not enter_year:
            enter_year = check_year(input("Enter correct year, pls: "))
            if not enter_year:
                print("You have entered wrong year. Try again")

        if leap_year(enter_year):
            print("This is a leap year")
        else:
            print("This isn't a leap year")
            print("Closest leap year is", find_closest_leap_year(enter_year))
    elif n == 2:
        enter_year1 = None
        enter_year2 = None

        while not enter_year1:
            enter_year1 = check_year(input("Enter the first correct year, pls: "))
            if not enter_year1:
                print("You have entered wrong year. Try again")

        while not enter_year2:
            enter_year2 = check_year(input("Enter the second correct year, pls: "))
            if not enter_year1:
                print("You have entered wrong year. Try again")
            elif enter_year2 <= enter_year1:
                print("The second year must be bigger than first. Try again")
                enter_year2 = None

        print("All leap years in given range:", enter_year1, "-", enter_year2)
        for _ in range(enter_year1, enter_year2+1):
            if leap_year(_):
                print(_, end=" ")
