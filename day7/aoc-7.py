class Rule:
    color_code = ''
    children = {}
    is_empty = False

    def __init__(self, rule_input):
        self.children = {}
        self.is_empty = False
        self.color_code = ''
        self.color_code, content_text = rule_input[:-2].split(' bags contain ')
        children_texts = content_text.replace(' bags', '').split(', ')
        for children_text in children_texts:
            if children_text.count('no other') > 0:
                self.is_empty = True
            else:
                words = children_text.split(' ')
                quantity = words[0]
                bag_name = words[1] + ' ' + words[2]
                self.children[bag_name] = int(quantity)


def load(name):
    file = open(name, "r")
    lines = file.readlines()
    file.close()
    return lines


def get_number_of_bags(rules_input):
    first_level = []
    for rule_item in rules_input[:]:
        if 'shiny gold' in rule_item.children:
            first_level.append(rule_item.color_code)
            rules_input.remove(rule_item)
    number_of_bag_colors = len(first_level)
    previous_level_colors = first_level
    current_level_colors = []
    while len(rules_input) > 0:
        for previous_level_color_rule in previous_level_colors:
            for rule_item in rules_input:
                if previous_level_color_rule in rule_item.children:
                    current_level_colors.append(rule_item.color_code)
                    number_of_bag_colors += 1
                    try:
                        rules_input.remove(rule_item)
                    except ValueError:
                        pass
                    break
        if len(current_level_colors) == 0:
            break
        previous_level_colors += current_level_colors
        current_level_colors = []
    return number_of_bag_colors


def get_number_of_bags_part2(rules_input, shiny_bag_rule):
    calculated_bags = {}
    size_of_full_input = len(rules_input)
    for rule_item in rules_input[:]:
        if rule_item.is_empty:
            calculated_bags[rule_item.color_code] = 1
            rules_input.remove(rule_item)
    while len(calculated_bags) < size_of_full_input:
        last_value = len(calculated_bags)
        for rule_item in rules_input[:]:
            number_of_calculated_children = 0
            sum_of_calculated_children = 0
            for child in rule_item.children:
                if child in calculated_bags.keys():
                    number_of_calculated_children += 1
                    sum_of_calculated_children += rule_item.children[child] * calculated_bags[child]
            if number_of_calculated_children == len(rule_item.children):
                calculated_bags[rule_item.color_code] = sum_of_calculated_children + 1
                try:
                    rules_input.remove(rule_item)
                except ValueError:
                    pass
        if len(calculated_bags) == last_value:
            break
    number_of_calculated_children = 0
    sum_of_calculated_children = 0
    for child in shiny_bag_rule.children:
        if child in calculated_bags.keys():
            number_of_calculated_children += 1
            sum_of_calculated_children += shiny_bag_rule.children[child] * calculated_bags[child]
    if number_of_calculated_children == len(shiny_bag_rule.children):
        return sum_of_calculated_children


if __name__ == '__main__':
    entries = load('input-7')
    rules = []
    shiny_gold_bag = None
    for entry in entries:
        rule = Rule(entry)
        if rule.color_code == 'shiny gold':
            shiny_gold_bag = rule
        else:
            rules.append(rule)
    result = get_number_of_bags(rules)
    print(f'result={result}')
    result_part2 = get_number_of_bags_part2(rules, shiny_gold_bag)
    print(f'part2 result={result_part2}')
