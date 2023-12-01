from get_input import get_input
import os

if not os.getenv('DEBUG'):
    input = get_input('6', lines=False).rstrip('\n')
else:
    input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

def solution(input, len_to_marker):
    for i in range(len(input)):
        m = input[i:i+len_to_marker]
        if len(set(m)) == len_to_marker:
            return i+len_to_marker
    

print(f"Part 1: {solution(input, 4)}")
print(f"Part 2: {solution(input, 14)}")
