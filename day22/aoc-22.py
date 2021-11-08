def load(name):
    with open(name, "r") as file:
        content = file.readlines()

    size = len(content)
    player1 = [int(card.replace('\n', '')) for card in content[1: size // 2]]
    player2 = [int(card.replace('\n', '')) for card in content[size // 2 + 2:]]

    return player1, player2


def play_round(player_a, player_b):
    a_top = player_a[0]
    b_top = player_b[0]

    if a_top > b_top:
        player_a = player_a[1:] + [a_top, b_top]
        player_b = player_b[1:]
    else:
        player_a = player_a[1:]
        player_b = player_b[1:] + [b_top, a_top]

    return player_a, player_b


def play_game(player_a, player_b):
    while len(player_a) > 0 and len(player_b) > 0:
        player_a, player_b = play_round(player_a, player_b)

    return calculate_score(player_a, player_b)


def calculate_score(player_a, player_b):
    tab = player_a if len(player_a) > 0 else player_b
    score = 0

    for idx, num in enumerate(reversed(tab)):
        score += (idx + 1) * num

    return score


if __name__ == '__main__':
    p1, p2 = load('input-22')
    result_part1 = play_game(p1, p2)
    print(result_part1)


