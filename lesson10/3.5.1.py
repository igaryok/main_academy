# /usr/bin/env python

import getpass
import string


def main():
    users = {
        "Vasya": "12345",
        "Kolya": "qwerty",
        "Petya": "1234554321"
    }
    username = input("Hello. Enter your name: ")
    try:
        pass_in_dic = users[username]
    except KeyError:
        print("This username haven't fond")
        return

    wrong_character = None
    password = None
    while not wrong_character:
        password = getpass.getpass()
        try:
            if password == "":
                raise RuntimeError
        except RuntimeError:
            print("Password mustn't be empty")
            return
        if any([each for each in list(password) if each in string.punctuation]):
            print("Your password have a sign od punctuation. This is wrong. Try again!")
        else:
            wrong_character = True

    if password == pass_in_dic:
        print("Access Granted")
    else:
        print("You have entered wrong password")


if __name__ == '__main__':
    main()