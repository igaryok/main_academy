# /usr/bin/env python

import re


def main():
    result_dictionary = dict()

    pattern = r"(([0-9]{1,3}\.){3}[0-9]{1,3}) ([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2}).+(\[\w+\]) - (.*)"

    with open("app.log") as file_open:
        for line in file_open:
            result = re.match(pattern, line)

            if result:
                if result.group(5) == "[ERROR]":
                    continue

                key = (result.group(1), "{0} {1}".format(result.group(3), result.group(4)))

                if not result_dictionary.get(key):
                    result_dictionary[key] = []

                result_dictionary[key].append(result.group(6))

    with open("result_parsing.txt", "w") as file_write:
        for key, item in result_dictionary.items():
            print(key, '=>', item)
            file_write.write(str(key) + ' => ' + str(item) + '\n')


if __name__ == '__main__':
    main()