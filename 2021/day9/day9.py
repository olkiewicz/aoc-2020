import math


def load(name: str):
    with open(name, "r") as file:
        points = []

        for line in file.readlines():
            points.append([int(digit) for digit in line if digit.isdigit()])

        return points


def check_is_low_point(_input: list[list[int]], x: int, y: int) -> bool:
    size_x = len(_input)
    size_y = len(_input[0])

    digit = _input[x][y]
    digits = []

    if y > 0:
        digits.append(_input[x][y - 1])

    if y + 1 < size_y:
        digits.append(_input[x][y + 1])

    if x > 0:
        digits.append(_input[x - 1][y])

    if x + 1 < size_x:
        digits.append(_input[x + 1][y])

    yo = digit < min(digits)
    return yo


def part1(_input: list):
    lowest_points = []
    size_x = len(_input)
    size_y = len(_input[0])

    for x in range(size_x):
        for y in range(size_y):
            if check_is_low_point(_input, x, y):
                digit = _input[x][y]
                lowest_points.append(digit + 1)

    return sum(lowest_points)


def find_basin_size(low_point: tuple, _input: list) -> int:
    size_x = len(_input)
    size_y = len(_input[0])
    basin_points = [low_point]
    basin_points_checked = []

    while len(basin_points) > 0:
        for point in basin_points:
            x, y = point

            if x > 0:
                new_point = x - 1, y

                if _input[x - 1][y] != 9 and basin_points_checked.count(new_point) == 0:
                    basin_points.append(new_point)

            if y > 0:
                new_point = x, y - 1

                if _input[x][y - 1] != 9 and basin_points_checked.count(new_point) == 0:
                    basin_points.append(new_point)

            if y + 1 < size_y:
                new_point = x, y + 1

                if _input[x][y + 1] != 9 and basin_points_checked.count(new_point) == 0:
                    basin_points.append(new_point)

            if x + 1 < size_x:
                new_point = x + 1, y

                if _input[x + 1][y] != 9 and basin_points_checked.count(new_point) == 0:
                    basin_points.append(new_point)

            basin_points_checked.append(point)
            basin_points.remove(point)

    return len(list(set(basin_points_checked)))


def part2(_input: list):
    basins_size = []
    lowest_points = []
    size_x = len(_input)
    size_y = len(_input[0])

    for x in range(size_x):
        for y in range(size_y):
            if check_is_low_point(_input, x, y):
                lowest_points.append((x, y))

    for lowest_point in lowest_points:
        basin_size = find_basin_size(lowest_point, _input)
        basins_size.append(basin_size)

    result = math.prod(sorted(basins_size, reverse=True)[:3])

    return result


if __name__ == '__main__':
    input_array = load('input-9')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
