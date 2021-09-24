def load(name):
    file = open(name, "r")
    return [line[:-1] for line in file.readlines()]


def count_trees(input, stepX, stepY):
    width = len(input[0])
    height = len(input)
    pos_x, pos_y = 0, 0
    tree_counter = 0
    pos_x = 0
    while pos_y < height:
        if input[pos_y][pos_x % width] == '#':
            tree_counter += 1
        pos_y += stepY
        pos_x += stepX
    return tree_counter


if __name__ == '__main__':
    input_array = load('input-3')
    slope_3_1 = count_trees(input_array, 3, 1)
    slope_1_1 = count_trees(input_array, 1, 1)
    slope_5_1 = count_trees(input_array, 5, 1)
    slope_7_1 = count_trees(input_array, 7, 1)
    slope_1_2 = count_trees(input_array, 1, 2)
    result_part2 = slope_5_1 * slope_1_2 * slope_7_1 * slope_1_1 * slope_3_1;
    print(result_part2)

