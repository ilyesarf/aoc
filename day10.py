from get_input import get_input
from textwrap import wrap
import os

if not os.getenv('DEBUG'):
    input = [l.rstrip('\n') for l in get_input('10')]
else:
    input = [l.rstrip('\n') for l in open('ex', 'r').readlines()]

def exec_cmds(input):
    cycles = []

    for inst in input:
        cmd = inst.split(' ')[0]
        if cmd == 'noop':
            cycles.append(0)
        elif cmd == 'addx':
            v = inst.split(' ')[1]
            cycles.extend([0, int(v)])

    return cycles

def get_char(cycle, x):
    if x == cycle or x+1 == cycle or x+2 == cycle:
        return '#'

    return '.'

def solve(input):
    strength = 0
    x = 1
    cycles = exec_cmds(input)
    crt = ''

    for i, v in enumerate(cycles, start=1):
        crt += get_char(i%40, x)
        if i in [j+1 for j in range(19, 221, 40)]:
            strength += x*i

        x += v

    print(f'Part 1: {strength}')
    print('\nPart 2:\n')
    for row in (wrap(crt, width=40)):
        print(row)


solve(input)
