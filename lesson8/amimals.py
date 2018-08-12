def question(string_input):
    """
    Print question from strng_input and wait for answer from user. Answer must be neither Y, y, 1, T ,t for positive
    answer or N, n ,0, F, f for negative answer.
    :param string_input: string
    :return: boolean (True or False)
    """
    ask = None
    result = None

    while not ask:
        ask = input(string_input+": ")
        if ask in ("Y", "y", "1", "T", "t"):
            result = True
        elif ask in ("N", "n", "0", "F", "f"):
            result = False
        else:
            print("You have entered missing answer. Try one more time, pls")
            ask = None

    return result


def main():
    answer = question("Can it fly?")
    if answer:
        answer = question("Has it feathers?")
        if answer:
            print("This is bird")
        else:
            answer = question("Is this bat?")
            if answer:
                print("This is bat")
            else:
                print("This is insect")
    else:
        answer = question("Does it live in water?")
        if answer:
            print("This is fish")
        else:
            answer = question("Has it lags?")
            if answer:
                print("This is mammal")
            else:
                print("This is snake")

    print("Well done!")
    return


if __name__ == '__main__':
    main()
