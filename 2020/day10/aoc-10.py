def load(name):
    with open(name, "r") as file:
        lines = file.readlines()

    return [int(line[:-1]) for line in lines]


def calculate_part1(array_numbers):
    adapters1 = []
    adapters2 = []
    adapters3 = []
    array_numbers.sort()
    last_number = array_numbers[0]

    if last_number == 1:
        adapters1.append(last_number)

    elif last_number == 2:
        adapters2.append(last_number)

    else:
        adapters3.append(last_number)

    for number in array_numbers[1:]:
        if number - 1 == last_number:
            adapters1.append(number)

        elif number - 2 == last_number:
            adapters2.append(number)

        elif number - 3 == last_number:
            adapters3.append(number)

        else:
            return number, last_number

        last_number = number

    return len(adapters1 * (len(adapters3) + 1))


def count_all_paths(_paths: list):
    size = len(_paths)
    diff = _paths[-1] - _paths[0]

    if size == 5 and diff == 4:
        return 7

    elif size == 4 and diff == 3:
        return 4

    elif size == 3 and diff == 2:
        return 2

    elif size == 2 and 3 >= diff > 0:
        return 1

    elif size == 1:
        return 1

    else:
        return 1


def find_chains(_paths):
    res = []
    current_head_idx = 0
    for idx, num in enumerate(_paths[1:]):
        diff = num - _paths[idx]

        if diff == 3:
            res.append(_paths[current_head_idx:idx+1])
            current_head_idx = idx+1

        elif idx == len(_paths) - 2:
            res.append(_paths[current_head_idx:])

    return res


def calculate_part2(chains):
    res = 1
    for chain in chains:
        res *= count_all_paths(chain)

    return res


if __name__ == '__main__':
    puzzle_input = load('input-10')
    part1 = calculate_part1(puzzle_input)
    print(f'part1 = {part1}')
    puzzle_input.sort()
    puzzle_input.insert(0, 0)
    chains = find_chains(puzzle_input)
    print(f'part2 = {calculate_part2(chains)}')
