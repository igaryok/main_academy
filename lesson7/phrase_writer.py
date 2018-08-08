import sys


def print_ordinal(n):
    """
    Function return an ordinal number in English from 1 to 100
    :param n: must integer from 1 to 100
    :return: string
    """

    dic_num_pfraze = {
        "units_ordinal": ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"],
        "11-19": ["eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth",
                  "eighteenth", "nineteenth"],
        "dozens": ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"],
        "dozens_ordinal": ["tenth",  "twentieth", "thirtieth", "forties", "fiftieth", "sixtieth", "seventieth",
                           "eightieth", "ninetieth", "hundredth", ]
    }

    if not type(n) == int:
        print("Error: type")
        return None

    if n < 1 or n > 100:
        print("Error: number out of range")
        return None

    if n % 10 == 0:
        result_string = dic_num_pfraze["dozens_ordinal"][n // 10 - 1]
    elif n < 10:
        result_string = dic_num_pfraze["units_ordinal"][n-1]
    elif 9 < n < 20:
        result_string = dic_num_pfraze["11-19"][n - 11]
    else:
        result_string = dic_num_pfraze["dozens"][n // 10 - 1] + " " + dic_num_pfraze["units_ordinal"][n % 10 - 1]

    return result_string


def main():
    if len(sys.argv) != 2:
        print("You must run a program with one argument from 1 to 100. The argument is set to the default value 3")
        num = 3
    elif not sys.argv[1].isdigit():
        print("The argument must be integer from 1 to 100. The argument is set to the default value 3")
        num = 3
    elif not (int(sys.argv[1]) in range(1,101)):
        print("The argument must be integer from 1 to 100. The argument is set to the default value 3")
        num = 3
    else:
        num = int(sys.argv[1])

    write_file = open("phrases_file.txt", "w")
    for _ in range(1, num+1):
        phrase = input("The "+print_ordinal(_)+" phrase : ")
        if phrase:
            print("The "+print_ordinal(_)+" phrase:", phrase[::-1], file=write_file, flush=True)
        else:
            print("Thank you!")
            break
    else:
        print("Thank you!")

    write_file.close()


if __name__ == '__main__':
    main()
