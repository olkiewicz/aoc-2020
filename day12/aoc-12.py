import math


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1] for line in lines]


def calculate_manhattan_distance_part2(array_input):
    east_west_pos = 0
    north_south_pos = 0
    east_west_wp_pos = 10
    north_south_wp_pos = 1
    for command in array_input:
        instruction, value = command[0], int(command[1:])
        if instruction == 'N':
            north_south_wp_pos += value
        elif instruction == 'S':
            north_south_wp_pos -= value
        elif instruction == 'E':
            east_west_wp_pos += value
        elif instruction == 'W':
            east_west_wp_pos -= value
        elif instruction == 'R':
            if value == 90:
                east_west_wp_pos, north_south_wp_pos = north_south_wp_pos, -east_west_wp_pos
            elif value == 180:
                east_west_wp_pos, north_south_wp_pos = -east_west_wp_pos, -north_south_wp_pos
            elif value == 270:
                east_west_wp_pos, north_south_wp_pos = -north_south_wp_pos, east_west_wp_pos
        elif instruction == 'L':
            if value == 90:
                east_west_wp_pos, north_south_wp_pos = -north_south_wp_pos, east_west_wp_pos
            elif value == 180:
                east_west_wp_pos, north_south_wp_pos = -east_west_wp_pos, -north_south_wp_pos
            elif value == 270:
                east_west_wp_pos, north_south_wp_pos = north_south_wp_pos, -east_west_wp_pos
        elif instruction == 'F':
            east_west_pos += value * east_west_wp_pos
            north_south_pos += value * north_south_wp_pos
    return east_west_pos, north_south_pos


def calculate_manhattan_distance(array_input):
    east_west_pos = 0
    north_south_pos = 0
    angle = 0  # 0 - east, 90 - south, 180 - west, 270 - north
    for command in array_input:
        instruction, value = command[0], int(command[1:])
        print(east_west_pos, north_south_pos)
        if instruction == 'N':
            north_south_pos += value
        elif instruction == 'S':
            north_south_pos -= value
        elif instruction == 'E':
            east_west_pos += value
        elif instruction == 'W':
            east_west_pos -= value
        elif instruction == 'R':
            angle = (angle + value) % 360
        elif instruction == 'L':
            angle = (angle - value) % 360
        elif instruction == 'F':
            if angle == 0:
                east_west_pos += value
            elif angle == 90:
                north_south_pos -= value
            elif angle == 180:
                east_west_pos -= value
            elif angle == 270:
                north_south_pos += value
    return east_west_pos, north_south_pos


if __name__ == '__main__':
    puzzle_input = load('input-12')
    ea_pos, ns_pos = calculate_manhattan_distance(puzzle_input)
    print(math.fabs(ea_pos) + math.fabs(ns_pos))
    ea_pos_part2, ns_pos_part2 = calculate_manhattan_distance_part2(puzzle_input)
    print(math.fabs(ea_pos_part2) + math.fabs(ns_pos_part2))
