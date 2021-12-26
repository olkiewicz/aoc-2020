import math


def load(name: str) -> list[str]:
    with open(name, "r") as file:
        return [line.rstrip() for line in file.readlines() if line]


def alu(instructions: list[str], input_numbers) -> int:  # it's useless
    variables = {}

    for instruction in instructions:
        commands = instruction.split(' ')

        if commands[0] == 'inp':
            variables[commands[1]] = int(input_numbers[0])
            input_numbers = input_numbers[1:]

        elif commands[0] == 'add':
            a = commands[1]
            a_value = 0 if a not in variables else variables[a]
            b = commands[2]
            b_value = int(b) if b[0] == '-' or b.isnumeric() else (0 if b not in variables else variables[b])
            variables[a] = a_value + b_value

        elif commands[0] == 'mul':
            a = commands[1]
            a_value = 0 if a not in variables else variables[a]
            b = commands[2]
            b_value = int(b) if b[0] == '-' or b.isnumeric() else variables[b]
            variables[a] = a_value * b_value

        elif commands[0] == 'div':
            a = commands[1]
            a_value = 0 if a not in variables else variables[a]
            b = commands[2]
            b_value = int(b) if b[0] == '-' or b.isnumeric() else variables[b]
            variables[a] = math.floor(a_value / b_value)

        elif commands[0] == 'mod':
            a = commands[1]
            a_value = 0 if a not in variables else variables[a]
            b = commands[2]
            b_value = int(b) if b[0] == '-' or b.isnumeric() else variables[b]
            variables[a] = a_value % b_value

        elif commands[0] == 'eql':
            a = commands[1]
            a_value = 0 if a not in variables else variables[a]
            b = commands[2]
            b_value = int(b) if b[0] == '-' or b.isnumeric() else variables[b]
            variables[a] = 1 if a_value == b_value else 0

    return variables['z']


def part1(instructions: list[str]) -> int:
    # return alu(instructions, '13579246899999')
    input_numbers = 53579246899999

    # for current_input in reversed(range(53579246899999, 93579246899999)):
    for current_input in range(11111116671575, 93579246899999):
        print(current_input)
        current_input_str = str(current_input)

        if current_input_str.count('0') > 0:
            continue

        is_valid = alu(instructions, current_input_str) == 0

        if is_valid:
            return current_input

    return 0


def part2(instructions: list[list]) -> int:
    return 0


if __name__ == '__main__':
    input_array = load('input-24')

    result_part1 = part1(input_array)
    print(result_part1)
    # result_part2 = part2(input_array)
    # print(result_part2)


# 53579246899999 too low
# 93579246899999 too high