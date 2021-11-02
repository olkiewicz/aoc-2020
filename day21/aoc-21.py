from collections import Counter
from copy import copy

all_ingredients = []


def load(name):
    with open(name, "r") as file:
        lines = file.readlines()

    _ingredients = []
    _allergens = []

    for line in lines:
        ingredient, allergen = line.replace(')\n', '').split(' (contains ')
        _ingredients.append(ingredient)
        _allergens.append(allergen)

    return _ingredients, _allergens


def collect_allergens(ingredients_arg, allergens_arg):
    global all_ingredients
    allergens_dict = {}

    for idx, allergen_entry in enumerate(allergens_arg):
        _ingredients = ingredients_arg[idx].split(' ')
        all_ingredients += _ingredients

        for allergen in allergen_entry.split(', '):

            if allergen not in allergens_dict:
                allergens_dict[allergen] = set()



            if len(allergens_dict[allergen]) == 0:
                allergens_dict[allergen].update(_ingredients)

            else:
                allergens_dict[allergen].intersection_update(_ingredients)

    return allergens_dict


if __name__ == '__main__':
    ingredients, allergens = load('input-21')
    allergens_dict = collect_allergens(ingredients, allergens)
    calculated_allergens = {}

    for key, value in copy(allergens_dict).items():
        if len(value) == 1:
            element = value.pop()
            calculated_allergens[key] = element
            allergens_dict.pop(key)

            for allergen in allergens_dict.keys():
                x = allergens_dict[allergen]

                if element in x:
                    allergens_dict[allergen].remove(element)

    while len(allergens_dict) > 0:
        for key, value in copy(allergens_dict).items():
            if len(value) == 1:
                element = value.pop()
                calculated_allergens[key] = element
                allergens_dict.pop(key)

                for allergen in allergens_dict.keys():
                    x = allergens_dict[allergen]

                    if element in x:
                        allergens_dict[allergen].remove(element)

    all_ingredients_counter = Counter(all_ingredients)

    for al in calculated_allergens.values():
        all_ingredients_counter.pop(al)
    sum = 0

    for val in all_ingredients_counter.values():
        sum += val

    print(sum)
    part2 = ','.join([value for key, value in sorted(calculated_allergens.items())])
    print()
    print(part2)

