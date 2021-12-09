from collections import Counter


def load(name: str):
    with open(name, "r") as file:
        return [line.replace('\n', '').split(' | ') for line in file.readlines() if line]


def part1(_input: list):
    digits = Counter()
    for _, line in _input:
        strings = line.split(' ')
        for string in strings:
            digit = len(string)
            digits[digit] += 1

    return digits[2] + digits[3] + digits[4] + digits[7]


def calculate_digits(segments: str) -> int:
    digits = {}
    patterns = segments[0].split(' ')
    digits_to_decode = segments[1].split(' ')

    for pattern in patterns[:]:
        size = len(pattern)

        if size == 2:
            digits[1] = pattern
            patterns.remove(pattern)

        elif size == 3:
            digits[7] = pattern
            patterns.remove(pattern)

        elif size == 4:
            digits[4] = pattern
            patterns.remove(pattern)

        elif size == 7:
            digits[8] = pattern
            patterns.remove(pattern)

    while len(patterns) > 0:
        for pattern in patterns[:]:
            size = len(pattern)

            if size == 5:
                if 9 in digits.keys():
                    segments_of_nine = 0

                    for c in digits[9]:
                        if pattern.count(c) > 0:
                            segments_of_nine += 1

                    if segments_of_nine == 5:
                        digits[5] = pattern
                        patterns.remove(pattern)
                        break

                elif pattern.count(digits[1][0]) > 0 and pattern.count(digits[1][1]) > 0:
                    segments_of_seven = 0

                    for c in digits[7]:
                        if pattern.count(c) > 0:
                            segments_of_seven += 1

                    if segments_of_seven == 3:
                        digits[3] = pattern
                        patterns.remove(pattern)
                        break

                if 3 in digits.keys() and 5 in digits.keys():
                    digits[2] = pattern
                    patterns.remove(pattern)
                    break

            if size == 6 and 3 in digits.keys():
                contains_one = all([characters in pattern for characters in digits[1]])
                contains_three = all([characters in pattern for characters in digits[3]])
                contains_five = all([characters in pattern for characters in digits[5]]) if 5 in digits.keys() else False

                if 3 in digits.keys() and contains_three and contains_one:
                    digits[9] = pattern
                    patterns.remove(pattern)
                    break

                elif contains_five:
                    digits[6] = pattern
                    patterns.remove(pattern)
                    break

                elif 6 in digits.keys() and 9 in digits.keys():
                    digits[0] = pattern
                    patterns.remove(pattern)
                    break

    if len(digits.keys()) == 10:
        sum_of_decoded_digits = 0

        for index, digit_to_decode in enumerate(digits_to_decode):
            for i in range(10):
                if len(digit_to_decode) == len(digits[i]) and all([characters in digit_to_decode for characters in digits[i]]):
                    sum_of_decoded_digits += 10 ** (3 - index) * i

        return sum_of_decoded_digits

    return 0


def part2(_input: list):
    result_sum = 0
    for line in _input:
        result_sum += calculate_digits(line)

    return result_sum


if __name__ == '__main__':
    input_array = load('input-8')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
