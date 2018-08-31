# /usr/bin/env python

import os
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


def create_payments_dic(work_dir):
    """
    Function create dictionary result_dic. It takes data from file-name_of_file
    structure of dictionary: key - string with name of man
    value - list of tuples with payments, where every tuple has next structure:
    first item string with date of payment, second item float with amount of
    payment and third item - string with name of currency
    :param work_dir: dir with data files
    :return: dictionary and list of payments date
    """
    pattern = r"(.+);(\d+[\.,]?\d*) ([A-Z]{3});(\d{4}(-\d{2}){2}) \d{2}(:\d{2}){2};(.*);"
    result_dic = dict()
    payment_days = []
    for each in os.listdir(work_dir):
        lines_in_file = 0
        patterned_lines = 0
        if os.path.isfile(work_dir + each):
            payment_days.append(each.replace(".txt", ""))

        with open(work_dir + each) as file:
            for line in file:
                lines_in_file += 1
                result = re.match(pattern, line)
                if result:
                    patterned_lines += 1
                    if result.group(7) == "out":
                        if not result_dic.get(result.group(1)):
                            result_dic[result.group(1)] = list()
                        result_dic[result.group(1)].append((result.group(4), to_float(result.group(2)),
                                                            result.group(3)))

        if not (lines_in_file == patterned_lines):
            print("The quantity of lines from", each, "is different from quantity notes. Maybe something wrong")
            print(lines_in_file, patterned_lines)

    return result_dic, payment_days


def main():
    payments_dir = "payments"
    work_dir = os.getcwd() + "/" + payments_dir + "/"

    # create payment dictionary and list of payments days from all payment files
    result_dic, payment_days = create_payments_dic(work_dir)

    # the first list of people (sorted by total sum and quantity of purchases)
    with open("1st_list_1.txt", "w") as write_file:
        print("<<The first list of people (sorted by total sum)>>")
        print("")
        write_file.write("<<The first list of people (sorted by total sum)>>\n")
        write_file.write("\n")
        for item, value in sorted(result_dic.items(), key=lambda x: sum([a[1] for a in x[1]]), reverse=True):
            print(item, ":")
            total_sum = '{:.2f}'.format(sum([a[1] for a in value]))
            print("Total purchases:", len(value), " ; Total sum:", total_sum)
            print("In currency:")
            write_file.write(item + ":\n")
            write_file.write("Total purchases: " + str(len(value)) + " ; Total sum: " + total_sum + "\n")
            currency_dic = dict()
            for each in value:
                if not currency_dic.get(each[2]):
                    currency_dic[each[2]] = 0
                currency_dic[each[2]] += each[1]
            for key, val in currency_dic.items():
                print(key, " : ", '{:.2f}'.format(val))
                write_file.write(key + " : " + '{:.2f}'.format(val) + "\n")

            print("----------")
            write_file.write("----------\n")
            del currency_dic

    with open("1st_list_2.txt", "w") as write_file:
        print("<<The first list of people (sorted by quantity of purchases)>>")
        print("")
        write_file.write("<<The first list of people (sorted by quantity of purchases)>>\n")
        write_file.write("\n")
        for item, value in sorted(result_dic.items(), key=lambda x: len(x[1]), reverse=True):
            print(item, ":")
            total_sum = '{:.2f}'.format(sum([a[1] for a in value]))
            print("Total purchases:", len(value), " ; Total sum:", total_sum)
            print("In currency:")
            write_file.write(item + ":\n")
            write_file.write("Total purchases: " + str(len(value)) + " ; Total sum: " + total_sum + "\n")
            currency_dic = dict()
            for each in value:
                if not currency_dic.get(each[2]):
                    currency_dic[each[2]] = 0
                currency_dic[each[2]] += each[1]
            for key, val in currency_dic.items():
                print(key, " : ", '{:.2f}'.format(val))
                write_file.write(key + " : " + '{:.2f}'.format(val) + "\n")

            print("----------")
            write_file.write("----------\n")
            del currency_dic

    # the second list of people, whom made purchases every day
    with open("2nd_list.txt", "w") as write_file:
        print("\n<<The second list of people, whom made purchases every day>>")
        print("")
        write_file.write("<<The second list of people, whom made purchases every day>>\n")
        write_file.write("\n")
        for item, value in result_dic.items():
            if len(set([a[0] for a in value])) == len(payment_days):
                print(item)
                write_file.write(item + "\n")

    # the third list of people whom made purchases in the first day only
    with open("3rd_list.txt", "w") as write_file:
        print("\n<<The third list of people whom made purchases in the first day only>>")
        print("")
        write_file.write("<<The third list of people whom made purchases in the first day only>>\n")
        write_file.write("\n")
        for item, value in result_dic.items():
            if (len(list(set([a[0] for a in value]))) == 1) and \
                    (list(set([a[0] for a in value]))[0] == sorted(payment_days)[0]):
                print(item)
                write_file.write(item + "\n")


if __name__ == '__main__':
    main()
