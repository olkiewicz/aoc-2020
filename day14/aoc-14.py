class Memory:
    memory = {}
    x = set()

    def add_to_memory(self, mask, address, value):
        self.memory[address] = add(value, mask)

    def get_sum_of_values(self):
        sum = 0
        for val in self.memory.values():
            sum += val
        return sum


class MultiMemory:
    memory = {}

    def add_to_memory(self, mask, address, value):
        addresses = calculate_floating_address(address, mask)
        for adr in addresses:
            self.memory[adr] = value

    def get_sum_of_values(self):
        sum = 0
        for val in self.memory.values():
            # for ad in val:
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


def calculate_floating_address(address, mask):
    binary_number = convert_to_bin(address)
    size = len(binary_number)
    result = []
    for idx in range(size):
        mask_value = mask[idx]
        number_value = binary_number[idx]
        if mask_value in ('X', '1'):
            result.append(mask_value)
        else:
            result.append(number_value)
    text_result = ''.join(result)
    t = calculate_floating_results(text_result)
    x = [int(res, 2) for res in t]
    return x


def calculate_floating_results(bin_number):
    results = [bin_number]
    for idx in range(0, len(bin_number)):
        letter = bin_number[idx]
        if letter == 'X':
            results = calculate_multiple_floating_result(list(results), idx)
    final_result = []
    for res in results:
        if isinstance(res, str) and res.count('X') == 0:
            final_result.append(''.join(res))
    return final_result


def calculate_multiple_floating_result(numbers, float_index):
    size = len(numbers[0])
    counter = 0
    current_numbers = numbers
    while counter <= size:
        new_results = []
        for number in current_numbers:
            new_results += (calculate_single_floating_result(number, float_index))
        counter += 1
    return new_results


def calculate_single_floating_result(bin_number, float_index):
    if isinstance(bin_number, list):
        num = bin_number[0]
    else:
        num = bin_number
    zero_number = list(num)
    zero_number[float_index] = '0'
    one_number = list(num)
    one_number[float_index] = '1'
    return [''.join(zero_number), ''.join(one_number)]


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
    mm = MultiMemory()
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for line in puzzle_input:
        if line.count('mask') > 0:
            current_mask = line.replace('mask = ', '')
        else:
            address, value = line.replace(' ', '').split(']=')
            address = int(address.replace('mem[', ''))
            mm.add_to_memory(current_mask, address, int(value))
    print(mm.get_sum_of_values())
