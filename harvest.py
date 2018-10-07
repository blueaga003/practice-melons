############
# Part 1   #
############

import pdb

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "muskmellon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", 2003, "orange", False, False, "casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", False, False, "crenshaw")
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    watermellon = MelonType("yw", 2013, "yellow", False, True, "yellow watermellon")
    watermellon.add_pairing("ice cream")
    all_melon_types.append(watermellon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("{} pairs well with {}".format(melon.name, melon.pairings))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types_dictionary = {}

    for melon in melon_types:
        melon_types_dictionary[melon.code] = melon.name

    return melon_types_dictionary

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating,
                harvested_field, harvested_by):
        """Initialize instance of Melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Returns true if the melon is sellable."""

        return ((self.shape_rating > 5) and
                (self.color_rating > 5) and
                (self.harvested_field != 3))


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    list_of_melons = []

    melon_1 = Melon(melon_types[3], 8, 7, 2, "Shiela")
    list_of_melons.append(melon_1)

    melon_2 = (melon_types[3], 3, 4, 2, "Shiela")
    list_of_melons.append(melon_2)

    melon_3 = (melon_types[3], 9, 8, 3, "Shiela")
    list_of_melons.append(melon_3)

    melon_4 = (melon_types[1], 10, 6, 35, "Shiela")
    list_of_melons.append(melon_4)

    melon_5 = (melon_types[2], 8, 9, 35, "Michael")
    list_of_melons.append(melon_5)

    melon_6 = (melon_types[2], 8, 2, 35, "Michael")
    list_of_melons.append(melon_6)

    melon_7 = (melon_types[2], 2, 3, 4, "Michael")
    list_of_melons.append(melon_7)

    melon_8 = (melon_types[0], 6, 7, 4, "Michael")
    list_of_melons.append(melon_8)

    melon_9 = (melon_types[3], 7, 10, 3, "Shiela")
    list_of_melons.append(melon_9)

    return list_of_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

types_of_melons = make_melon_types()
print_pairing_info(types_of_melons)
make_melon_type_lookup(types_of_melons)
(make_melons(types_of_melons))
