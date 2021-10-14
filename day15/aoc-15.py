import math


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [line[:-1] for line in lines]


if __name__ == '__main__':
    # puzzle_input = load('input-14')
    value = 7.304
    text, text_fraction = str(value).split('.')
    size = len(text)
    size_fraction = len(text_fraction)
    res = [str(int(text[digit]) * 10 ** (size - digit - 1)) for digit in range(size) if text[digit] != '0']
    # res_fraction = [str(f'{int(text_fraction[digit]) * 10 ** (size_fraction - digit - 1)}') for digit in range(size_fraction) if text_fraction[digit] != '0']
    res_fraction = [f'{int(text_fraction[digit])}/{10 ** (digit + 1)}' for digit in range(size_fraction) if text_fraction[digit] != '0']
    print(' + '.join(res + res_fraction))
