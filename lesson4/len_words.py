import string


def max_min(text, max_len=True):
    '''
    function returns the biggest word from the text if param_len is True
    else it returns the smallest word from the text
    'word' - is a combination of symbols not less 2
    :param text: string
    :param max_len: boolean
    :return: string
    '''

    # clear text from signs of punctuation without '
    for each in string.punctuation:
        if not each == '\'':
            text = text.replace(each, "")

    list_of_words = text.lower().split()

    # delete all words which has one symbol
    list_of_words = [a for a in list_of_words if len(a) > 1]

    list_of_words.sort(key=len)

    if max_len:
        return list_of_words[-1]
    else:
        return list_of_words[0]


if __name__ == '__main__':
    with open("dzen.txt") as file:
        txt = file.read()

    print("The biggest word:", max_min(txt))
    print("The smallest word:", max_min(txt, False))
