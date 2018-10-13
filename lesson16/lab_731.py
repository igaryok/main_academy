class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.__number = number
        self.set_store_palace()

    def set_store_palace(self):
        if self.__number <= 0:
            self.store_place = "out of stock"
        elif self.__number in range(1, 100):
            self.store_place = "warehouse"
        else:
            self.store_place = "Remote warehouse"

    def plus(self, n):
        self.__number += n
        self.set_store_palace()

    def minus(self, n):
        self.__number -= n
        self.set_store_palace()

    def show_number(self):
        return self.__number

    @staticmethod
    def factory():
        return [MarketFactory("brick", "white", 100), MarketFactory("plank", "brown", 10)]


class MarketFactory(Building):
    def __str__(self):
        return '{} {} {} {}'.format(
            self.material, self.color, self.store_place, self.show_number())


if __name__ == '__main__':
    obj = Building.factory()
    for each in obj:
        print(each)
