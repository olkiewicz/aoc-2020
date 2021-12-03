def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1] for line in lines]


def get_seat_id(boarding_pass_input, rows_range, columns_range):
    row = boarding_pass_input[:-3]
    column = boarding_pass_input[-3:]
    min_row, max_row = 0, rows_range
    min_col, max_col = 0, columns_range
    step = (rows_range + 1) / 2
    row_number, col_number = 0, 0
    for row_letter in row:
        if row_letter == 'F':
            max_row -= step
        else:
            min_row += step
        step /= 2
    if min_row == max_row:
        row_number = min_row
    step = (columns_range + 1) / 2
    for col_letter in column:
        if col_letter == 'L':
            max_col -= step
        else:
            min_col += step
        step /= 2
    if min_col == max_col:
        col_number = min_col
    return int((row_number * 8) + col_number)


if __name__ == '__main__':
    entries = load('input-5')
    max_seat_id = 0
    min_seat_id = 2000
    seat_ids = set()
    for entry in entries:
        seat_id = get_seat_id(entry, 127.0, 7.0)
        seat_ids.add(seat_id)
        if max_seat_id < seat_id:
            max_seat_id = seat_id
        if min_seat_id > seat_id:
            min_seat_id = seat_id
    print(f'result={max_seat_id}, {min_seat_id}')
    my_seat_id = 0
    for seat_id in range(min_seat_id, max_seat_id):
        if seat_id - 1 in seat_ids and seat_id + 1 in seat_ids and seat_id not in seat_ids:
            my_seat_id = seat_id
    print(my_seat_id)
