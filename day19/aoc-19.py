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
            self.valid_messages = messages
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
    messages = [list(m) for m in message.split(' | ')]
    for m in messages:
        m.remove(' ')
    res = []
    unique_rules = list(set(message.replace('| ', '').split(' ')))
    for mes in unique_rules:
        if mes not in unique_rules:
            return None
        else:
            x = [r for r in multiply_rules(mes, messages, calculated_rules_dict) if r]
            res += x
    return res


def multiply_rules(rule_number: int, messages: list, unique_rules: dict):
    size_of_used_number = len(unique_rules[rule_number])
    res = []
    for message in messages:
        if str(rule_number) in message:
            for i in range(size_of_used_number):
                liter = unique_rules[rule_number][i]
                text = ''.join([p.replace(f'{rule_number}', liter) for p in message])
                res.append(text)
    return res


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
        print(rule)
        if rule.is_calculated:
            calculated_rules[rule.number] = rule.valid_messages
        else:
            rules.append(rule)
    for rule in rules:
        if rule.compute_valid_messages(calculated_rules):
            new_definitions = get_valid_messages(rule.definition, calculated_rules)
            # calculated_rules[rule.number] = rule.valid_messages
            calculated_rules[rule.number] = new_definitions
            #rules.remove(rule)
    print(calculated_rules)
