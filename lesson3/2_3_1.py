import string
import random

# generate string with all lowercase, uppercase symbols and numbers
str = "".join(random.choices(string.ascii_letters + string.digits, k=100))
print("String:", str)

print("First symbol:", str[0])
print("Last symbol:", str[-1])
print("3 symbol from beginning:", str[2])
print("3 symbol from the end:", str[-3])
print("slice of first 8 symbols:", str[:8])
print("only symbols with index, which divides on 3 without remaining: ", end="")
for i in range(len(str)-1):
    if i % 3 == 0:
        print(str[i], end="")
print("\nthe symbol of the middle of the string text:", str[(len(str)-1) // 2])
print("reverse text: ", str[::-1])