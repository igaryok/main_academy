# /usr/bin/env python

word = "Found name"
ids = {
    "name": "Vasya",
    "age": 55
}


def function_for_lab(string, name, *args, age=None):
    print(string, name)
    print("Age:", age)
    print(args)


function_for_lab(word, **ids)
function_for_lab(word, ids["name"], *list(range(0, 10)))