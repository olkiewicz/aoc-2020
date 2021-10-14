def load(name):
    file = open(name, "r")
    content = file.read()
    file.close()
    return [int(line[:]) for line in content.split(',')]


def game(array_input):
    last_spoken = dict()
    spoken_numbers = dict()
    for idx in range(len(array_input)):
        num = array_input[idx]
        spoken_numbers[num] = [idx + 1]
    last_number = array_input[-1]
    counter = len(array_input) + 1
    while True:
        if counter == 30000001:
            return last_number
        if last_number not in last_spoken:
            last_number = 0
            if last_number in spoken_numbers:
                spoken_numbers[last_number] += [counter]
            else:
                spoken_numbers[last_number] = [counter]
            last_spoken[last_number] = counter
        else:
            if last_number in spoken_numbers and len(spoken_numbers[last_number]) > 1:
                a, b = spoken_numbers[last_number][-2:]
                # a, b = turns
                last_number = b - a
                if last_number in spoken_numbers:
                    spoken_numbers[last_number] += [counter]
                else:
                    spoken_numbers[last_number] = [counter]
                last_spoken[last_number] = counter
            else:
                last_number = 0
                spoken_numbers[last_number] += [counter]
                last_spoken[last_number] = counter
        counter += 1


if __name__ == '__main__':
    puzzle_input = load('input-15')
    res = game(puzzle_input)
    print(res)

