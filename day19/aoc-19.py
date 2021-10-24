from collections import Counter


class Rule:
    # valid_messages = []
    # is_calculated = False

    def __init__(self, rule_line):
        number, definition = rule_line.split(': ')
        self.number = number
        if definition.count('"') > 0:
            self.valid_messages = [definition.replace('"', '')]
            self.is_calculated = True
            self.definition = ''
        else:
            self.valid_messages = []
            self.is_calculated = False
            self.definition = definition

    def compute_valid_messages(self, calculated_rules_dict: dict):
        definitions = self.definition.split(' | ')
        is_all_ok = True
        messages = []
        for d in definitions:
            numbers = d.split(' ')
            if set(numbers).issubset(calculated_rules_dict.keys()):
                #  print(f'{self.number}: SUKCEZ!')
                message = str(list([calculated_rules_dict[num] for num in numbers]))
                # for xd in calculated_rules_dict[num]:
                    # message = d.replace('')j
                    # pass
            else:
                is_all_ok = False
                #  print(f'{self.number}: porazka')
                break
            messages.append(str(message))
        if is_all_ok:
            self.is_calculated = True
            self.valid_messages = list(set(messages))
        return is_all_ok

    def __str__(self):
        text = f'[{self.number}] '
        if self.is_calculated:
            text += f'valid_messages: {self.valid_messages}'
        else:
            text += f'def: {self.definition}'
        return text


def get_valid_messages(message: str, calculated_rules_dict: dict):
    # messages = [list(m) for m in message.split(' | ')]
    # messages2 = list(set(message.replace('| ', '').split(' ')))
    messages = [m.split(' ') for m in message.split(' | ')]
    for m in messages:
        if m.count(' ') > 0:
            m.remove(' ')
    res = []
    unique_rules = list(set(message.replace('| ', '').split(' ')))
    for mes in unique_rules:
        if mes not in unique_rules:
            return None
        else:
            computed_rules = [r for r in list(set(multiply_rules(mes, messages, calculated_rules_dict))) if r]
            for chars in computed_rules:
                for char in chars:
                    if char.isdigit():
                        messages.append(chars)
                        break
                    res += computed_rules
    return res


def multiply_rules(rule_number, messages: list, unique_rules: dict):
    print(f'number: {rule_number}, messages: {messages}')
    size_of_used_number = len(unique_rules[rule_number])
    res = []
    for message in messages:
        mes = ' '.join(message)
        if str(rule_number) in mes:
            for i in range(size_of_used_number):
                liter = unique_rules[rule_number][i]
                # text = ''.join([p.replace(f'{rule_number}', liter) for p in mes]).replace(' ', '')
                text = ''.join([p.replace(f'{rule_number}', liter) for p in mes]).replace(' ', '')
                text = mes.replace(f'{rule_number}', liter).replace(' ', '')
                # text = [p.replace(f'{rule_number}', liter) for p in mes if p != ' ']
                res.append(text)
    # return list(set(res))
    return res


def clear_calculated_rules(_calculated_rules):
    # for _rule in _calculated_rules[:]:
    #     for char in _rule:
    #         if char.isdigit():
    #             _calculated_rules.remove(_rule)
    # return _calculated_rules
    c = [key for key in list(Counter(_calculated_rules).keys()) if has_no_digit(key)]
    return c


def has_no_digit(_text: str):
    for char in _text:
        if char.isdigit():
            return False
    return True


def load(name):
    file = open(name, "r")
    content = file.read()
    rules_input, data = content.split('\n\n')
    rules_input = rules_input.split('\n')
    data = data[:-1].split('\n')
    return rules_input, data


if __name__ == '__main__':
    rules_data, content_data = load('input-19')
    rules = []
    calculated_rules = {}
    for line in rules_data:
        rule = Rule(line)
        if rule.is_calculated:
            calculated_rules[rule.number] = rule.valid_messages
        else:
            rules.append(rule)
    for rule in rules[:]:
        if rule.compute_valid_messages(calculated_rules):
            print(f'calculate {rule.number}')
            new_definitions = get_valid_messages(rule.definition, calculated_rules)
            new_definitions = clear_calculated_rules(list(set(new_definitions)))
            # calculated_rules[rule.number] = rule.valid_messages
            calculated_rules[rule.number] = list(set(new_definitions))
            rules.remove(rule)
    for rule in rules:
        if rule.compute_valid_messages(calculated_rules):
            print(f'calculate {rule.number}')
            new_definitions = get_valid_messages(rule.definition, calculated_rules)
            new_definitions = clear_calculated_rules(list(set(new_definitions)))
            # calculated_rules[rule.number] = rule.valid_messages
            calculated_rules[rule.number] = list(set(new_definitions))
            rules.remove(rule)
    for rule in rules:
        if rule.compute_valid_messages(calculated_rules):
            print(f'calculate {rule.number}')
            new_definitions = get_valid_messages(rule.definition, calculated_rules)
            new_definitions = clear_calculated_rules(list(set(new_definitions)))
            # calculated_rules[rule.number] = rule.valid_messages
            calculated_rules[rule.number] = list(set(new_definitions))
            #rules.remove(rule)
    print(f'end = {calculated_rules}')
    print()
    print(content_data)
    result = 0
    for content in content_data:
        if content in calculated_rules['0']:
            result += 1
    print(result)
