from lab_721 import Building as Parent


class Market(Parent):

    def __init__(self, material, color, price, number=0):
        Parent.__init__(self, material, color, number)
        self.price = price

    def __str__(self):
        return '{} {} {} {} {}'.format(
            self.material, self.color, self.price, self.store_place, self.show_number())


if __name__ == '__main__':
    obj1 = Market("brick", "white", 1.2, 300)
    obj2 = Market("plank", "brown", 2.1, 20)
    for each in (obj1, obj2):
        print(each)
