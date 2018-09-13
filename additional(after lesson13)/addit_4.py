"""
decorating function from task addit_1.py
function-decorator check if the number is right digit
"""


def sum_digits(number):
    """
    recursion function which calculate sum from digits of numbers
    don't use strings, lists. loops
    :param number: integer >=0
    :return: sum of all numbers digits
    """
    if number // 10 == 0:
        return number % 10
    else:
        return number % 10 + sum_digits(number // 10)


def check_decor(func):
    def check(num):
        if num.isdigit():
            func(int(n))
            return True
        else:
            print("Error!")

    return check


@check_decor
def main(num):
    result = sum_digits(num)
    if result:
        print(result)

    return result


if __name__ == '__main__':
    correct = None
    while not correct:
        n = input("Enter number: ")
        correct = main(n)
        if not correct:
            print("You have entered wrong number. Tru again!")
