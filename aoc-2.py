def computeLine(line):
    numbers, letter, password = line.split(' ')
    min, max = numbers.split('-')
    return (int(min), int(max), letter[:-1], password[:-1])


def load(name):
    file = open(name, "r")
    return [computeLine(line) for line in file.readlines()]


def isPasswordCorrect(args: []):
    minOccurences, maxOccurences, letter, password = args
    occurrences = password.count(letter)
    return minOccurences <= occurrences <= maxOccurences


def isPasswordCorrectPart2(args: []):
    firstOccurence, secondOccurence, letter, password = args
    firstCheck = password[firstOccurence - 1] == letter
    secondCheck = password[secondOccurence - 1] == letter
    return firstCheck != secondCheck


if __name__ == '__main__':
    inputArray = load('input-2')
    result, resultPart2 = 0, 0
    for line in inputArray:
        if isPasswordCorrect(line):
            result += 1
        if isPasswordCorrectPart2(line):
            resultPart2 += 1
    print(result)
    print(resultPart2)




