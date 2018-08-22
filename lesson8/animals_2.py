def question(string_input):
    """
    Print question from sting_input and wait for answer from user. Answer must be neither Y, y, 1, T ,t for positive
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
    list_of_questions = ["Can it fly?", "Has it feathers?", "Is this bat?", "Does it live in water?", "Has it lags?"]

    dict_of_animals = {
        (True, True, False, False, False): "This is bird",
        (True, False, True, False, False): "This is bat",
        (True, False, False, False, False): "This is insect",
        (False, False, False, True, False): "This is fish",
        (False, False, False, False, True): "This is mammal",
        (False, False, False, False, False): "This is snake"
    }

    print("Answer for ", len(list_of_questions), "questions. Yes or No")
    input("Press Enter for continue ...")

    answers = []
    for each in list_of_questions:
        answer_for_question = question(each)
        answers.append(answer_for_question)

    print(dict_of_animals.get(tuple(answers), "unknown species"))


if __name__ == '__main__':
    main()