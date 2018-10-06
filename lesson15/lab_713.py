import lab_712 as lab2


if __name__ == '__main__':
    obg1 = lab2.Building("brick", "yellow", 200)
    obg2 = lab2.Building("plank", "red", 10)
    for each in (obg1, obg2):
        print(each.material, each.color, each.number, each.store_place)

    obg1.plus(1)
    obg2.minus(2)
    for each in (obg1, obg2):
        print(each.material, each.color, each.number, each.store_place)