from collections import Counter


def load(name: str) -> tuple:
    with open(name, "r") as file:
        template = file.readline().replace('\n', '')
        pairs = [line.replace('\n', '') for line in file.readlines() if line.replace('\n', '')]

        return template, pairs


def get_pair_indexes(_polymer: str, xy: str) -> list:
    indexes = []
    i = 0

    while i < len(_polymer):
        try:
            index = _polymer[i:].index(xy)
            indexes.append(index + i)
            i += index+1
            continue

        except ValueError:
            i += 1

    return indexes


def insertion(_polymer: str, pairs: list):
    new_elements = []

    for pair in pairs:
        xy, z = pair.split(' -> ')
        occurrences = _polymer.count(xy)

        if occurrences == 0:
            continue

        new_element_indexes = get_pair_indexes(_polymer, xy)

        for index in new_element_indexes:
            insert_element = index + 1, z
            new_elements.append(insert_element)

    new_elements = sorted(new_elements, reverse=True)
    new_polymer = list(_polymer)

    for index, element in new_elements:
        new_polymer.insert(index, element)

    return ''.join(new_polymer)


def part1(_input: tuple) -> int:
    polymer, pairs = _input

    for i in range(10):
        _polymer = insertion(polymer, pairs)
        polymer = _polymer[:]

    elements = Counter(polymer)
    most_common_element = max(elements.values())
    least_common_element = min(elements.values())

    return most_common_element - least_common_element


def compute_step(_polymer: Counter, pairs_rules: dict) -> Counter:
    new_polymer = Counter()

    for key, value in pairs_rules.items():
        occurrences = _polymer[key]

        if occurrences == 0:
            continue

        pair_a, pair_b = value
        new_polymer[pair_a] += occurrences
        new_polymer[pair_b] += occurrences

    return new_polymer


def part2(_input: tuple) -> int:
    polymer, pairs = _input
    polymer_dict = Counter()
    pairs_rules = {}

    for pair in pairs:
        xy, z = pair.split(' -> ')
        x, y = xy
        rule = [''.join([x, z]), ''.join([z, y])]
        pairs_rules[xy] = rule
        occurrences = polymer.count(xy)

        if occurrences > 0:
            polymer_dict[xy] += occurrences

    for i in range(40):
        polymer_dict = compute_step(polymer_dict, pairs_rules)

    elements = Counter()

    for key, value in polymer_dict.items():
        element_a, element_b = key
        elements[element_a] += value
        elements[element_b] += value

    elements[polymer[0]] += 1
    elements[polymer[-1]] += 1

    most_common_element = max(elements.values())
    least_common_element = min(elements.values())

    return (most_common_element - least_common_element) // 2


if __name__ == '__main__':
    input_array = load('input-14')

    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)

# too low 2304722022017
