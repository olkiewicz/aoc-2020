from collections import Counter
from copy import copy


class DeterministicDice:
    def __init__(self):
        self.next_roll = 1
        self.number_of_rolls = 0

    def roll(self) -> int:
        self.number_of_rolls += 1
        roll_number = self.next_roll
        self.next_roll += 1

        return roll_number


class Universe:
    def __init__(self, player1_pos: int, player2_pos: int, player1_score: int = 0, player2_score: int = 0):
        self.player1_pos = player1_pos
        self.player2_pos = player2_pos
        self.player1_score = player1_score
        self.player2_score = player2_score

    def __repr__(self):
        return f'p1={self.player1_pos}, p2={self.player2_pos}, p1_score={self.player1_score}, p2_score={self.player2_score}'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if not isinstance(other, Universe):
            return False

        other_universe: Universe = other

        return other_universe.player1_pos == self.player1_pos and other_universe.player2_pos == self.player2_pos\
            and other_universe.player1_score == self.player1_score and other_universe.player2_score == self.player2_score


def load(name: str) -> list[int]:
    with open(name, "r") as file:
        return [int(line[28:].rstrip()) for line in file.readlines() if line]


def part1(starting_pos: list[int]) -> int:
    player1_pos, player2_pos = starting_pos
    player1_score = 0
    player2_score = 0
    dice = DeterministicDice()

    while player1_score < 1000 and player2_score < 1000:
        # player 1
        first_roll = dice.roll()
        second_roll = dice.roll()
        third_roll = dice.roll()

        player1_pos = (player1_pos + first_roll + second_roll + third_roll) % 10
        player1_score += player1_pos if player1_pos != 0 else 10

        if player1_score >= 1000:
            break

        # player 2
        first_roll = dice.roll()
        second_roll = dice.roll()
        third_roll = dice.roll()

        player2_pos = (player2_pos + first_roll + second_roll + third_roll) % 10
        player2_score += player2_pos if player2_pos != 0 else 10

    return min(player1_score, player2_score) * dice.number_of_rolls


def part2(starting_pos: list[int]) -> int:
    points_to_win = 21
    previous_universes = Counter()
    p1_winning_universes = Counter()
    p2_winning_universes = Counter()
    player1_pos, player2_pos = starting_pos

    starting_universe = Universe(player1_pos, player2_pos)
    previous_universes[starting_universe] = 1

    while len(previous_universes) > 0:
        # player1 turn
        # first roll
        new_universes = {}
        current_universes = {}
        for i in range(1, 4):
            for k, v in previous_universes.items():
                new_p1_pos = (k.player1_pos + i) % 10

                if new_p1_pos == 0:
                    new_p1_pos = 10

                new_universe = Universe(new_p1_pos, k.player2_pos, k.player1_score, k.player2_score)

                if new_universe in new_universes.keys():
                    new_universes[new_universe] += v

                else:
                    new_universes[new_universe] = v

            current_universes.update(new_universes)

        # second roll
        new_universes = {}
        previous_universes = copy(current_universes)
        current_universes = {}

        for i in range(1, 4):
            for k, v in previous_universes.items():
                new_p1_pos = (k.player1_pos + i) % 10

                if new_p1_pos == 0:
                    new_p1_pos = 10

                new_universe = Universe(new_p1_pos, k.player2_pos, k.player1_score, k.player2_score)

                if new_universe in new_universes.keys():
                    new_universes[new_universe] += v
                else:
                    new_universes[new_universe] = v

            current_universes.update(new_universes)

        # third roll
        new_universes = {}
        previous_universes = copy(current_universes)
        current_universes = {}

        for i in range(1, 4):
            for k, v in previous_universes.items():
                new_p1_pos = (k.player1_pos + i) % 10

                if new_p1_pos == 0:
                    new_p1_pos = 10
                new_universe = Universe(new_p1_pos, k.player2_pos, k.player1_score + new_p1_pos, k.player2_score)

                if new_universe.player1_score >= points_to_win:
                    if new_universe in p1_winning_universes.keys():
                        p1_winning_universes[new_universe] += v

                    else:
                        p1_winning_universes[new_universe] = v

                elif new_universe in new_universes.keys():
                    new_universes[new_universe] += v

                else:
                    new_universes[new_universe] = v

            current_universes.update(new_universes)
        new_universes = {}
        previous_universes = copy(current_universes)
        current_universes = {}

        # player 2 turn
        # first roll
        for i in range(1, 4):
            for k, v in previous_universes.items():
                new_p2_pos = (k.player2_pos + i) % 10

                if new_p2_pos == 0:
                    new_p2_pos = 10

                new_universe = Universe(k.player1_pos, new_p2_pos, k.player1_score, k.player2_score)

                if new_universe in new_universes.keys():
                    new_universes[new_universe] += v

                else:
                    new_universes[new_universe] = v

            current_universes.update(new_universes)

        # second roll
        new_universes = {}
        previous_universes = copy(current_universes)
        current_universes = {}

        for i in range(1, 4):
            for k, v in previous_universes.items():
                new_p2_pos = (k.player2_pos + i) % 10

                if new_p2_pos == 0:
                    new_p2_pos = 10

                new_universe = Universe(k.player1_pos, new_p2_pos, k.player1_score, k.player2_score)

                if new_universe in new_universes.keys():
                    new_universes[new_universe] += v

                else:
                    new_universes[new_universe] = v

            current_universes.update(new_universes)

        # third roll
        new_universes = {}
        previous_universes = copy(current_universes)
        current_universes = {}

        for i in range(1, 4):
            for k, v in previous_universes.items():
                new_p2_pos = (k.player2_pos + i) % 10

                if new_p2_pos == 0:
                    new_p2_pos = 10

                new_universe = Universe(k.player1_pos, new_p2_pos, k.player1_score, k.player2_score + new_p2_pos)

                if new_universe.player2_score >= points_to_win:
                    if new_universe in p2_winning_universes.keys():
                        p2_winning_universes[new_universe] += v

                    else:
                        p2_winning_universes[new_universe] = v

                elif new_universe in new_universes.keys():
                    new_universes[new_universe] += v

                else:
                    new_universes[new_universe] = v

            current_universes.update(new_universes)
        previous_universes = copy(current_universes)

    p1 = sum(p1_winning_universes.values())
    p2 = sum(p2_winning_universes.values())

    return max(p1, p2)


if __name__ == '__main__':
    input_array = load('input-21')

    result_part1 = part1(input_array)
    print(result_part1)
    result_part2 = part2(input_array)
    print(result_part2)
