import string


input_string = input("Enter string: ").lower()

shift = 4

code_dic = {}
list_of_dictionary = list(enumerate(string.ascii_lowercase))
for item in list_of_dictionary:
    new_index = (item[0] + shift) % len(string.ascii_lowercase)
    code_dic[item[1]] = list_of_dictionary[new_index][1]

decode_dic = {value:key for key, value in code_dic.items()}

# code
code_string = ""
for each in input_string:
    if each in code_dic:
        code_string += code_dic[each]
    else:
        code_string += each

print("Code string:", code_string)

# decode
decode_string = ""
for each in code_string:
    if each in decode_dic:
        decode_string += decode_dic[each]
    else:
        decode_string += each

print("Decode string:", decode_string)
