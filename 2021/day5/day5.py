from functools import total_ordering


@total_ordering
class VentEnd:
    def __init__(self, end: str):
        x, y = end.split(',')
        self.__x = int(x)
        self.__y = int(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return f'{self.__x}, {self.__y}'

    def __eq__(self, other):
        return self.x == other.x and self.y and other.y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y

        else:
            return self.x < other.x

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y

        else:
            return self.x > other.x


class Vent:
    def __init__(self, line: str):
        _ends = line.split(' -> ')
        self.__first_end = VentEnd(_ends[0])
        self.__second_end = VentEnd(_ends[1])

    @property
    def first_end(self):
        return self.__first_end

    @property
    def second_end(self):
        return self.__second_end

    def __repr__(self):
        return f'{self.__first_end} -> {self.__second_end}'


def load(name: str):
    with open(name, "r") as file:
        return [Vent(line) for line in file.readlines() if line]


def part1(_input: tuple):
    size = 1000
    diagram = [[0] * size for i in range(size)]

    for vent in _input:
        _first_end = vent.first_end
        _second_end = vent.second_end

        if _first_end.x != _second_end.x and _first_end.y != _second_end.y:
            continue

        if _first_end > _second_end:
            _first_end, _second_end = _second_end, _first_end

        for i in range(_first_end.x, _second_end.x + 1):
            for j in range(_first_end.y, _second_end.y + 1):
                diagram[i][j] += 1

    result = 0

    for i in range(size):
        for j in range(size):
            if diagram[i][j] > 1:
                result += 1

    return result


def part2(_input: tuple):
    size = 1000
    diagram = [[0] * size for i in range(size)]

    for vent in _input:
        _first_end = vent.first_end
        _second_end = vent.second_end

        if _first_end > _second_end:
            _first_end, _second_end = _second_end, _first_end

        if _first_end.x == _second_end.x or _first_end.y == _second_end.y:
            for i in range(_first_end.x, _second_end.x + 1):
                for j in range(_first_end.y, _second_end.y + 1):
                    diagram[i][j] += 1

        else:
            x_step = 1
            y_step = 1 if _first_end.y < _second_end.y else -1
            number_of_steps = _second_end.x - _first_end.x
            start_x = _first_end.x
            start_y = _first_end.y

            for i in range(number_of_steps + 1):
                x = start_x + i * x_step
                y = start_y + i * y_step
                diagram[x][y] += 1

    result = 0

    for i in range(size):
        for j in range(size):
            if diagram[i][j] > 1:
                result += 1

    return result


if __name__ == '__main__':
    input_array = load('input-5')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
