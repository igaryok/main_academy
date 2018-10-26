import random
import datetime
import os
from peewee import SqliteDatabase, Model, DoubleField, CharField, DateTimeField

db = SqliteDatabase('payments.db')


class DBPayments(Model):
    class Meta:
        database = db
        db_table = "payments"

    amount = DoubleField()
    currency = CharField()
    created = DateTimeField()
    owner = CharField()
    bdate = DateTimeField()

    def __str__(self):
        return f"{self.amount} {self.currency} {self.created} {self.owner}"


class Payer:
    __payers_list = []

    def __init__(self, name):
        self.__name = name
        self.__bdate = Payer.create_birthday()
        Payer.__payers_list.append(self)

    @classmethod
    def find_by_name(cls, name):

        result = None
        for item in cls.__payers_list:
            if item.__name == name:
                result = item
                break

        return result

    def return_name(self):
        return self.__name

    def return_bdate(self):
        return self.__bdate

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


class Payment:
    id = 0
    __payments_list = []

    def __init__(self, amount, currency, created, owner):
        self.__id = Payment.id + 1
        self.__amount = amount
        self.__currency = currency
        self.__created = created
        self.__owner = owner
        Payment.__payments_list.append(self)
        Payment.id += 1

    @staticmethod
    def create_from_string(string):
        payer = Payer.find_by_name(string.split(";")[0])
        if not payer:
            payer = Payer(string.split(";")[0])

        amount = float(string.split(";")[1].split()[0].replace(",", "."))
        currency = string.split(";")[1].split()[1]
        date = datetime.datetime.strptime(string.split(";")[2], "%Y-%m-%d %H:%M:%S")
        Payment(amount, currency, date, payer)

    @staticmethod
    def print_list():
        for item in Payment.__payments_list:
            print(item.__id, str(item.__amount), item.__currency)

    @staticmethod
    def load_to_db():
        DBPayments.drop_table()
        DBPayments.create_table()

        for item in Payment.__payments_list:
            DBPayments.create(amount=item.__amount,
                              currency=item.__currency,
                              created=item.__created,
                              owner=item.__owner.return_name(),
                              bdate=item.__owner.return_bdate())

        db.close()


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
    for line in work_with_files():
        if not line.split(";")[3] == "out":
            continue

        Payment.create_from_string(line)

    Payment.load_to_db()

    payments = DBPayments.select()
    for item in payments:
        print(item.id, item)
