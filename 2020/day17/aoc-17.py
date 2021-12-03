from collections import Counter
import math

number_of_cycles = 0
size_of_expanded_input = 0


def load(name):
    with open(name, "r") as file:
        lines = file.readlines()

    return [list(input_line.replace('\n', '')) for input_line in lines]


def is_neighbors(cube, neighbor_candidate):
    for idx, coordinate in enumerate(cube):
        if int(abs(coordinate - neighbor_candidate[idx])) > 1:
            return False

    return True


def find_active_neighbors(cube, current_state):
    active = []
    sum_of_active_neighbors = 0

    min_w = max(0, cube[3] - 1)
    max_w = min(len(current_state), cube[3] + 2)

    for w in range(min_w, max_w):
        min_z = max(0, cube[2] - 1)
        max_z = min(len(current_state), cube[2] + 2)

        for z in range(min_z, max_z):
            min_x = max(0, cube[0] - 1)
            max_x = min(size_of_expanded_input, cube[0] + 2)

            for x in range(min_x, max_x):
                min_y = max(0, cube[1] - 1)
                max_y = min(size_of_expanded_input, cube[1] + 2)

                for y in range(min_y, max_y):
                    if cube[0] == x and cube[1] == y and cube[2] == z and cube[3] == w:
                        continue

                    neighbor_candidate = (x, y, z, w)

                    if current_state[w][z][x][y] == '#' and is_neighbors(cube, neighbor_candidate):
                        sum_of_active_neighbors += 1
                        active.append(neighbor_candidate)

    return sum_of_active_neighbors


def calculate_next_cycle(current_state: list):
    fourth_dim_state = []
    for w, w_slice in enumerate(current_state):
        next_cycle_state = []
        for z, z_slice in enumerate(w_slice):
            next_cycle_state.insert(z, [])

            for x, x_slice in enumerate(z_slice):
                new_x_dim = []

                for y, y_slice in enumerate(x_slice):
                    num = find_active_neighbors((x, y, z, w), current_state)

                    if (z_slice[x][y] == '#' and num in (2, 3)) or num == 3:
                        new_x_dim.append('#')

                    else:
                        new_x_dim.append('.')

                next_cycle_state[z].append(new_x_dim)

        fourth_dim_state.append(next_cycle_state)

    return fourth_dim_state


def expand_init_state(_init_state: list):
    global number_of_cycles
    number_of_cycles = 6

    init_size = len(_init_state)

    global size_of_expanded_input
    size_of_expanded_input = init_size + number_of_cycles * 2
    size_of_third_dimension = number_of_cycles * 2 + 1
    first_dimension = ['.'] * size_of_expanded_input
    fourth_dim_states = []

    for w in range(size_of_third_dimension):
        expanded_states = []
        for z in range(size_of_third_dimension):
            expanded_states.append([first_dimension[:] for _ in range(size_of_expanded_input)])
        fourth_dim_states.append(expanded_states[:])

    for x in range(init_size):
        for y in range(init_size):
            fourth_dim_states[number_of_cycles][number_of_cycles][x + number_of_cycles][y + number_of_cycles] = _init_state[x][y]

    return fourth_dim_states


def calculate_part2(cubes):
    for idx in range(number_of_cycles):
        cubes = calculate_next_cycle(cubes)

    print(f'part2 = {[y for w in cubes for z in w for x in z for y in x].count("#")}')


if __name__ == '__main__':
    # puzzle_input = load('input-17')
    # init_state = expand_init_state(puzzle_input)
    # calculate_part2(init_state)
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    size = len(names)
    r = 6
    p = math.floor(r / size)
    l = math.log2(p)
    power_of_2 = 2 ** math.floor(l)
    rest = r - power_of_2 * size
    rest += size + 1

    dif = math.floor(rest / power_of_2)
    # print(f'p={p}, num={l} = rest{rest}, 2^={2 ** math.floor(l)}, dif={dif}')
    # rest = int((rest + 0) % size)

    print(f'p={p}, num={l} = rest{rest}, cola={names[dif % size]}')



