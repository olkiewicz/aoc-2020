class Memory:
    memory = {}

    def add_to_memory(self, mask, address, value):
        self.memory[address] = add(value, mask)

    def get_sum_of_values(self):
        sum = 0
        for val in self.memory.values():
            sum += val
        return sum


def convert_to_bin(number):
    bin_num = bin(number)
    text = f'{bin_num}'[2:]
    return text.zfill(36)


def add(number, mask):
    binary_number = convert_to_bin(number)
    size = len(binary_number)
    result = []
    for idx in range(size):
        mask_value = mask[idx]
        if mask_value != 'X':
            result.append(mask_value)
        else:
            result.append(binary_number[idx])
    text_result = ''.join(result)
    return int(text_result, 2)


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1] for line in lines]


def calculate_result(array_input):
    memory = Memory()
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in array_input:
        if line.count('mask') > 0:
            current_mask = line.replace('mask = ', '')
        else:
            address, value = line.replace(' ', '').split(']=')
            address = int(address.replace('mem[', ''))
            memory.add_to_memory(current_mask, address, int(value))
    print(memory.get_sum_of_values())




if __name__ == '__main__':
    puzzle_input = load('input-14')
    # x = convert_to_bin(11)
    # # print(x)
    # r = add(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
    # print(r)
    calculate_result(puzzle_input)
