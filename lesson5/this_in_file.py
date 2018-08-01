import sys

origin_stdout = sys.stdout

with open("dzen_file.txt", "w") as f:
    sys.stdout = f
    import this

sys.stdout = origin_stdout
print("Well done!")
