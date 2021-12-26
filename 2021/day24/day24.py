import math
from copy import copy


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


def reverse_alu(instructions: list[str]) -> list[int]:
    possible_values = []
    starting_variables = {'z': 0}

    # looking for "mul a 0"
    for instruction in instructions:
        commands = instruction.split(' ')

        if commands[0] == 'mul' and commands[2] == '0':
            starting_variables[commands[1]] = 0

    input_variable = instructions[0].split(' ')[1]
    for possible_z in range(-27, 27):
        for possible_value in range(1, 10):
            variables = copy(starting_variables)
            variables[input_variable] = possible_value
            variables['z'] = possible_z

            for instruction in instructions[1:]:
                commands = instruction.split(' ')

                if commands[0] == 'add':
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
            else:
                print(f'z={variables["z"]}')
                if variables['z'] == 0:
                    possible_values.append(possible_value)


    return possible_values


def part1(instructions: list[str]) -> int:
    values = reverse_alu(instructions[-18:])

    return len(values)


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