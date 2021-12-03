def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1] for line in lines]


def transform_seat_part2(array_input, row, column):
    number_of_empty_seats = 0
    number_of_occupied_seats = 0
    row_size = len(array_input)
    column_size = len(array_input[0])
    # up
    c = column
    r = row - 1
    while r >= 0:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            r -= 1
    # down
    c = column
    r = row + 1
    while r < row_size:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            r += 1
    # left
    c = column + 1
    r = row
    while c < column_size:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            c += 1
    # right
    c = column - 1
    r = row
    while c >= 0:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            c -= 1
    # up-right
    c = column - 1
    r = row - 1
    while r >= 0 and c >= 0:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            r -= 1
            c -= 1
    # up-left
    c = column + 1
    r = row - 1
    while r >= 0 and c < column_size:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            r -= 1
            c += 1
    # down-right
    c = column - 1
    r = row + 1
    while r < row_size and c >= 0:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            r += 1
            c -= 1
    # down-left
    c = column + 1
    r = row + 1
    while r < row_size and c < column_size:
        seat = array_input[r][c]
        if seat == 'L':
            number_of_empty_seats += 1
            break
        elif seat == '#':
            number_of_occupied_seats += 1
            break
        else:
            r += 1
            c += 1
    seat = array_input[row][column]
    if seat == '#' and number_of_occupied_seats >= 5:
        return 'L'
    elif seat == 'L' and number_of_occupied_seats == 0:
        return '#'
    else:
        return seat


def transform_seat(array_input, row, column):
    number_of_empty_seats = 0
    number_of_occupied_seats = 0
    row_size = len(array_input)
    column_size = len(array_input[0])
    steps = 0
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            steps += 1
            if not (r == row and c == column):
                if 0 <= r < row_size and 0 <= c < column_size:
                    seat = array_input[r][c]
                    if seat == 'L':
                        number_of_empty_seats += 1
                    elif seat == '#':
                        number_of_occupied_seats += 1
    seat = array_input[row][column]
    if seat == 'L' and number_of_occupied_seats == 0:
        return '#'
    elif seat == '#' and number_of_occupied_seats >= 4:
        return 'L'
    else:
        return seat


def transform_seats(array_input):
    row = []
    rows = []
    for row_index in range(len(array_input)):
        for column_index in range(len(array_input[0])):
            seat = transform_seat(array_input[:], row_index, column_index)
            row.append(seat)
        rows.append(''.join(row))
        row = []
    return rows


if __name__ == '__main__':
    puzzle_input = load('input-11')
    new_puzzle = []
    while True:
        new_puzzle = transform_seats(puzzle_input)
        if puzzle_input == new_puzzle:
            break
        puzzle_input = new_puzzle[:]
    sum_of_occupied_seats = 0
    for rows in puzzle_input:
        sum_of_occupied_seats += rows.count('#')
    print(f'result={sum_of_occupied_seats}')
