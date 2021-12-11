def load(name: str) -> list:
    with open(name, "r") as file:
        numbers = []

        for line in file.readlines():
            numbers.append([int(char) for char in line.replace('\n', '') if char])

        return numbers


def increase_energy_level_around(_input: list[list[int]], _x: int, _y: int) -> list:
    size = len(_input[0])
    min_x = _x - 1 if _x > 0 else _x
    min_y = _y - 1 if _y > 0 else _y
    max_x = _x + 1 if _x + 1 < size else _x
    max_y = _y + 1 if _y + 1 < size else _y

    new_flash_of_octopuses = []

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if x == _x and y == _y:
                continue

            energy_level = _input[x][y]

            if energy_level == 9:
                _input[x][y] = 0
                # print(f'flash: {(x, y)}')
                # increase_energy_level_around(_input, x, y)
                new_flash_of_octopuses.append((x, y))

            elif energy_level != 0:
                # print(energy_level)
                _input[x][y] += 1
    return new_flash_of_octopuses
                # print(f'not flash: {(x, y)}, new energy lvl ={_input[x][y]}')
    # for x, y in new_flash_of_octopuses:
    #     print(f'new explosions: {x, y}')
    #     increase_energy_level_around(_input, x, y)
    # print(f'after flasing = {_input}')


def check_number_of_new_flashes(_input: list[list[int]]) -> int:
    number_of_flashes = 0
    size = len(_input)

    for x in range(size):
        for y in range(size):
            energy_level = _input[x][y]

            if energy_level == 0:
                number_of_flashes += 1

    return number_of_flashes


def part1(_input: list) -> int:
    number_of_flashes = 0
    size = len(_input)
    number_of_steps = 195

    current_step_new_flashes = 0
    for step in range(number_of_steps):
        current_step_flashes = []
        current_step_new_flashes = 0
        for x in range(size):
            for y in range(size):
                energy_level = _input[x][y]
                _input[x][y] = energy_level + 1

                if energy_level == 9:
                    current_step_flashes.append((x, y))
                    _input[x][y] = 0

        current_step_new_flashes = len(current_step_flashes)
        current_step_new_flashes_iter = current_step_flashes[:]
        flashed_octopuses = []

        while len(current_step_new_flashes_iter) > 0:
            # print(f'yo        ={_input}')
            new_iter_flashes = []
            for x, y in current_step_new_flashes_iter[:]:
                if (x, y) in flashed_octopuses:
                    current_step_new_flashes_iter.remove((x, y))
                    continue

                new_flashes = increase_energy_level_around(_input, x, y)
                flashed_octopuses.append((x, y))
                # print(f'yo,({x, y}={_input}')

                if new_flashes:
                    # print(f'new flashes: {new_flashes}')
                    new_iter_flashes += new_flashes
                current_step_new_flashes_iter.remove((x, y))
            if new_iter_flashes:
                current_step_new_flashes += len(new_iter_flashes)
                current_step_new_flashes_iter += new_iter_flashes

        step_flashes = check_number_of_new_flashes(_input)
        number_of_flashes += step_flashes
    # print(f'       {_input}')
    return number_of_flashes


def part2(_input: list) -> int:
    number_of_flashes = 0
    size = len(_input)
    number_of_steps = 1000

    current_step_new_flashes = 0
    for step in range(number_of_steps):
        current_step_flashes = []
        current_step_new_flashes = 0
        for x in range(size):
            for y in range(size):
                energy_level = _input[x][y]
                _input[x][y] = energy_level + 1

                if energy_level == 9:
                    current_step_flashes.append((x, y))
                    _input[x][y] = 0

        current_step_new_flashes = len(current_step_flashes)
        current_step_new_flashes_iter = current_step_flashes[:]
        flashed_octopuses = []

        while len(current_step_new_flashes_iter) > 0:
            # print(f'yo        ={_input}')
            new_iter_flashes = []
            for x, y in current_step_new_flashes_iter[:]:
                if (x, y) in flashed_octopuses:
                    current_step_new_flashes_iter.remove((x, y))
                    continue

                new_flashes = increase_energy_level_around(_input, x, y)
                flashed_octopuses.append((x, y))
                # print(f'yo,({x, y}={_input}')

                if new_flashes:
                    # print(f'new flashes: {new_flashes}')
                    new_iter_flashes += new_flashes
                current_step_new_flashes_iter.remove((x, y))
            if new_iter_flashes:
                current_step_new_flashes += len(new_iter_flashes)
                current_step_new_flashes_iter += new_iter_flashes

        step_flashes = check_number_of_new_flashes(_input)
        if step_flashes == size ** 2:
            return step + 1
        number_of_flashes += step_flashes
    # print(f'       {_input}')
    return 0


if __name__ == '__main__':
    input_array = load('input-11')
    input_array_part2 = load('input-11')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array_part2)
    print(result_part2)

# 219,220 too low
