from get_input import get_input

input = get_input('6', lines=False).rstrip('\n')
#input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

def solution(input, len_to_marker):
    for i in range(len(input)):
        m = input[i:i+len_to_marker]
        if len(set(m)) == len_to_marker:
            return i+len_to_marker
    

print(f"Part 1: {solution(input, 4)}")
print(f"Part 2: {solution(input, 14)}")
