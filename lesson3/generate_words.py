import random

str = input("Enter phrase: ")

str_w_whitesp = "".join(str.lower().split())
out_str = str_w_whitesp.replace(".", "").replace(",", "").replace("!", "").replace("?", "")

rezult_phrase = ""

# create the set of words
for i in range(0, 7):
    len_word = random.randint(2,8)
    word = "".join(random.sample(out_str, len_word))
    print(word)
    rezult_phrase = rezult_phrase + word + " "

# create the phrase
len_rezult_phrase = random.randint(2,6)
print(" ".join(random.sample(rezult_phrase.split(), len_rezult_phrase)).capitalize() + ".")