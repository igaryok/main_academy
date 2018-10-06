class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        if self.number <= 0:
            self.store_place = "out of stock"
        elif self.number in range(1, 100):
            self.store_place = "warehouse"
        else:
            self.store_place = "Remote warehouse"


obg1 = Building("cork", "red", 100)
obg2 = Building("straw", "yellow", 1)
