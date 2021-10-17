def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [input_line.replace('\n', '') for input_line in lines]


def split_data(data):
    data = ''.join(data)
    return list(data)


def compute(first_num, op, second_num):
    first_num = int(first_num)
    second_num = int(second_num)
    if op == '+':
        return first_num + second_num
    else:
        return first_num * second_num


def compute_line_multiplication(_line):
    if len(_line) == 1:
        return _line[0]
    numbers_of_operators = _line.count('+') + _line.count('*')
    new_tab = []
    for idx in range(len(_line) - 2):
        first = _line[idx]
        if first not in ('+', '*', '(', ')'):
            operator = _line[idx + 1]
            second = _line[idx + 2]
            if operator == '*' and second not in ('+', '*', '(', ')'):
                new_tab = [compute(first, operator, second)]
                new_tab += _line[idx + 3:]
                break
    if numbers_of_operators > 1:
        return compute_line_multiplication(new_tab)
    else:
        return new_tab[0]


def compute_line(_line):
    if _line.count('+') == 0:
        return compute_line_multiplication(_line)
    elif len(_line) == 1:
        return _line[0]
    numbers_of_operators = _line.count('+') + _line.count('*')
    new_tab = []
    for idx in range(len(_line) - 2):
        first = _line[idx]
        if first not in ('+', '*', '(', ')'):
            operator = _line[idx + 1]
            second = _line[idx + 2]
            if operator == '+' and second not in ('+', '*', '(', ')'):
                new_tab = _line[0:idx]
                new_tab += [compute(first, operator, second)]
                new_tab += _line[idx + 3:]
                break
    if numbers_of_operators > 1:
        return compute_line(new_tab)
    else:
        return new_tab[0]


def compute_line_with_parentheses(line):
    if line.count('(') == 0:
        return compute_line(line)
    numbers_of_operators = line.count('+') + line.count('*')
    new_tab = []
    for idx in range(len(line) - 4):
        start = line[idx]
        # looking for end of parentheses
        end_idx = line.index(')')
        if line[idx + 1:end_idx].count('(') == 0 and start == '(':
            new_tab = line[0:idx]
            inside = line[idx + 1:end_idx]
            new_tab += [compute_line(inside)]
            new_tab += line[end_idx + 1:]
            break
    if numbers_of_operators > 1:
        return compute_line_with_parentheses(new_tab)
    else:
        return new_tab[0]


def sum_of_expressions(expressions):
    sum = 0
    for expression in expressions:
        sum += compute_line_with_parentheses(split_data(expression.split(' ')))
    return sum


if __name__ == '__main__':
    puzzle_input = load('input-18')
    res = sum_of_expressions(puzzle_input)
    print(f'{res}')

