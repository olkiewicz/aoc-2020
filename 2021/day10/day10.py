from queue import LifoQueue
from statistics import median


def load(name: str) -> list:
    with open(name, "r") as file:
        return [line.replace('\n', '') for line in file.readlines()]


def calculate_corrupted_chunk_score(_line: str) -> int:
    first_illegal_character = ''
    open_chunks = LifoQueue()
    open_chunk_characters = ('(', '[', '{', '<')
    close_chunk_characters = (')', ']', '}', '>')
    syntax_error_scores = [3, 57, 1197, 25137]

    for character in _line:
        if character in open_chunk_characters:
            open_chunks.put(character)

        else:
            current_open_chunk_character = open_chunks.get()
            index = open_chunk_characters.index(current_open_chunk_character)
            expected_close_chunk_character = close_chunk_characters[index]

            if character != expected_close_chunk_character:
                first_illegal_character = character
                break

    try:
        first_illegal_character_index = close_chunk_characters.index(first_illegal_character)

        return syntax_error_scores[first_illegal_character_index]

    except ValueError:
        return 0


def part1(_input: list) -> int:
    sum_of_chunk_scores = 0
    lines_to_remove = []

    for line in _input[:]:
        score = calculate_corrupted_chunk_score(line)

        if score != 0:
            lines_to_remove.append(line)

        sum_of_chunk_scores += score

    for line in lines_to_remove:
        _input.remove(line)

    return sum_of_chunk_scores


def calculate_incomplete_chunk_score(_line: str) -> int:
    result_score = 0
    open_chunks = LifoQueue()
    open_chunk_characters = ('(', '[', '{', '<')
    close_chunk_characters = (')', ']', '}', '>')

    for character in _line:
        if character in open_chunk_characters:
            open_chunks.put(character)

        else:
            current_open_chunk_character = open_chunks.get()
            index = open_chunk_characters.index(current_open_chunk_character)
            expected_close_chunk_character = close_chunk_characters[index]

            if character != expected_close_chunk_character:
                break

    while not open_chunks.empty():
        current_open_chunk_character = open_chunks.get()
        index = open_chunk_characters.index(current_open_chunk_character)
        result_score *= 5
        result_score += (index + 1)

    return result_score


def part2(_input: list) -> int:
    scores = []

    for line in _input:
        score = calculate_incomplete_chunk_score(line)
        scores.append(score)

    return median(scores)


if __name__ == '__main__':
    input_array = load('input-10')
    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
