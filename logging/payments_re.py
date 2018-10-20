'''
refactoring task for payments without OOP but with logging
'''

import os
import datetime
import logging


def work_with_files():
    '''
    generator create string from all files
    :yield: string
    '''

    work_dir = os.getcwd() + "/payments/"

    for file in os.listdir(work_dir):
        with open(work_dir + file) as obj_file:
            for line in obj_file:
                yield line


def create_payers():
    dic_payers = {}
    for string in work_with_files():
        if not string.split(";")[3] == "out":
            continue

        name = string.split(";", 1)[0]
        if name not in dic_payers:
            log.info(f"Create item in payments dictionary: {name}")
            dic_payers[name] = []

        amount = string.split(";")[1].split()[0].replace(",", ".")
        currency = string.split(";")[1].split()[1]
        date = string.split(";")[2].split()[0]
        log.info(f"add payment for {name}: {amount} {currency} - {date}")
        dic_payers[name].append((float(amount), currency, datetime.datetime.strptime(date, "%Y-%m-%d")))

    return dic_payers


def save_in_file(file, string, mode):
    with open(file, mode) as file_obj:
        file_obj.write(string + "\n")

    if mode == "w":
        log.info(f"create file: {file}")


if __name__ == '__main__':
    # *initialization logging*
    log = logging.getLogger("payers")
    log_file = logging.FileHandler("payment.log")
    log_file.setFormatter(logging.Formatter("%(asctime)s, %(name)s : %(message)s"))
    log.setLevel(logging.INFO)
    log.addHandler(log_file)
    log.info("Start work of script")
    # create dictionary data
    # key - name(string), value - list of tuple(first item - amount(float),
    # second - currency(string), third - date(datetime.date))
    payers = create_payers()

    # print report
    # list payers sorted by quantity of purchases #
    msg = "List payers sorted by quantity of purchases"
    save = "1st_lst.txt"
    print(msg)
    save_in_file(save, msg, mode="w")
    for key, item in sorted(payers.items(), key=lambda x: len(x[1]), reverse=True):
        msg = key + " - " + str(len(item)) + " purchases"
        print(msg)
        save_in_file(save, msg, mode="a")

    # list payers sorted by sum of purchases
    msg = "List of payers sorted by sum of purchases"
    save = "2st_lst.txt"
    print(msg)
    save_in_file(save, msg, mode="w")
    for key, item in sorted(payers.items(), key=lambda x: sum(a[0] for a in x[1]), reverse=True):
        msg = '{} - {:.2f} total sum'.format(key, sum(a[0] for a in item))
        print(msg)
        save_in_file(save, msg, mode="a")

    # create set of payments days
    set_days = set()
    for each in payers.values():
        for item in each:
            set_days.add(item[2])

    # list of person who made purchases every day #
    msg = "List of person who made purchases every day"
    save = "3st_lst.txt"
    print(msg)
    save_in_file(save, msg, mode="w")
    for person, val in payers.items():
        if sorted(set_days) == sorted(set(item[2] for item in val)):
            msg = person
            print(person)
            save_in_file(save, msg, mode="a")

    # list of person who made purchases the first day only #
    msg = "List of person who made purchases the first day only "
    save = "4st_lst.txt"
    print(msg)
    save_in_file(save, msg, mode="w")
    for person, val in payers.items():
        days = sorted(set(item[2] for item in val))
        if sorted(set_days)[0] == days[0] and len(days) == 1:
            msg = person
            print(person)
            save_in_file(save, msg, mode="a")

    log.info("Finish work of script")
