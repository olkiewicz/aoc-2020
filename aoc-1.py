
def load(name):
    file = open(name, "r")
    return [int(line) for line in file.readlines()]


def findTwoEntries(numbers):
    for x in numbers:
        for y in numbers:
            if 2020 - x == y:
                return (x, y)

def findThreeEntries(numbers):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if 2020 - x - z == y:
                    return (x, y, z)


if __name__ == '__main__':
    inputArray = load('input-1')
    a, b = findTwoEntries(inputArray)
    print(f'{a} * {b} = {a * b} ')
    x, y, z = findThreeEntries(inputArray)
    print(f'{x} * {y} * {z} = {x * y * z} ')

