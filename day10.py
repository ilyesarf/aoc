from get_input import get_input

input = [l.rstrip('\n') for l in get_input('10')]

#input = [l.rstrip('\n') for l in open('ex', 'r').readlines()]

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

def part1(input):
    strength = 0
    x = 1
    cycles = exec_cmds(input)
    
    for i, v in enumerate(cycles, start=1):
        if i in [j+1 for j in range(19, 221, 40)]:
            print(f"{(i, x)} = {i * x}")
            strength += x*i

        x += v

    return strength

print(part1(input))
        
