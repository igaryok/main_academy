from random import randint

def main():
    NUMBER = randint(0,100)
    answer = None
    while answer != NUMBER:
        answer = int(input("Enter your answer: "))
        if answer < NUMBER:
            print("Number is small")
        elif answer > NUMBER:
            print("Number is big")
        else:
            print("Exactly")

    return


main()