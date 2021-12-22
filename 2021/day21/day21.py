class DeterministicDice:
    def __init__(self):
        self.next_roll = 1
        self.number_of_rolls = 0

    def roll(self) -> int:
        self.number_of_rolls += 1
        roll_number = self.next_roll
        self.next_roll += 1

        return roll_number


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
        print(player1_score, player2_score)

    result = min(player1_score, player2_score) * dice.number_of_rolls

    return result


if __name__ == '__main__':
    input_array = load('input-21')

    result_part1 = part1(input_array)
    print(result_part1)
