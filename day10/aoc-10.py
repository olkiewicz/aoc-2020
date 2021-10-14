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


def count_paths(array_numbers):
    reversed_array = array_numbers[::-1]
    edges = dict()
    size = len(reversed_array)
    for num in range(size - 1):
        number = reversed_array[num]
        paths = 0
        if num + 1 < size and (reversed_array[num + 1] + 1 == number or reversed_array[num + 1] + 2 == number or reversed_array[num + 1] + 3 == number):
            paths += 1
        if num + 2 < size and (reversed_array[num + 2] + 1 == number or reversed_array[num + 2] + 2 == number or reversed_array[num + 2] + 3 == number):
            paths += 1
        if num + 3 < size and (reversed_array[num + 3] + 1 == number or reversed_array[num + 3] + 2 == number or reversed_array[num + 3] + 3 == number):
            paths += 1
        edges[number] = paths
    return edges


def count_result(dict_numbers: dict):
    res = 1
    previous_number = 1
    current_value = 0
    for key, value in dict_numbers.items():
        print(f'key={key} value={value} res={res} cur={current_value}')
        if value != 1:
            previous_number = value
            if current_value > 0:
                current_value *= previous_number
            else:
                current_value = previous_number
        else:
            if current_value > 0:
                res *= current_value
            current_value = 0

    return res


def find_result_part2(array_numbers):
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
    # res = find_result(puzzle_input)
    # red_part2 = find_result_part2(puzzle_input)
    puzzle_input.sort()
    print(puzzle_input)
    x = count_paths(puzzle_input)
    r = count_result(x)
    print(r)

# 156423 is too low
