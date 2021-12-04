from statistics import multimode


def load(name: str):
    with open(name, "r") as file:
        return [line[:-1] for line in file.readlines() if line]


def get_most_common_value_on_position(_input: list, _position: int, _prefix: list = None):
    result_array = []
    prefix = ''.join(_prefix) if _prefix is not None else ''

    for _row in _input:
        try:
            if _prefix is None or _row.index(prefix) == 0:
                result_array.append(_row[_position])

        except ValueError:
            pass

    result = multimode(result_array)
    size_of_result = len(result)

    return result[0] if size_of_result == 1 else '1'


def get_least_common_value_on_position(_input: list, _position: int, _prefix: list):
    result_array = []
    prefix = ''.join(_prefix) if _prefix is not None else ''

    for _row in _input:
        try:
            if _prefix is None or _row.index(prefix) == 0:
                result_array.append(_row[_position])

        except ValueError:
            pass

    result = multimode(result_array)
    size_of_result = len(result)

    if len(result_array) == 1:
        return result[0]

    elif size_of_result > 1 or result[0] == '1':
        return '0'

    else:
        return '1'


def part1(_input: list):
    gamma_rate = []
    _size = len(_input[0])

    for i in range(_size):
        most_common_value = get_most_common_value_on_position(_input, i)
        gamma_rate.append(most_common_value)

    epsilon_rate = ['0' if c == '1' else '1' for c in gamma_rate]
    gamma_rate_value = int(''.join(gamma_rate), 2)
    epsilon_rate_value = int(''.join(epsilon_rate), 2)

    return gamma_rate_value * epsilon_rate_value


def part2(_input: list):
    oxygen_rating = []
    co2_scrubber_rating = []
    _size = len(_input[0])

    index = 0
    while index < _size:
        most_common_value = get_most_common_value_on_position(_input, index, oxygen_rating)
        index += 1

        if most_common_value:
            oxygen_rating.append(most_common_value)

    index = 0
    while index < _size:
        most_common_value = get_least_common_value_on_position(_input, index, co2_scrubber_rating)
        index += 1

        if most_common_value:
            co2_scrubber_rating.append(most_common_value)

    oxygen_rating_value = int(''.join(oxygen_rating), 2)
    co2_scrubber_rating_value = int(''.join(co2_scrubber_rating), 2)

    return oxygen_rating_value * co2_scrubber_rating_value


if __name__ == '__main__':
    input_array = load('input-3')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
