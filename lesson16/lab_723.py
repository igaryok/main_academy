from lab_721 import Building


class Market(Building):

    def plus(self, count):
        self._Building__number += count / 2
        self.set_store_palace()

    def minus(self, count):
        self._Building__number -= count / 2
        self.set_store_palace()

    def __str__(self):
        return '{} {} {} {}'.format(
            self.material, self.color, self.store_place, self.show_number())


if __name__ == '__main__':
    obj1 = Market("brick", "white", 300)
    obj2 = Market("plank", "brown", 20)
    for each in (obj1, obj2):
        print(each)

    obj1.plus(50)
    obj2.minus(3)
    for each in (obj1, obj2):
        print(each)
