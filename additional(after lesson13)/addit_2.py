"""
additional task - sum all payments from the first payment day only in USD
"""
import re


def to_float(number_in_string):
    """
    Function try to convert string from str to dloat
    :param number_in_string: string with number
    :return: float or None if number_in_string has wrong format
    """
    if "," in number_in_string:
        number_in_string = number_in_string.replace(",", ".")

    try:
        result = float(number_in_string)
    except ValueError:
        print("Format of number is wrong")
        result = None

    return result


def get_sum(file_name):
    """
    generator which return an amount of payment for each iteration from file
    if the payment had done in USD
    :param file_name: name of file
    :yield: float
    """
    pattern = r"(.+);(\d+[\.,]?\d*) ([A-Z]{3});(\d{4}(-\d{2}){2}) \d{2}(:\d{2}){2};(.*);"
    with open(file_name) as file:
        for line in file:
            result_match = re.match(pattern, line)
            if result_match:
                if result_match.group(7) == "out" and result_match.group(3) == "USD":
                    yield to_float(result_match.group(2))


if __name__ == '__main__':
    print("{:.2f} USD".format(sum(get_sum("payments/2018-08-20.txt"))))
