import re

pattern = re.compile('[0-9a-f]{6}')


class Passport:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    cid = False

    def __init__(self, input):
        data = input.split(' ')
        for pair in data:
            if pair.count('byr') > 0:
                __value = int(pair.split(':')[1])
                if 1920 <= __value <= 2002:
                    self.byr = True
            elif pair.count('iyr') > 0:
                __value = int(pair.split(':')[1])
                if 2010 <= __value <= 2020:
                    self.iyr = True
            elif pair.count('eyr') > 0:
                __value = int(pair.split(':')[1])
                if 2020 <= __value <= 2030:
                    self.eyr = True
            elif pair.count('hgt') > 0 and len(pair) >= 8:
                __field = pair.split(':')[1]
                __value = int(__field[:-2])
                __unit = __field[-2:]
                if (__unit == 'cm' and 150 <= __value <= 193) or (__unit == 'in' and 59 <= __value <= 76):
                    self.hgt = True
            elif pair.count('hcl') > 0:
                __value = pair.split(':')[1]
                if pattern.match(__value[1:]):
                    self.hcl = True
            elif pair.count('ecl') > 0:
                __value = pair.split(':')[1]
                if __value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    self.ecl = True
            elif pair.count('pid') > 0:
                __value = pair.split(':')[1]
                try:
                    __number = int(__value)
                    if len(__value) == 9:
                        self.pid = True
                except ValueError:
                    pass
            elif pair.count('cid'):
                self.cid = ''

    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid  # and self.cid


def load(name):
    file = open(name, "r")
    content = file.read()
    file.close()
    return [data.replace('\n', ' ') for data in content.split('\n\n')]


if __name__ == '__main__':
    entries = load('input-4')
    valid_counter = 0
    for entry in entries:
        passport = Passport(entry)
        if passport.is_valid():
            valid_counter += 1
    print(f'result={valid_counter}')
