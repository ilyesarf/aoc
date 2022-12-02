from get_input import get_input
#[point, draw, loose, win]

input = get_input('2')

#test_input = ["A Y\n", "B X\n", "C Z\n"]

p1 = []
p2 = []
for i in input:
    p1.append(i.split(' ')[0])
    p2.append(i.split(' ')[1].replace('\n', ''))


def part1(p1, p2):
    logic = {'X': [1, 'A', 'B', 'C'], 'Y': [2, 'B', 'C', 'A'], 'Z': [3, 'C', 'A', 'B']}

    full_score = 0
    for i in range(len(p1)):
        move2 = logic[p2[i]]
        score = move2[0]
        if p1[i] == move2[1]:
            score += 3
        elif p1[i] == move2[3]:
            score += 6
    
        full_score += score
    
    return full_score

print(part1(p1, p2))
      
