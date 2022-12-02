from get_input import get_input

input = [line.rstrip('\n') for line in get_input('2')]
#input = ["A Y", "B X", "C Z"] #test

p1 = []
p2 = []
for i in input:
    p1.append(i.split(' ')[0])
    p2.append(i.split(' ')[1])


def part1(p1, p2):
    #[point, draw, loose, win]
    logic = {'X': [1, 'A', 'B', 'C'], 'Y': [2, 'B', 'C', 'A'], 'Z': [3, 'C', 'A', 'B']}
    
    full_score = 0
    for i in range(len(p1)):
        move1 = p1[i]
        move2 = logic[p2[i]]
        
        score = move2[0]
        if move1 == move2[1]:
            score += 3
        elif move1 == move2[3]:
            score += 6
    
        full_score += score
    
    return full_score

print(part1(p1, p2))

def part2(p1, p2):

    #[point, draw, win, loose]
    logic = {'A': [1, 'A', 'B', 'C'], 'B': [2, 'B', 'C', 'A'], 'C': [3, 'C', 'A', 'B']}
    #[loose, draw, win]
    states = ['X', 'Y', 'Z']

    full_score = 0
    for i in range(len(p1)):
        move1 = p1[i]
        score = states.index(p2[i])*3 #Points for state
        
        if p2[i] == states[0]: #loose
            move2 = logic[move1][3]
        elif p2[i] == states[1]: #draw
            move2 = move1
        elif p2[i] == states[2]: #win
            move2 = logic[move1][2]
        
        score += logic[move2][0]
        
        full_score += score

    return full_score

print(part2(p1, p2))
