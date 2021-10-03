import math


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1] for line in lines]


def calculate_result(array_input):
    timestamp = int(array_input[0])
    bus_ids = [int(bus) for bus in array_input[1].replace(',x', '').split(',')]
    min_timestamp, result = timestamp, 0
    for bus_id in bus_ids:
        time = math.ceil(timestamp / bus_id) * bus_id % timestamp
        if time < min_timestamp:
            min_timestamp = time
            result = time * bus_id
    # print(result)


def check_result(number, ids, idxs):
    for i in range(len(ids)):
        index = idxs[i]
        bus_id = ids[i]
        # print(f'num={number}, bus_id={bus_id}, idx={index}, XX={(number + index) % bus_id}')
        if not (number + index) % bus_id == 0:
            return False
    return True


def calculate_result_part2(array_input):
    entries = [bus for bus in array_input[1].split(',')]
    bus_ids, bus_idxs = [], []
    max_id, max_idx = 0, 0
    for index in range(len(entries)):
        bus_id = entries[index]
        if bus_id != 'x':
            bus_ids.append(int(bus_id))
            bus_idxs.append(index)
            if int(bus_id) > max_id:
                max_id, max_idx = int(bus_id), index
    first_bus_id = bus_ids[0] # 19
    # num = 380009752565841
    num = 0
    print(f'id={max_id}, idx={max_idx}')
    # print(check_result(1068781, bus_ids, bus_idxs))

    # while True:
    #     if check_result(num, bus_ids, bus_idxs):
    #         break
    #     num += first_bus_id
    #     print(num)
    return num


def find_z(first_number, second_number, a, b):
    num = 1
    while True:
        if (num + a) % first_number == 0 and  (num + b) % second_number == 0:
            print(num)
            break
        num += 1


if __name__ == '__main__':
    puzzle_input = load('input-13')
    # calculate_result(puzzle_input)
    # print(calculate_result_part2(puzzle_input))
    find_z(13, 19, 2, 3)
    find_z(17, 206, 0, 0)


# 380000000000000 too low
# 780000000000000 too high