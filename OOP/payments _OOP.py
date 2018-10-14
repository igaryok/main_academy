'''
create unique list of person from files
print the list sorted bu birthday
'''

import datetime
import random
import os


class Person:
    list_of_person = []

    def __init__(self, name):
        self.name = name
        self.birthday = Person.create_birthday()
        Person.list_of_person.append(self)

    @staticmethod
    def create_list_person(names):
        for each in names:
            Person(each)

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
        return isinstance(other, Person) and self.birthday == other.birthday

    def __lt__(self, other):
        return isinstance(other, Person) and self.birthday < other.birthday

    def __gt__(self, other):
        return isinstance(other, Person) and self.birthday > other.birthday

    def __str__(self):
        return f'{self.name} {self.birthday.strftime("%d/%m/%Y")}'

    @classmethod
    def find_by_name(cls, name):
        result = None
        for item in cls.list_of_person:
            if item.name == name:
                result = each
                break

        return result


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
    unique_name = set()

    for line in work_with_files():
        unique_name.add(line.split(";", 1)[0])

    Person.create_list_person(unique_name)
    for each in sorted(Person.list_of_person):
        print(each)
