from copy import copy


def load(name: str) -> list[list]:
    with open(name, "r") as file:
        return [list(line.rstrip()) for line in file.readlines() if line]


def part1(new_region_map: list[list]) -> int:
    step_number = 1
    size_height = len(new_region_map)
    size_width = len(new_region_map[0])

    while True:
        # step
        step_move = 0

        # east-facing herd move
        region_map = new_region_map[:]
        new_region_map = []

        for i in range(size_height):
            new_region_map.append(copy(region_map[i]))

        for i in range(size_height):
            for j in range(size_width):
                location = region_map[i][j]

                if location == '>':
                    adjacent_location_height = i
                    adjacent_location_width = (j + 1) % size_width
                    adjacent_location = region_map[adjacent_location_height][adjacent_location_width]

                    if adjacent_location == '.':
                        new_region_map[i][j] = '.'
                        new_region_map[adjacent_location_height][adjacent_location_width] = '>'
                        step_move += 1

        # south-facing herd move
        region_map = new_region_map[:]
        new_region_map = []

        for i in range(size_height):
            new_region_map.append(copy(region_map[i]))

        for i in range(size_height):
            for j in range(size_width):
                location = region_map[i][j]

                if location == 'v':
                    adjacent_location_height = (i + 1) % size_height
                    adjacent_location_width = j % size_width
                    adjacent_location = region_map[adjacent_location_height][adjacent_location_width]

                    if adjacent_location == '.':
                        new_region_map[i][j] = '.'
                        new_region_map[adjacent_location_height][adjacent_location_width] = 'v'
                        step_move += 1

        if step_move == 0:
            return step_number

        else:
            step_number += 1


def part2(new_region_map: list[list]) -> int:
    return 0


if __name__ == '__main__':
    input_array = load('input-25')

    result_part1 = part1(input_array)
    print(result_part1)
    # result_part2 = part2(input_array)
    # print(result_part2)
