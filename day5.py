from get_input import get_input
from collections import defaultdict

input = [l if l == '\n' else l.rstrip('\n').replace('[', ' ').replace(']', ' ') for l in get_input('5')]


def get_crates(input):
    lines = input[:input.index('\n')-1]
    
    crates = [] 
    
    for i in range(len(lines)):
        line = lines[i]
        
        group = []
        for c in range(0, len(line)+1, 4):
            crate = line[c:c+3].strip()
            group.append(crate)
        
        crates.append(group)

    return crates 

def get_stacks():

    crates = get_crates(input)
    stacks = {str(id): [] for id in range(1, 10)}

    for id in stacks.keys():
        for group in crates:
            if group[int(id)-1] != '':
                stacks[id].append(group[int(id)-1])
    
    return stacks


def parse_instruct(inst):
    cut_inst = inst.split(' ')
    n = cut_inst[1]
    from_id = cut_inst[3]
    to_id = cut_inst[5]
    
    return n, from_id, to_id

def move_crates(n, from_id, to_id, stacks):
    stacks1 = stacks[from_id]
    stacks2 = stacks[to_id]
    
    crates = stacks1[:n]
    print(crates)
    
    for crate in crates:
        stacks2.insert(0, crate)
        stacks1.remove(crate)
     
    
    stacks[from_id] = stacks1
    stacks[to_id] = stacks2

    return stacks

def part1(input):    
    stacks = get_stacks()
    insts = input[input.index('\n')+1:]

    for inst in insts:
        n, from_id, to_id = parse_instruct(inst)
        stacks = move_crates(int(n), from_id, to_id, stacks)
    
    result = ''
    for k in stacks.keys():
        result += stacks[k][0]

    return result

print(part1(input))
