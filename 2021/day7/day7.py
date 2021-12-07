import statistics


def load(name: str):
    with open(name, "r") as file:
        _numbers = [line.replace('\n', '') for line in file.readlines() if line]
        return [int(number) for number in _numbers[0].split(',')]


def part1(_input: list):
    k = statistics.median(_input)
    print(k)

    fuel_cost = 0
    for crab in _input:
        start, end = k, crab

        if start > end:
            start, end = end, start

        cost = end - start
        fuel_cost += cost

    return fuel_cost


def calculate_fuel_cost(distance: int):
    cost = 0
    for i in range(distance):
        cost += i + 1

    return cost


def part2(_input: list):
    result = 99999999

    for best_pos in range(min(_input), max(_input)):
        fuel_cost = 0
        for crab in _input:
            start, end = best_pos, crab

            if start > end:
                start, end = end, start

            distance = end - start
            fuel_cost += calculate_fuel_cost(distance)

        if fuel_cost < result:
            result = fuel_cost

    return result


if __name__ == '__main__':
    input_array = load('input-7')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
