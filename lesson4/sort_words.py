import string


with open("dzen.txt") as file:
    text = file.read()

# clear text from signs of punctuation without '
for each in string.punctuation:
    if not each == '\'':
        text = text.replace(each, "")

list_of_words = text.lower().split()

list_of_words.sort()
with open("words_asc.txt", "w") as file:
    for each in list_of_words:
        file.writelines(each + "\n")


with open("words_desc.txt", "w") as file:
    for each in list_of_words[::-1]:
        file.writelines(each+"\n")
