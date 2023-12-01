from get_input import get_input
import os

SPELLED_DIGITS = {'one':'o1e', 'two':'t2o', 'three':'th3ee', 'four':'fo4r', 'five':'fi5e', 'six':'s6x', 'seven':'se7en', 'eight':'ei8ht','nine':'n9ne'}

if os.getenv('DEBUG') == '1':
    #part 1
    input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split('\n')

elif os.getenv('DEBUG') == '2':
    #part 2
    input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split('\n')
else:
    input = [l.strip() for l in get_input(1, 2023)]

def get_digits(line):
    digits = []
    for x in line:
        if x in "0123456789":
            digits.append(x)

    return digits


if __name__ == "__main__":
    sum = 0
    for line in input:

        for s,d in SPELLED_DIGITS.items():
            line = line.replace(s, d) #part2
        digits = get_digits(line)
        val = int(digits[0]+digits[-1])
        sum += val

        print(digits)

    print(f"result: {sum}")


