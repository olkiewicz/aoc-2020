class Fifo:
    preamble_size = 0
    numbers = []

    def __init__(self, preamble_size, array):
        self.preamble_size = preamble_size
        self.numbers = array[:self.preamble_size]

    def __str__(self):
        return f'numbers={self.numbers}'

    def add_number(self, next_number):
        result = False
        for first_number in self.numbers:
            for second_number in self.numbers:
                if first_number != second_number and next_number == first_number + second_number:
                    result = True
                    break
        for idx in range(len(self.numbers) - 1):
            self.numbers[idx] = self.numbers[idx + 1]
        self.numbers[-1] = next_number
        return result


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [int(line[:-1]) for line in lines]


def add_next_numbers(array, index_start, size):
    sum = 0
    for idx in range(index_start, index_start + size):
        sum += array[idx]
    return sum


def find_weakness(input, number, size):
    size_of_set = 1
    while True:
        size_of_set += 1
        for idx in range(0, size - size_of_set):
            if add_next_numbers(input, idx, size_of_set) == number:
                result_array = input[idx:idx+17]
                min = number
                max = 0
                for num in result_array:
                    if num < min:
                        min = num
                    elif num > max:
                        max = num
                return min + max


if __name__ == '__main__':
    puzzle_input = load('input-9')
    size_of_preamble = 25
    fifo = Fifo(size_of_preamble, puzzle_input)
    for index in range(size_of_preamble, len(puzzle_input)):
        number = puzzle_input[index]
        res = fifo.add_number(number)
        if not res:
            print(f'idx={index}, res={number}')
            break
    result_part2 = find_weakness(puzzle_input, 14144619, 504)
    print(f'result_part2={result_part2}')
