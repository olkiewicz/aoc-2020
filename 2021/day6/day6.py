from collections import Counter


def load(name: str):
    with open(name, "r") as file:
        _numbers = [line.replace('\n', '') for line in file.readlines() if line]
        return [int(number) for number in _numbers[0].split(',')]


def part1(_input: list):
    days = 80
    fishes = _input[:]
    next_day_fishes = []

    for day in range(days):
        number_of_new_fish = 0

        for fish in fishes:
            if fish == 0:
                next_day_fish = 6
                number_of_new_fish += 1

            else:
                next_day_fish = fish - 1

            next_day_fishes.append(next_day_fish)

        for i in range(number_of_new_fish):
            next_day_fishes.append(8)

        fishes = next_day_fishes[:]
        next_day_fishes = []

    return len(fishes)


def part2(_input: list):
    fishes = Counter(_input)
    days = 256
    next_day_fishes = Counter()

    for day in range(days):
        number_of_new_fish = fishes[0]

        for index in range(0, 8):
            next_day_fishes[index] = fishes[index + 1]

        next_day_fishes[6] += number_of_new_fish
        next_day_fishes[8] = number_of_new_fish
        fishes = next_day_fishes

    return sum(fishes.values())


if __name__ == '__main__':
    input_array = load('input-6')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
