"""
task for decorator
decorator-spy and wrapped recursion function from task addit_1.py
"""


def spy(func):
    """
    decorator - spy. It writes name of function, arguments and
    result of function. If it happen error in function decorator write
    the error but don't stop function
    :param func: function which is decorated
    :return: wrapped function
    """
    def decorator(*args, **kwargs):
        with open("result_spy.txt", "w") as file:
            file.write("Function name => " + func.__name__ + "\n")
            file.write("Function is called with arguments => " + func.__name__ + "(")

            result_str = ""
            for each in args:
                result_str += str(each) + ", "
            else:
                if len(kwargs) == 0:
                    file.write(result_str[0:len(result_str)-2])

            result_str = ""
            for item, value in kwargs.items():
                result_str += str(item) + "=" + str(value) + ", "
            else:
                file.write(result_str[0:len(result_str)-2])
            file.write(")")
            try:
                result = func(*args, **kwargs)
                file.write("\nResult of function: " + str(result) + "\n")
            except Exception as result_exception:
                file.write("\nThe function generate error: " + str(result_exception) + "\n")
                result = "Error: " + str(result_exception)

        return result

    return decorator


@spy
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
