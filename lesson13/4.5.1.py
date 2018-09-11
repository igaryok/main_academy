# /usr/bin/env python

"""
own function enumerate
"""


def own_enumerate(obj):
    count = 0
    for item in obj:
        count += 1
        yield item, count


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    for each in own_enumerate(lst):
        print(each)
