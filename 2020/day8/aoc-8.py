def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1].split(' ') for line in lines]


def handle_part1(instructions):
    accumulator = 0
    index = 0
    executed_instructions = set()
    while True:
        instruction, number = instructions[index]
        number = int(number)
        if index in executed_instructions:
            print(accumulator)
            break
        executed_instructions.add(index)
        if instruction == 'acc':
            accumulator += number
            index += 1
        elif instruction == 'jmp':
            index += number
        else:
            index += 1


def handle_part2(instructions):
    size_of_byte_code = len(instructions)
    for i in range(size_of_byte_code+1):
        accumulator = 0
        index = 0
        executed_instructions = set()
        while True:
            if index >= size_of_byte_code:
                print(f'acc={accumulator}')
                break
            instruction, number = instructions[index]
            number = int(number)
            if index in executed_instructions:
                break
            executed_instructions.add(index)
            if instruction == 'acc':
                accumulator += number
                index += 1
            elif instruction == 'jmp':
                if index == i:
                    index += 1
                else:
                    index += number
            else:
                if index == i:
                    index += number
                else:
                    index += 1


if __name__ == '__main__':
    input = load('input-8')
    handle_part1(input)
    handle_part2(input)
