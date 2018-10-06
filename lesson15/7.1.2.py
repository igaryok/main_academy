class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        self.set_store_palace()

    def set_store_palace(self):
        if self.number <= 0:
            self.store_place = "out of stock"
        elif self.number in range(1, 100):
            self.store_place = "warehouse"
        else:
            self.store_place = "Remote warehouse"

    def plus(self, n):
        self.number += n
        self.set_store_palace()

    def minus(self, n):
        self.number -= n
        self.set_store_palace()


obg1 = Building("brick", "white", 300)
obg2 = Building("plank", "brown", 20)
for each in (obg1, obg2):
    print(each.material, each.color, each.number, each.store_place)

obg1.plus(50)
obg2.minus(3)
for each in (obg1, obg2):
    print(each.material, each.color, each.number, each.store_place)
