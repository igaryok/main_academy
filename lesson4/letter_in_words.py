import string

with open("dzen.txt") as file:
    text = file.read()

dic_letters = {}

# clear text from signs of punctuation without '
for each in string.punctuation:
    if not each == '\'':
        text = text.replace(each, "")

list_of_words = text.lower().split()

for letter in "".join(list_of_words):
    if letter not in dic_letters:
        dic_letters[letter] = []

    for word in list_of_words:
        if letter in word:
            if word not in dic_letters[letter]:
                dic_letters[letter].append(word)


for each in dic_letters:
    print(each, "=>", dic_letters[each])