def simple_decorator(func):
    def decor(item):
        with open("config.data", "r+") as file:
            func(file, item)
    return decor


@simple_decorator
def write_config(file, string):
    data = file.read()
    if "Configuration file! Don't modify!" not in data:
        file.write("Configuration file! Don't modify!\n")
    file.write(string + "\n")


if __name__ == '__main__':
    str_data = ["1", "2", "3", "4", "5"]
    for each in str_data:
        write_config(each)
