from typing import Optional


def load(name: str) -> tuple:
    with open(name, "r") as file:
        line = file.readline().rstrip()
        line = line.replace('target area: x=' , '')
        x_target, y_target = line.split(', y=')
        x = [int(num) for num in x_target.split('..')]
        y = [int(num) for num in y_target.split('..')]

        return x, y


def calculate_trajectory(velocity_x: int, velocity_y: int, target_x: list, target_y: list) -> Optional[int]:
    pos_x, pos_y = 0, 0
    max_y = 0

    while True:
        if velocity_x == 0 and (pos_x < target_x[0] or pos_x > target_x[1]):
            break

        if velocity_y < 0 and (pos_y < target_y[0]):
            break

        pos_x += velocity_x
        pos_y += velocity_y

        if max_y < pos_y:
            max_y = pos_y

        if target_x[0] <= pos_x <= target_x[1] and target_y[0] <= pos_y <= target_y[1]:
            return max_y

        if velocity_x > 0:
            velocity_x -= 1

        elif velocity_x < 0:
            velocity_x += 1

        velocity_y -= 1

    return None


def find_velocities(target_area: tuple) -> tuple:
    max_ys = []

    for x in range(0, target_area[0][1] + 1):
        for y in range(target_area[1][0], -target_area[1][0]):
            max_y = calculate_trajectory(x, y, target_area[0], target_area[1])

            if max_y or max_y == 0:
                max_ys.append(max_y)

    return max(max_ys), len(max_ys)


if __name__ == '__main__':
    input_array = load('input-17')

    result = find_velocities(input_array)
    print(result[0])
    print(result[1])

# 247 too low
# 1292 too low
# 4748