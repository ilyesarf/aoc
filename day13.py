from get_input import get_input
import os

if not os.getenv('DEBUG'):
    input = list(filter(None, get_input('13', lines=False).split('\n')))
else:
    ex = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    input = list(filter(None, ex.split('\n')))

pairs = [[eval(pair[0]), eval(pair[1])] for pair in [input[i:i+2] for i in range(0, len(input), 2)]]

def compare(left, right):
    is_correct = True 
    
    if type(left) == int and type(left) == type(right):
        is_correct = left < right if left != right else None 
        return is_correct

    elif type(left) == list and type(left) == type(right):  
        i = 0
        while True:
            if i == len(left) and i == len(right):
                return None
            elif i == len(left):
                return True
            elif i == len(right):
                return False

            is_correct = compare(left[i], right[i])

            if is_correct != None:
                return is_correct 

            i += 1

    elif type(left) != type(right):
        if type(left) != list:
            left = [left]
        elif type(right) != list:
            right = [right]
        
        is_correct = compare(left, right)

    return is_correct


def part1(pairs):
    score = 0
    for i in range(len(pairs)):
        left, right = pairs[i]
        if compare(left, right):
            score += i+1

    print(f'Part 1: {score}')

part1(pairs)
"""
i = 3 
print(f'------------DEBUG {(i+1)}------------')
print()
left, right = pairs[i]
print(compare(left, right))
"""