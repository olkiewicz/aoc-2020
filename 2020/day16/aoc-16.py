class Rule:
    def __init__(self, rule_line: str):
        rule_name, numbers = rule_line.split(': ')
        self.name = rule_name
        first, second = numbers.split(' or ')
        self.first = tuple(int(num) for num in first.split('-'))
        self.second = tuple(int(num) for num in second.split('-'))

    def check_number(self, num: int):
        return self.first[0] <= num <= self.first[1] or self.second[0] <= num <= self.second[1]

    def __str__(self):
        return f'Name: {self.name}, first rule: {self.first}, second rule: {self.second}'


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return [input_line.replace('\n', '') for input_line in lines]


def load_data(input_array):
    rules = []
    for idx in range(len(puzzle_input)):
        line = puzzle_input[idx]
        if line == 'your ticket:':
            my_ticket = tuple(int(num) for num in puzzle_input[idx + 1].split(','))
            nearby_tickets = []
            for ticket_line in puzzle_input[idx + 4:]:
                ticket = tuple(int(num) for num in ticket_line.split(','))
                nearby_tickets.append(ticket)
            break
        elif line != '':
            rule = Rule(line)
            rules.append(rule)
    return my_ticket, nearby_tickets, rules


if __name__ == '__main__':
    puzzle_input = load('input-16')
    my_ticket, nearby_tickets, rules = load_data(puzzle_input)
    size = len(my_ticket)
    numbers_of_rules = len(rules)
    completely_invalid = []
    sum_of_wrong_numbers = 0
    for ticket_idx in range(len(nearby_tickets)):
        nearby_ticket = nearby_tickets[ticket_idx]
        for number in nearby_ticket:
            invalid_number = 0
            for idx in range(len(rules)):
                rule = rules[idx]
                if rule.check_number(number):
                    pass
                else:
                    invalid_number += 1
                if invalid_number == size:
                    completely_invalid.append(ticket_idx)
                    sum_of_wrong_numbers += number
    for completely_invalid_idx in completely_invalid[::-1]:
        nearby_tickets.pop(completely_invalid_idx)
    possible_rules = dict()
    for rule in rules:
        possible_rules[rule.name] = []
        size_of_tickets = len(nearby_tickets)
        for idx in range(size):
            numbers_of_valid_tickets = 0
            for nearby_ticket in nearby_tickets:
                if not rule.check_number(nearby_ticket[idx]):
                    break
                numbers_of_valid_tickets += 1
            if numbers_of_valid_tickets == size_of_tickets:
                possible_rules[rule.name] += [idx]
    right_rules = []
    counter = 0
    while True:
        if counter == size:
            break
        # looking for a rule with one possible column
        handle_column_name: str
        handle_column_idx: int
        for key, value in possible_rules.items():
            if value is not None and len(value) == 1:
                handle_column_name, handle_column_idx = (key, value[0])
                break
        for key, value in possible_rules.items():
            if handle_column_idx in value:
                value.remove(handle_column_idx)
            possible_rules[key] = value
        right_rules.append([handle_column_name, handle_column_idx])
        counter += 1
    result = 1
    for rule in right_rules:
        rule_name, column = rule
        if rule_name.count('departure') > 0:
            val = my_ticket[column]
            result *= val
    print(result)
