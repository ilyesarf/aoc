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


def compare(left, right):
    in_order = True 
    
    if type(left) == int and type(left) == type(right):
        in_order = left < right if left != right else None 
        return in_order

    elif type(left) == list and type(left) == type(right):  
        i = 0
        while True:
            if i == len(left) and i == len(right):
                return None
            elif i == len(left):
                return True
            elif i == len(right):
                return False

            in_order = compare(left[i], right[i])

            if in_order != None:
                return in_order 

            i += 1

    elif type(left) != type(right):
        if type(left) != list:
            left = [left]
        elif type(right) != list:
            right = [right]
        
        in_order = compare(left, right)

    return in_order


def part1():
    pairs = [[eval(pair[0]), eval(pair[1])] for pair in [input[i:i+2] for i in range(0, len(input), 2)]]

    score = 0
    for i in range(len(pairs)):
        left, right = pairs[i]
        if compare(left, right):
            score += i+1

    print(f'Part 1: {score}')

part1()

def sort(packets): #bubble sort
    for i in range(len(packets)):
        for j in range(len(packets)-i-1):
            
            in_order = compare(packets[j], packets[j+1]) 
            if in_order == False:
                packets[j], packets[j + 1] = packets[j+ 1], packets[j] #reverse order
    
    return packets

def part2():
    packets = [eval(pair) for pair in input]
    divider1 = [[2]]
    divider2 = [[6]]
    packets.append(divider1)
    packets.append(divider2)

    packets = sort(packets)

    score = (packets.index(divider1) + 1) * (packets.index(divider2) + 1)

    print(f'Part 2: {score}')

part2()
