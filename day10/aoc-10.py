def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [int(line[:-1]) for line in lines]


def find_result(array_numbers):
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
    print(f'ad1={len(adapters1)}, ad2={len(adapters2)}, ad3={len(adapters3)+1}')
    print(f'result={len(adapters1 * (len(adapters3) + 1))}')


if __name__ == '__main__':
    puzzle_input = load('input-10')
    res = find_result(puzzle_input)
    print(f'err={res}')

# 156423 is too low