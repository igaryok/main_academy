'''
Count the numbers payments and amounts payments in total and
in each payments day by currency
'''

import datetime
import random
import os


class Payer:
    list_of_person = []

    def __init__(self, name):
        self.name = name
        self.birthday = Payer.create_birthday()
        self.payments_list = []
        Payer.list_of_person.append(self)

    @staticmethod
    def create_list_person(names):
        for each in names:
            Payer(each)

    @staticmethod
    def create_birthday(start_date="01/01/1970", end_date="31/12/1989", frm="%d/%m/%Y"):
        '''
        create random date from range start_date to end_date
        end_date must bigger than start_day (more than 2 days)
        :param start_date: string with data (01/01/1970")
        :param end_date: string with data (31/12/1989")
        :param frm - presentation of the dates (%d/%m/%Y")
        :return: object datetime.date
        '''

        start_date = datetime.datetime.strptime(start_date, frm)
        end_date = datetime.datetime.strptime(end_date, frm)

        delta = end_date - start_date

        if delta.days < 2:
            raise ValueError("start day less than end day or difference between days less 2")

        return_day = start_date + datetime.timedelta(days=random.randint(1, delta.days))
        return return_day.date()

    def __eq__(self, other):
        return isinstance(other, Payer) and self.birthday == other.birthday

    def __lt__(self, other):
        return isinstance(other, Payer) and self.birthday < other.birthday

    def __gt__(self, other):
        return isinstance(other, Payer) and self.birthday > other.birthday

    def __str__(self):
        return f'{self.name} {self.birthday.strftime("%d/%m/%Y")}'

    @classmethod
    def find_by_name(cls, name):

        if not all((x for x in cls.list_of_person if isinstance(x, Payer))):
            raise TypeError("list of payer wrong")

        result = None
        for item in cls.list_of_person:
            if item.name == name:
                result = item
                break

        return result

    def add_payment(self, amount, currency, date):
        self.payments_list.append(Payment(amount, currency, date, self))


class Payment:

    payment_id = 1
    payment_list = []

    def __init__(self, amount, currency, date, owner):
        if not isinstance(owner, Payer):
            raise TypeError("last parameter owner must be an object of class Payer")
        self.amount = amount
        self.currency = currency
        self.date = date
        self.owner = owner
        Payment.payment_list.append(self)
        Payment.payment_id += 1

    @staticmethod
    def create_from_string(string):
        payer = Payer.find_by_name(string.split(";")[0])
        if payer:
            amount = float(string.split(";")[1].split()[0].replace(",", "."))
            currency = string.split(";")[1].split()[1]
            date = datetime.datetime.strptime(string.split(";")[2].split()[0], "%Y-%m-%d").date()
            payer.add_payment(amount, currency, date)
        else:
            print(string.split(";")[0], "not found")


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


if __name__ == '__main__':
    # create data #
    unique_name = set()
    for line in work_with_files():
        unique_name.add(line.split(";", 1)[0])

    Payer.create_list_person(unique_name)

    # Lucius Malfoy;869.53 EUR;2018-08-22 09:09:37;out;
    # name - [0], amount with currency - [1], datetime - [2], direction - [3]
    for line in work_with_files():
        if not line.split(";")[3] == "out":
            continue
        Payment.create_from_string(line)

    # create report #
    date_set = set(a.date for a in Payment.payment_list)
    currency_set = set(a.currency for a in Payment.payment_list)
    print("Payments report")
    print("TOTAL")
    print("Count of payment - ", len(Payment.payment_list))
    print("In currency:")
    for each in currency_set:
        _ = list(a.amount for a in Payment.payment_list if a.currency == each)
        print(each, ":", "{:.2f}".format(sum(_)), "({} payments)".format(len(_)))
    print()
    print("IN DATE")
    for each in sorted(date_set):
        print(datetime.datetime.strftime(each, "%d/%m/%Y"))
        for item in currency_set:
            _ = list(a.amount for a in Payment.payment_list if a.currency == item and a.date == each)
            print(item, ":", "{:.2f}".format(sum(_)), "({} payments)".format(len(_)))
