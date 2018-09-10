# /usr/bin/env python
"""
refactoring code from functions_lab.py
put into function calculate days in year
put into function deciding which planet year is bigger
"""

import math


def main():
    planets = {
        "orbital_radius": {
            "Mercury": 58,
            "Venus": 108,
            "Earth": 150,
            "Mars": 228,
            "Jupiter": 778,
            "Saturn": 1429,
            "Uranus": 2871,
            "Neptune": 4504
        },  # millions of kilometres
        "orbital_speed": {
            "Mercury": 47.87,
            "Venus": 35.02,
            "Earth": 29.78,
            "Mars": 24.13,
            "Jupiter": 13.07,
            "Saturn": 9.69,
            "Uranus": 6.81,
            "Neptune": 5.43
        }  # kilometres per second
    }

    print("You can enter any names of planets from the list.")
    print("If you enter empty string program will be finished")
    for item in planets["orbital_radius"].keys():
        print(item, end=" ")
    print()

    # create list of comparing planets
    list_of_planet = list()
    planet = True
    # The list will be created until you enter a empty string
    while planet:
        not_error = False
        while not not_error:
            try:
                planet = input("Planet " + str(len(list_of_planet)+1) + " :")
                if not planet:
                    not_error = True
                elif planet not in planets["orbital_radius"]:
                    raise KeyError
                else:
                    not_error = True
                    list_of_planet.append([planet])
            except KeyError:
                not_error = False
                print("You have entered wrong name of planet. Try again!")

    for each in list_of_planet:
        planet_year = days_in_year(planets["orbital_radius"][each[0]], planets["orbital_speed"][each[0]])
        print("The year is {} days on {}".format(int(planet_year), each[0]))
        each.append(planet_year)

    print("The {} year is bigger".format(which_bigger(tuple(list_of_planet))))


def days_in_year(radius, speed):
    orbital_radius = radius * 1000000  # turning millions of kilometres to kilometres
    planet_year = (2 * math.pi * orbital_radius / speed)
    planet_year = planet_year / (60 * 60 * 24)  # converting seconds to days

    return planet_year


def which_bigger(pln):

    return sorted(pln, key=lambda x: x[1], reverse=True)[0][0]


if __name__ == '__main__':
    main()
