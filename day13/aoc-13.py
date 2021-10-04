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
        if not (number + index) % bus_id == 0:
            return False
    return True


def calculate_result_part22(array_input):
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
    first_bus_id = bus_ids[0]
    number = calculate_first_step(first_bus_id, bus_ids[1], bus_idxs[1])
    step = first_bus_id * bus_ids[1]
    for idx in range(2, len(bus_ids)):
        current_bus = bus_ids[idx]
        number = calculate_next_step(number, first_bus_id, current_bus, bus_idxs[idx], step)
        step *= current_bus
    return number


def calculate_first_step(first_num, second_num, time_after):
    num = 0
    while True:
        if (num + time_after) % second_num == 0 and (num % first_num) == 0:
            return num
        num += first_num


def calculate_next_step(start, first_num, second_num, delay, step):
    num = start
    while True:
        if (num + delay) % second_num == 0 and (num % first_num) == 0:
            return num
        num += step


if __name__ == '__main__':
    puzzle_input = load('input-13')
    # calculate_result(puzzle_input)
    # print(calculate_result_part2(puzzle_input))
    # find_z(13, 19, 2, 3)
    # find_z(17, 206, 0, 0)
    # x = cal(0, 7, 13, 1)
    # print(f'res={x}')
    # y = cal_next(77, 7, 59, 4, 7*13)
    # print(y)
    # z = cal_next(350, 7, 31, 6, 7*13*59)
    # print(z)
    # a = cal_next(70147, 7, 19, 7, 7*13*59*31)
    # print(a)
    # ids = [7, 13, 59]
    # idxs = [0, 1, 4]
    # print(check_result(y, ids, idxs))
    print(calculate_result_part22(puzzle_input))


# 380000000000000 too low
# 780000000000000 too high