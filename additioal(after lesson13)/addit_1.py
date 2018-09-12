
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


if __name__ == '__main__':
    num = False
    while not num:
        num = input("Enter number: ")
        if not num.isdigit():
            print("You have entered wrong number. Try again!")
            num = False

    print(sum_digits(int(num)))
