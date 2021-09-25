def load(name):
    file = open(name, "r")
    content = file.read()
    file.close()
    return [data.replace('\n', ' ') for data in content.split('\n\n')]


def count_questions(group_input):
    questions = set()
    for letter in group_input:
        if letter != ' ':
            questions.add(letter)
    return len(questions)


def count_question_part2(group_input):
    groups = group_input.split(' ')
    number_of_groups = len(groups)
    questions = {}
    for group in groups:
        for letter in group:
            if letter in questions:
                questions[letter] += 1
            else:
                questions[letter] = 1
    result = 0
    for value in questions.values():
        if value == number_of_groups:
            result += 1
    return result


if __name__ == '__main__':
    entries = load('input-6')
    anyone_yes_sum = 0
    everyone_yes_sum = 0
    for entry in entries:
        anyone_yes_sum += count_questions(entry)
        everyone_yes_sum += count_question_part2(entry)
    print(anyone_yes_sum)
    print(everyone_yes_sum)
