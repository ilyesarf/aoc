from get_input import get_input

input = get_input('6', lines=False).rstrip('\n')
#input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

def solution(input):
    for i in range(len(input)):
        m = input[i:i+4]
        if len(set(m)) == 4:
            return i+4
    

print(solution(input))
