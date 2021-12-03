def load(name: str):
    with open(name, "r") as file:
        return [int(line) for line in file.readlines() if line]


def part1(_input: list):
    last = _input[0]
    result_array = []

    for number in _input[1:]:
        if number > last:
            result_array.append(number)

        last = number

    return len(result_array)


def part2(_input: list):
    result_array = []

    for idx, number in enumerate(_input[:-2]):
        _sum = _input[idx] + _input[idx + 1] + _input[idx + 2]
        result_array.append(_sum)

    return part1(result_array)


if __name__ == '__main__':
    input_array = load('input-1')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
