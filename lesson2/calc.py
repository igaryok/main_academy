def main():
    arg1 = input('Enter arg1: ')
    arg2 = input('Enter arg2: ')
    action = input('Enter action: ')

    if action == "+":
        print(int(arg1) + int(arg2))
    elif action == "-":
        print(int(arg1) - int(arg2))
    elif action == "/":
        print(int(arg1) / int(arg2))
    elif action == "*":
        print(int(arg1) * int(arg2))
    else:
        print("Unsupported action")

    return


main()
