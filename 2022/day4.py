from get_input import get_input 
import os

if not os.getenv('DEBUG'):
    input = [l.rstrip('\n') for l in get_input('4')]
else:
    input = [l.rstrip('\n') for l in """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()]

def get_ranges(input):
    ranges = [range.split(',') for range in input]

    return ranges

def is_in(part, range1, range2):
    n = [i for i in range(int(range1.split('-')[0]), int(range1.split('-')[1])+1)]
    m = [i for i in range(int(range2.split('-')[0]), int(range2.split('-')[1])+1)]

    if part == '1':
        return set(n) <= set(m) or set(m) <= set(n) #check if range contains another range (part1)
    elif part == '2':
        return bool(set(n) & set(m)) #check if they overlap (part2)


ranges = get_ranges(input)

def solve(part, ranges):
    count = 0
    for i in range(len(ranges)):
        range1 = ranges[i][0]
        range2 = ranges[i][1]

        if is_in(part, range1, range2):
            count += 1

    print(f'Part {part}: {count}')

solve('1', ranges)
solve('2', ranges)
     
    
    
