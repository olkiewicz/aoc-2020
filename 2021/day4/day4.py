class BingoNumber:
    def __init__(self, number: int):
        self.__number = number
        self.__drawn = False

    @property
    def number(self):
        return self.__number

    @property
    def drawn(self):
        return self.__drawn

    @drawn.setter
    def drawn(self, _drawn: bool):
        self.__drawn = _drawn

    def __repr__(self):
        return f'({self.__number}, {self.__drawn})'


def load(name: str):
    with open(name, "r") as file:
        file_input = file.read().split('\n\n')
        numbers_order = [int(number) for number in file_input[0].split(',') if number]
        _boards = [board for board in file_input[1:]]
        boards = []
        for _board in _boards:
            board = []
            _lines = [line for line in _board.split('\n') if line]
            for _line in _lines:
                line = [BingoNumber(int(number)) for number in _line.split(' ') if number]
                board.append(line)
            boards.append(board)

        return numbers_order, boards


def unmarked_numbers(board: list[list[BingoNumber]]):
    sum_of_unmarked_numbers = 0
    size = len(board[0])

    for i in range(size):
        for j in range(size):
            number = board[i][j]
            if not number.drawn:
                sum_of_unmarked_numbers += number.number

    return sum_of_unmarked_numbers


def check_for_a_win(board: list[list[BingoNumber]]):
    size = len(board[0])

    for index in range(size):
        if board[index][0].drawn and board[index][1].drawn and board[index][2].drawn and board[index][3].drawn and board[index][4].drawn:
            return unmarked_numbers(board)

    for index in range(size):
        if board[0][index].drawn and board[1][index].drawn and board[2][index].drawn and board[3][index].drawn and board[4][index].drawn:
            return unmarked_numbers(board)

    return 0


def part1(_input: tuple):
    drawn_numbers = _input[0]
    boards: list[list[list[BingoNumber]]] = _input[1]

    for drawn_number in drawn_numbers:
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    bingo_number = board[i][j]

                    if bingo_number.number == drawn_number:
                        bingo_number.drawn = True

            result = check_for_a_win(board)

            if result > 0:
                return drawn_number * result

    return 0


def part2(_input: tuple):
    drawn_numbers = _input[0]
    boards: list[list[list[BingoNumber]]] = _input[1]
    number_of_boards = len(boards)
    board_win_indexes = []

    for drawn_number in drawn_numbers:
        for board_index, board in enumerate(boards):
            if board_index in board_win_indexes:
                continue

            for i in range(len(board)):
                for j in range(len(board[i])):
                    bingo_number = board[i][j]

                    if bingo_number.number == drawn_number:
                        bingo_number.drawn = True

            result = check_for_a_win(board)

            if result > 0:
                if len(board_win_indexes) + 1 < number_of_boards:
                    board_win_indexes.append(board_index)
                else:
                    return drawn_number * result

    return 0


if __name__ == '__main__':
    input_array = load('input-4')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
