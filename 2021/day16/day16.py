from typing import Optional


class Packet:
    def __init__(self, bits: str, version: int, type_id: int, number: int, length_type_id: str = None,
                 total_length: int = None, number_of_subpackets: int = None, subpackets: list = None):
        # self.bits = bits.rstrip('0') # maybe it should works in that way
        if subpackets is None:
            subpackets = []
        self.bits = bits
        self.version = version
        self.type_id = type_id
        self.number = number
        self.length_type_id = length_type_id
        self.total_length = total_length
        self.number_of_subpackets = number_of_subpackets
        self.subpackets = subpackets

    def get_version_number_with_subpackets(self):
        sum_of_version_numbers = self.version

        for subpacket in self.subpackets:
            sum_of_version_numbers += subpacket.get_version_number_with_subpackets()

        return sum_of_version_numbers


def load(name: str) -> str:
    with open(name, "r") as file:
        array = [int(digit, 16) for digit in file.readline() if digit]

        bin_array = []
        for hex_num in array:
            a = format(hex_num, '04b')
            bin_array.append(a)
        return ''.join(bin_array)


def get_literal_value_packet(binary_data: str) -> Optional[Packet]:
    size = len(binary_data)

    if size < 11:
        return None

    a = size - 11
    b = a % 5
    if size > 11 and b != 0:
        return None

    version = int(binary_data[:3], 2)
    type_id = int(binary_data[3:6], 2)

    if type_id != 4:
        return None

    index = 6
    number_bits = []
    has_last_group = False

    while True:
        # invalid packet!
        if index >= size:
            return None

        # if binary_data[index:index + 5]

        number_group = binary_data[index:index + 5]
        number_bits.append(number_group[1:])
        index += 5

        if binary_data[index - 5] == '0':
            index += 3
            has_last_group = True
            break

    number = int(''.join(number_bits), 2)
    extra_zeros = binary_data[index:]

    if not has_last_group or extra_zeros.count('1') > 0:
        return None

    return Packet(binary_data[:index], version, type_id, number)


def get_operator_packet(binary_data: str) -> Optional[Packet]:
    min_length_type_id0_length = 33
    min_length_type_id1_length = 39
    size = len(binary_data)
    version = int(binary_data[:3], 2)
    type_id = int(binary_data[3:6], 2)

    if type_id == 4:
        return None

    index = 6
    number_bits = []
    length_type_id = binary_data[index]
    index += 1
    total_length_of_subpackets = -1
    number_of_subpackets = -1
    subpackets = []

    if length_type_id == '0':
        total_length_of_subpackets = int(binary_data[index:index + 15], 2)
        index += 15
        print(f'total length={total_length_of_subpackets}')
        if total_length_of_subpackets < 11 or size < 22 + total_length_of_subpackets:
            return None
        subpackets = get_all_subpackets(binary_data[index:index + total_length_of_subpackets])
        print(subpackets)

        if len(subpackets) == 0:
            return None

    else:
        number_of_subpackets = int(binary_data[index:index + 11], 2)
        if number_of_subpackets == 0 or size < (18 + number_of_subpackets * 11):
            return None
        index += 11
        substring = binary_data[index:]
        subpackets = get_all_subpackets(substring, number_of_subpackets=number_of_subpackets)
        print(subpackets)
        if len(subpackets) < number_of_subpackets:
            return None

    return Packet(binary_data[:], version, type_id, 0, length_type_id, total_length_of_subpackets, number_of_subpackets, subpackets)


def get_all_subpackets(binary_data: str, number_of_subpackets: int = 0) -> list:
    subpackets = []
    size = len(binary_data)
    min_literal_value_packet_size = 11
    min_operator_packet_size = 18

    if size == min_literal_value_packet_size:
        subpacket = get_literal_value_packet(binary_data)
        if subpacket:
            subpackets.append(subpacket)
            return subpackets

    start_index = 0
    end_index = min_literal_value_packet_size
    while end_index < size:
        num = len(subpackets)
        if 0 < number_of_subpackets == len(subpackets):
            return subpackets
        for i in range(0, size - end_index + 1):
            substring = binary_data[start_index:end_index + i]
            if len(substring) < min_literal_value_packet_size:
                continue
            literal_value_packet = get_literal_value_packet(substring)
            if literal_value_packet:
                print(f'start={start_index}, end_index={end_index + i}, data={substring}')
                subpackets.append(literal_value_packet)
                start_index = end_index + i
                end_index += min_literal_value_packet_size
                break
            operator_packet = get_operator_packet(substring)
            if operator_packet:
                print(f'start={start_index}, end_index={end_index + i}, data={substring}')
                subpackets.append(operator_packet)
                start_index = end_index + i
                end_index += min_operator_packet_size
                break
        if len(subpackets) == num:
            break

    if 0 < number_of_subpackets != len(subpackets):
        return []

    return subpackets


def part1(binary_data: str) -> int:
    size = len(binary_data)
    master_operator_packet = get_operator_packet(binary_data)
    print(master_operator_packet)
    return master_operator_packet.get_version_number_with_subpackets()
    # version = int(binary_data[:3], 2)
    # type_id = int(binary_data[3:6], 2)
    # number = 0
    # index = 6
    # subpackets = []
    #
    # if type_id == 4: # literal value
    #     number_bits = []
    #
    #     while True:
    #         number_group = binary_data[index:index + 5]
    #         number_bits.append(number_group[1:])
    #         index += 5
    #
    #         if binary_data[index - 5] == '0':
    #             break
    #
    #     number = int(''.join(number_bits), 2)
    #     print(f'version={version}, type_id={type_id}, number={number}, index={index}, {binary_data[index:]}')
    #
    # else: # operator
    #     length_type_id = binary_data[index]
    #     index += 1
    #     if length_type_id == '0':
    #         total_length_of_subpackets = int(binary_data[index:index+15], 2)
    #         index += 15
    #         print(f'total length={total_length_of_subpackets}')
    #         subpackets = get_all_subpackets(binary_data[index:index + total_length_of_subpackets])
    #         print(subpackets)
    #     else:
    #         number_of_subpackets = int(binary_data[index:index+11], 2)
    #         index += 11
    #         print(f'number of subpackets={number_of_subpackets}')
    #         subpackets = get_all_subpackets(binary_data[index:], number_of_subpackets=number_of_subpackets)
    #         print(subpackets)
    #
    #     sum = 0
    #
    #     for subpacket in subpackets:
    #         sum += subpacket.get_version_number_with_subpackets()
    #
    #     return sum


def part2(edges: list) -> int:
    pass

if __name__ == '__main__':
    input_array = load('input-16')

    result_part1 = part1(input_array)
    print(result_part1)
    # result_part2 = part2(input_array)
    # print(result_part2)
