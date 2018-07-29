import string
import random

# generate list of symbols
dig = [1, 2, 3, 4, 5, 6, 7, 8, 0]
dig.extend(list(string.ascii_letters))
lst = [_ for _ in random.choices(dig, k=50)]
print("list of symbols:", lst)

print("1st symbol of the list:", lst[0])
print("last symbol of the list:", lst[-1])
print("3rd from the start: ", lst[2], "; and 3rd from the end:", lst[-3])
print("slice first 10 symbols:", lst[0:9])
print("symbol with index which divides on 2 without remainnig:", lst[::2])
print("only integers:", [a for a in lst if type(a) == int])
print("revers list using slice:", lst[::-1])
print("convert list into string", "".join([str(a) for a in lst]))