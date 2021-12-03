def load(name: str):
    with open(name, "r") as file:
        return [line for line in file.readlines() if line]


def part1(_input: list):
    horizontal_position = 0
    depth = 0

    for line in _input:
        _command, _value = line.split(' ')

        if _command == 'forward':
            horizontal_position += int(_value)

        elif _command == 'down':
            depth += int(_value)

        else:
            depth -= int(_value)

    return horizontal_position * depth


def part2(_input: list):
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in _input:
        _command, _value = line.split(' ')
        value = int(_value)

        if _command == 'forward':
            horizontal_position += int(value)
            depth += aim * value

        elif _command == 'down':
            aim += int(value)

        else:
            aim -= int(value)

    return horizontal_position * depth


if __name__ == '__main__':
    input_array = load('input-2')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
